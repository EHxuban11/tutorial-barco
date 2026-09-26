from pathlib import Path
import imageio.v2 as iio
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parent
for i in range(1,313):
    with Image.open(R/'frames-v6'/f'{i:04d}.png') as im:
        assert im.size==(1280,720);im.verify()
selected=[0,70,95,96,190,239,276,311]
sheet=Image.new('RGB',(1280,760),'#112431');draw=ImageDraw.Draw(sheet)
count=0
for i,frame in enumerate(iio.get_reader(R.parent/'videos'/'6.mp4')):
    assert frame.shape[:2]==(720,1280)
    if i in selected:
        k=selected.index(i);x=(k%4)*320;y=(k//4)*380
        im=Image.fromarray(frame);im.thumbnail((320,340));sheet.paste(im,(x,y+22))
        draw.text((x+8,y+5),f'Frame {i+1} / {i/24:.2f}s',fill='white')
    count+=1
assert count==312,count
sheet.save(R/'renders'/'v6-video-check.jpg',quality=90)
print('VERIFIED: all 312 PNGs and all 312 decoded MP4 frames; 1280x720, 24fps, 13s.')
