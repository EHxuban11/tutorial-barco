"""Blender --background scene.blend --python render_frames.py -- --output renders --frames 1,72,144"""
import argparse
import json
import sys
from pathlib import Path
import bpy

p=argparse.ArgumentParser(description='Render frames of the loaded Blender scene without saving over it.')
p.add_argument('--output',required=True)
p.add_argument('--frames',help='Comma-separated still frames; otherwise render the full interval.')
p.add_argument('--start',type=int)
p.add_argument('--end',type=int)
p.add_argument('--step',type=int,default=1)
p.add_argument('--camera')
p.add_argument('--width',type=int,default=960)
p.add_argument('--height',type=int,default=540)
p.add_argument('--samples',type=int,default=12)
a=p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
scene=bpy.context.scene
if a.camera:
    cam=bpy.data.objects.get(a.camera)
    if not cam or cam.type!='CAMERA': p.error('Named camera not found')
    scene.camera=cam
if scene.camera is None: p.error('Scene has no active camera')
if min(a.width,a.height,a.samples,a.step)<=0: p.error('Dimensions, samples and step must be positive')
frames=[int(f) for f in a.frames.split(',')] if a.frames else list(range(a.start if a.start is not None else scene.frame_start,(a.end if a.end is not None else scene.frame_end)+1,a.step))
if not frames: p.error('No frames selected')
out=Path(a.output).expanduser().resolve(); out.mkdir(parents=True,exist_ok=True)
scene.render.engine='CYCLES'; scene.cycles.samples=a.samples; scene.cycles.use_denoising=True
prefs=bpy.context.preferences.addons['cycles'].preferences
backend=None
for candidate in ('METAL','OPTIX','CUDA','HIP','ONEAPI'):
    try:
        prefs.compute_device_type=candidate; prefs.get_devices()
        if any(d.type==candidate for d in prefs.devices):
            for d in prefs.devices: d.use=d.type==candidate
            backend=candidate; break
    except (TypeError,RuntimeError): pass
scene.cycles.device='GPU' if backend else 'CPU'
scene.render.resolution_x=a.width; scene.render.resolution_y=a.height
scene.render.resolution_percentage=100; scene.render.image_settings.file_format='PNG'
manifest={'blender':bpy.app.version_string,'source':bpy.data.filepath,'camera':scene.camera.name,'fps':scene.render.fps/scene.render.fps_base,'resolution':[a.width,a.height],'samples':a.samples,'device':backend or 'CPU','requested_frames':frames,'completed_frames':[]}
for f in frames:
    scene.frame_set(f); scene.render.filepath=str(out/f'{f:06d}.png')
    bpy.ops.render.render(write_still=True)
    manifest['completed_frames'].append(f)
    (out/'render-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Render complete:',len(frames),'frames in',out)
