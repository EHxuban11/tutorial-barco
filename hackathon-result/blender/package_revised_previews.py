"""Package local Blender previews, never call a paid generation service."""
from pathlib import Path
import subprocess
import imageio_ffmpeg
import imageio.v2 as iio

root=Path(__file__).resolve().parent
ff=imageio_ffmpeg.get_ffmpeg_exe()
for name,number,count in [('cofre',20,192),('ciudad',21,144)]:
    frames=root/f'revised-{name}-frames-v3'
    assert all((frames/f'{n:04d}.png').is_file() for n in range(1,count+1))
    target=root.parent/'videos'/f'{number}.mp4'
    if not target.exists():
        subprocess.run([ff,'-v','error','-framerate','24','-i',str(frames/'%04d.png'),
            '-c:v','libx264','-preset','slow','-crf','20','-pix_fmt','yuv420p',
            '-movflags','+faststart','-an',str(target)],check=True)
    reader=iio.get_reader(target)
    meta=reader.get_meta_data()
    assert sum(1 for _ in reader)==count
    assert meta['size']==(800,450) and meta['fps']==24
    print(name,target,meta['duration'],'seconds, verified',flush=True)
