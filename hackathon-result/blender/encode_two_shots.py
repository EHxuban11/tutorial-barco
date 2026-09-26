from pathlib import Path
import imageio.v2 as iio
from PIL import Image,ImageDraw
import sys
root=Path(__file__).resolve().parent
stages=[97,166,213,240,263,277,296,312]
sheet=Image.new('RGB',(1280,760),'#111820');d=ImageDraw.Draw(sheet)
for k,f in enumerate(stages):
    im=Image.open(root/'preview-second'/f'{f:04d}.png');im.thumbnail((420,236))
    x=k%3*426;y=k//3*253;sheet.paste(im,(x,y));d.text((x+8,y+236),f'Shot 2 / {(f-97)/24:.2f}s',fill='white')
sheet.save(root/'renders/second-pan-contact.jpg')
if '--test' not in sys.argv:
    first=[root/'preview-flyby'/f'{f:04d}.png' for f in range(1,97)]
    second=[root/'preview-second'/f'{f:04d}.png' for f in range(97,313)]
    assert all(p.exists() for p in first+second)
    with iio.get_writer(root/'ELKANO-two-shots.mp4',fps=24,codec='libx264',quality=8,macro_block_size=2,ffmpeg_params=['-movflags','+faststart','-g','1']) as w:
        for p in first+second:w.append_data(iio.imread(p))
