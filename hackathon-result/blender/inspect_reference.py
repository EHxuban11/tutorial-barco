from pathlib import Path
import imageio.v2 as iio
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parent
r=iio.get_reader(root.parent/'video/clip_0m54s-0m58s.mp4')
m=r.get_meta_data();print(m)
sheet=Image.new('RGB',(1280,810),'#141414')
d=ImageDraw.Draw(sheet)
for k,t in enumerate([0,.45,.9,1.35,1.8,2.25,2.7,3.15,3.6]):
    im=Image.fromarray(r.get_data(round(t*m['fps'])));im.thumbnail((420,236))
    x=(k%3)*426;y=(k//3)*270;sheet.paste(im,(x,y));d.text((x+8,y+241),f'{54+t:.2f}s',fill='white')
sheet.save(root/'renders/reference-camera-sheet.jpg')
