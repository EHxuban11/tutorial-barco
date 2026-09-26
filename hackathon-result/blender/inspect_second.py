from pathlib import Path
import imageio.v2 as iio
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent
r=iio.get_reader(root.parent/'video/clip_0m18s-0m27s.mp4');m=r.get_meta_data();print(m)
sheet=Image.new('RGB',(1280,1080),'#111820');d=ImageDraw.Draw(sheet)
for k,t in enumerate([0,.8,1.6,2.4,3.2,4,4.8,5.6,6.4,7.2,8,8.8]):
    im=Image.fromarray(r.get_data(round(t*m['fps'])));im.thumbnail((420,236))
    x=k%3*426;y=k//3*270;sheet.paste(im,(x,y));d.text((x+8,y+241),f'{18+t:.2f}s',fill='white')
sheet.save(root/'renders/reference-second-sheet.jpg')
