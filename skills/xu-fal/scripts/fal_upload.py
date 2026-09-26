"""uv run --with fal-client python fal_upload.py --manifest uploads.json file1 file2
Add --upload to execute. No model generation is performed.
"""
import argparse
import datetime
import getpass
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('files',nargs='+'); p.add_argument('--manifest',required=True)
    p.add_argument('--upload',action='store_true'); p.add_argument('--refresh',action='store_true')
    p.add_argument('--keychain-service'); p.add_argument('--prompt-key',action='store_true')
    a=p.parse_args(); paths=[Path(f).expanduser().resolve() for f in a.files]
    for path in paths:
        if not path.is_file(): p.error('Not a regular file: '+str(path))
    target=Path(a.manifest).expanduser().resolve()
    if target in paths: p.error('The manifest cannot be an input')
    data=json.loads(target.read_text()) if target.exists() else {'version':1,'uploads':{}}
    records=[]
    for path in paths:
        digest=hashlib.sha256()
        with path.open('rb') as stream:
            for block in iter(lambda:stream.read(1024*1024),b''): digest.update(block)
        records.append({'path':str(path),'sha256':digest.hexdigest(),'bytes':path.stat().st_size})
    if not a.upload:
        print(json.dumps({'mode':'local-only plan','files':records,'network_calls':0},indent=2)); return 0
    key=os.environ.get('FAL_KEY','').strip()
    if not key and a.keychain_service:
        result=subprocess.run(['security','find-generic-password','-s',a.keychain_service,'-w'],capture_output=True,text=True,timeout=30)
        if result.returncode==0: key=result.stdout.strip()
    if not key and a.prompt_key: key=getpass.getpass('fal API key (hidden, kept in memory): ').strip()
    if not key: p.error('No credential. Set FAL_KEY, select an existing Keychain service or use --prompt-key; never paste keys into chat.')
    try:
        from fal_client import SyncClient
    except ImportError: p.error('Use the official fal-client package; see --help.')
    client=SyncClient(key=key); target.parent.mkdir(parents=True,exist_ok=True)
    for record in records:
        old=data['uploads'].get(record['sha256'])
        if old and old.get('url') and not a.refresh:
            print(json.dumps({'status':'reused_receipt','path':record['path'],'url':old['url']})); continue
        try: url=client.upload_file(record['path'])
        except Exception as exc:
            print('Upload failed for '+Path(record['path']).name+': '+type(exc).__name__,file=sys.stderr); return 1
        record.update(url=url,status='storage_uploaded',assets_library_verified=False,uploaded_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
        data['uploads'][record['sha256']]=record
        temp=target.with_suffix(target.suffix+'.tmp'); temp.write_text(json.dumps(data,indent=2)+'\n'); temp.replace(target)
        print(json.dumps({'status':'storage_uploaded','path':record['path'],'url':url}))
    return 0

if __name__=='__main__': raise SystemExit(main())
