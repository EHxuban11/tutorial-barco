"""Package all six scene assets and a silent review montage; no AI calls."""
from pathlib import Path
import shutil, subprocess, json
import imageio.v2 as iio
import imageio_ffmpeg
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parent
web=R.parent/'Elkano_Embat/apps/web/public/video'
videos=R.parent/'videos'
ff=imageio_ffmpeg.get_ffmpeg_exe()
for n,name,count,index in [(2,'isla',144,10),(6,'cierre',192,11)]:
    folder=R/f'scene{n:02d}-frames-v3'
    assert all((folder/f'{f:04d}.png').exists() for f in range(1,count+1))
    target=web/f'{name}-blender.mp4'
    assert not target.exists(),target
    subprocess.run([ff,'-v','error','-framerate','24','-i',str(folder/'%04d.png'),
        '-c:v','libx264','-preset','slow','-crf','23','-pix_fmt','yuv420p','-g','12',
        '-movflags','+faststart','-an',str(target)],check=True)
    reader=iio.get_reader(target);meta=reader.get_meta_data()
    assert sum(1 for _ in reader)==count
    assert meta['size']==(800,450) and meta['fps']==24
    assert target.stat().st_size<8_000_000
    for dest in [web/f'{name}.mp4',videos/f'{index}.mp4']:
        assert not dest.exists(),dest
        shutil.copy2(target,dest)
    print(name,meta,flush=True)

stills=['isla','estrellas','cofre-cerrado','cofre-abierto','puerto','cierre']
for name in stills:
    source=R/'storyboard-stills-v2'/f'{name}.jpg'
    with Image.open(source) as im:assert im.size==(1920,1080);im.verify()
    for suffix in ['', '-blender']:
        target=web/f'{name}{suffix}.jpg';assert not target.exists(),target
        shutil.copy2(source,target)

# Contact sheet: it is for review, never burned into scene assets.
sheet=Image.new('RGB',(1280,1152),'#061421');draw=ImageDraw.Draw(sheet)
items=[('1. ZARPAR',R/'scene01-frames-v2/0288.png'),
       ('2. LA ISLA',web/'isla.jpg'),('3. LAS ESTRELLAS',web/'estrellas.jpg'),
       ('4. EL COFRE',web/'cofre-abierto.jpg'),('5. EL PUERTO',web/'puerto.jpg'),('6. CIERRE',web/'cierre.jpg')]
for j,(label,p) in enumerate(items):
    x=(j%2)*640;y=(j//2)*384
    with Image.open(p) as im:sheet.paste(im.resize((640,360)),(x,y+24))
    draw.text((x+12,y+6),label+' / MAQUETA BLENDER',fill='#e9d6ab')
sheet.save(R/'renders/storyboard-six-scenes.jpg',quality=92)

montage=videos/'12.mp4';assert not montage.exists()
with iio.get_writer(montage,fps=24,codec='libx264',macro_block_size=2,
    ffmpeg_params=['-crf','23','-pix_fmt','yuv420p','-movflags','+faststart']) as writer:
    for kind,name,duration in [('video','barco-largo',12),('video','isla',6),
        ('image','estrellas',4),('image','cofre-cerrado',3),('image','cofre-abierto',3),
        ('image','puerto',4),('video','cierre',8)]:
        if kind=='video':
            for frame in iio.get_reader(web/f'{name}.mp4'):writer.append_data(frame)
        else:
            import numpy as np
            with Image.open(web/f'{name}.jpg') as im:frame=np.asarray(im.resize((800,450)).convert('RGB'))
            for _ in range(duration*24):writer.append_data(frame)
reader=iio.get_reader(montage);assert sum(1 for _ in reader)==960
print('ALL SIX SCENES VERIFIED. REVIEW MONTAGE:',montage,reader.get_meta_data(),flush=True)
