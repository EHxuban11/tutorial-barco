"""Encode and fully decode-check the 12-second blocking preview."""
from pathlib import Path
import shutil
import subprocess
import imageio.v2 as iio
import imageio_ffmpeg
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parent
frames = root/'scene01-frames-v2'
assert all((frames/f'{i:04d}.png').is_file() for i in range(1,289))
web = root.parent/'Elkano_Embat/apps/web/public/video'
preview = web/'barco-largo-blender.mp4'
assert not preview.exists(), 'Preview exists; do not overwrite silently'
subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-v', 'error', '-framerate', '24',
    '-i', str(frames/'%04d.png'), '-c:v', 'libx264', '-preset', 'slow', '-crf', '23',
    '-pix_fmt', 'yuv420p', '-g', '12', '-movflags', '+faststart', '-an', str(preview)], check=True)
reader = iio.get_reader(preview)
meta = reader.get_meta_data()
assert meta['size'] == (800,450)
assert meta['fps'] == 24
count = sum(1 for _ in reader)
assert count == 288, count
assert preview.stat().st_size < 8_000_000
live = web/'barco-largo.mp4'
assert not live.exists()
shutil.copy2(preview, live)
numbered = root.parent/'videos/9.mp4'
assert not numbered.exists()
shutil.copy2(preview, numbered)
sheet = Image.new('RGB', (1200, 730), '#071321')
draw = ImageDraw.Draw(sheet)
for j, f in enumerate([1,58,115,173,230,288]):
    x, y = j%2*600, j//2*243
    with Image.open(frames/f'{f:04d}.png') as im:
        im.thumbnail((400,225))
        sheet.paste(im, (x,y+18))
    draw.text((x+8,y+3), f'{(f-1)/24:.2f}s / 12s', fill='white')
    draw.text((x+410,y+65), 'ESPACIO PARA\nCAPAS WEB\n\nMAQUETA\nBLENDER', fill='#9fb4c7')
sheet.save(root/'renders/scene01-zarpar-check.jpg', quality=90)
print({'video':str(numbered),'frames':count,'size':meta['size'],'fps':meta['fps'],
    'duration':meta['duration'],'bytes':preview.stat().st_size})
