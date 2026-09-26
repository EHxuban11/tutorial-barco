"""Native full-HD stills from the approved blocking scene files."""
import bpy
from pathlib import Path
R=Path(__file__).resolve().parent
out=R/'storyboard-stills-v2';out.mkdir(exist_ok=True)
for n,name,frames in [(2,'isla',[(144,'isla')]),(3,'estrellas',[(1,'estrellas')]),
    (4,'cofre',[(1,'cofre-cerrado'),(2,'cofre-abierto')]),(5,'puerto',[(1,'puerto')]),(6,'cierre',[(192,'cierre')])]:
    bpy.ops.wm.open_mainfile(filepath=str(R/f'ELKANO-scene{n:02d}-{name}.blend'))
    s=bpy.context.scene
    prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='METAL';prefs.get_devices()
    for d in prefs.devices:d.use=d.type=='METAL'
    s.cycles.device='GPU';s.cycles.samples=64 if n==3 else 16
    s.render.resolution_x=1920;s.render.resolution_y=1080
    s.render.image_settings.file_format='JPEG';s.render.image_settings.quality=90
    for f,label in frames:
        p=out/f'{label}.jpg'
        if p.exists():continue
        s.frame_set(f);s.render.filepath=str(p);bpy.ops.render.render(write_still=True)
        print('STILL',label,flush=True)
