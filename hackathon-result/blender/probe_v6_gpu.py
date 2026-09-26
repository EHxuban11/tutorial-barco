"""Test local Metal rendering independently of the production CPU job."""
import bpy
from pathlib import Path
R=Path(__file__).resolve().parent;s=bpy.context.scene
prefs=bpy.context.preferences.addons['cycles'].preferences
prefs.compute_device_type='METAL';prefs.get_devices()
for d in prefs.devices:d.use=d.type=='METAL'
s.cycles.device='GPU';s.cycles.samples=24;s.cycles.adaptive_threshold=.08
s.render.resolution_x=1280;s.render.resolution_y=720;s.frame_set(96)
s.render.filepath=str(R/'renders'/'v6-metal-probe.png')
bpy.ops.render.render(write_still=True)
print('GPU PROBE OK',flush=True)
