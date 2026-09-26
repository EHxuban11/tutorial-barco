"""Render the saved V6 scene, resume safely, then make a full-HD hero still."""
import bpy, sys
from pathlib import Path
R=Path(__file__).resolve().parent;s=bpy.context.scene
s.render.use_persistent_data=True;s.cycles.device='CPU'
if '--gpu' in sys.argv:
    prefs=bpy.context.preferences.addons['cycles'].preferences
    prefs.compute_device_type='METAL';prefs.get_devices()
    for d in prefs.devices:d.use=d.type=='METAL'
    s.cycles.device='GPU'
s.render.resolution_x=1280;s.render.resolution_y=720;s.cycles.samples=24
s.cycles.adaptive_threshold=.08
out=R/'frames-v6';out.mkdir(exist_ok=True)
for f in range(1,313):
    path=out/f'{f:04d}.png'
    if path.exists():continue
    s.frame_set(f);s.render.filepath=str(path);bpy.ops.render.render(write_still=True)
    print(f'V6 PROGRESS {f}/312',flush=True)
s.frame_set(96);s.render.resolution_x=1920;s.render.resolution_y=1080;s.cycles.samples=96;s.cycles.adaptive_threshold=.025
s.render.filepath=str(R/'renders'/'elkano-v6-hero.png');bpy.ops.render.render(write_still=True)
print('V6 ALL FRAMES AND HERO COMPLETE',flush=True)
