"""Register existing fal-hosted upload receipts in the public Assets API.

Public API contract: fal-ai-community/genmedia-cli, src/commands/assets/upload.ts
and src/lib/api.ts. Uses content hashes as idempotency keys.
"""
import argparse,json,subprocess,urllib.request
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('--manifest',required=True); p.add_argument('--keychain-service',required=True); p.add_argument('--label',default='')
a=p.parse_args(); path=Path(a.manifest); data=json.loads(path.read_text())
key=subprocess.run(['security','find-generic-password','-s',a.keychain_service,'-w'],capture_output=True,text=True,check=True).stdout.strip()
for digest,item in data['uploads'].items():
    if item.get('asset'): continue
    name=Path(item['path']).name; kind='video' if name.lower().endswith(('.mp4','.mov')) else 'image'
    body={'url':item['url'],'type':kind,'prompt':(a.label+' — ' if a.label else '')+name,'favorite':False,'tag_ids':[]}
    req=urllib.request.Request('https://api.fal.ai/v1/assets/uploads',data=json.dumps(body).encode(),headers={'Authorization':'Key '+key,'Content-Type':'application/json','Idempotency-Key':'asset-'+digest},method='POST')
    with urllib.request.urlopen(req,timeout=60) as response: result=json.load(response)
    item['asset']=result.get('asset',result); item['assets_library_registered']=True
    temp=path.with_suffix('.tmp'); temp.write_text(json.dumps(data,indent=2)+'\n'); temp.replace(path)
    print(json.dumps({'file':name,'registered':True,'asset':item['asset']}),flush=True)
