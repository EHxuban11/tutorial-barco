"""uv run --with imageio-ffmpeg python prepare_media.py input.mp4 output.mp4"""
import argparse,math,subprocess
from pathlib import Path
import imageio_ffmpeg
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('output');p.add_argument('--crf',type=int,default=23)
a=p.parse_args();src=Path(a.source).resolve();dst=Path(a.output).resolve()
if src==dst:p.error('Output must be a separate copy')
if dst.exists():p.error('Output already exists; choose a new filename')
reader=imageio_ffmpeg.read_frames(str(src));meta=next(reader);reader.close()
fps=meta['fps'];gop=max(1,round(fps*.5))
dst.parent.mkdir(parents=True,exist_ok=True);ff=imageio_ffmpeg.get_ffmpeg_exe()
subprocess.run([ff,'-i',str(src),'-c:v','libx264','-preset','medium','-crf',str(a.crf),'-g',str(gop),'-keyint_min',str(gop),'-sc_threshold','0','-pix_fmt','yuv420p','-movflags','+faststart','-an',str(dst)],check=True)
subprocess.run([ff,'-v','error','-i',str(dst),'-f','null','-'],check=True)
print('Encoded and fully decoded:',dst)
