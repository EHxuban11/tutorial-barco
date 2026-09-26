from pathlib import Path
import imageio.v2 as iio
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent
frames=sorted((root/'preview-flyby').glob('*.png'))
assert len(frames)==96
with iio.get_writer(root/'ELKANO-camera-flyby.mp4',fps=24,codec='libx264',quality=8,macro_block_size=2,ffmpeg_params=['-movflags','+faststart','-g','1']) as w:
    for f in frames:w.append_data(iio.imread(f))
sheet=Image.new('RGB',(1200,720),'#111820');d=ImageDraw.Draw(sheet)
for k,n in enumerate([1,20,39,58,77,96]):
    im=Image.open(root/'preview-flyby'/f'{n:04d}.png');im.thumbnail((600,337))
    x=k%2*600;y=k//2*240
    im.thumbnail((400,225));sheet.paste(im,(x+100,y));d.text((x+10,y+10),f'{(n-1)/24:.2f}s',fill='white')
sheet.save(root/'renders/elkano-flyby-contact.jpg')
