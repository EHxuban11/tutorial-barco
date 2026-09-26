"""Portable reference packaging; no uploads or model calls.

uv run --with imageio-ffmpeg python scripts/prepare_boat_reference.py --help
"""
import argparse,json,subprocess
from pathlib import Path
import imageio_ffmpeg

p=argparse.ArgumentParser(description=__doc__)
sub=p.add_subparsers(dest='kind',required=True)
h=sub.add_parser('hero');h.add_argument('--frames',required=True);h.add_argument('--count',type=int,default=288)
n=sub.add_parser('night');n.add_argument('--image',required=True);n.add_argument('--seconds',type=float,default=4)
s=sub.add_parser('style');s.add_argument('--video',required=True);s.add_argument('--start',type=float,default=5);s.add_argument('--seconds',type=float,default=3)
for parser in [h,n,s]:parser.add_argument('--output',required=True)
a=p.parse_args();output=Path(a.output).resolve()
if output.exists():p.error('Output already exists; choose a fresh name')
ff=imageio_ffmpeg.get_ffmpeg_exe();args=[ff,'-v','error']
if a.kind=='hero':
    folder=Path(a.frames).resolve()
    if a.count<1 or any(not (folder/f'{i:06d}.png').is_file() for i in range(1,a.count+1)):p.error('Expected a complete sequence numbered 000001.png onward')
    args+=['-framerate','24','-i',str(folder/'%06d.png'),'-frames:v',str(a.count)];seconds=a.count/24
elif a.kind=='night':
    if a.seconds<=0 or not Path(a.image).is_file():p.error('A valid still and positive duration are required')
    args+=['-loop','1','-i',a.image,'-t',str(a.seconds)];seconds=a.seconds
else:
    reader=imageio_ffmpeg.read_frames(a.video);meta=next(reader);reader.close()
    if a.start<0 or a.seconds<=0 or a.start+a.seconds>meta['duration']+.02:p.error('Requested excerpt exceeds the source video')
    args+=['-ss',str(a.start),'-i',a.video,'-t',str(a.seconds)];seconds=a.seconds
output.parent.mkdir(parents=True,exist_ok=True)
args+=['-vf','scale=1280:720:flags=lanczos','-r','24','-c:v','libx264','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart','-an',str(output)]
subprocess.run(args,check=True);subprocess.run([ff,'-v','error','-i',str(output),'-f','null','-'],check=True)
reader=imageio_ffmpeg.read_frames(str(output));meta=next(reader);reader.close()
assert abs(meta['duration']-seconds)<.1 and meta['fps']==24 and meta['size']==(1280,720),meta
report={'kind':a.kind,'duration':meta['duration'],'fps':meta['fps'],'size':meta['size'],'held_still':a.kind=='night','decoded':True,'file':str(output)}
output.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
