"""Append a second camera shot; preserve ocean/model/materials/lighting."""
import bpy, math
from pathlib import Path
from mathutils import Vector
root=Path(__file__).resolve().parent;s=bpy.context.scene
first=s.camera
# Continue the existing boat/cloth motion for the longer edit. Ocean untouched.
ship=bpy.data.objects['ELKANO | animated ship']
cloth=[o.data.shape_keys for o in s.objects if o.type=='MESH' and o.parent==ship and o.data.shape_keys]
motion=[]
for f in range(1,145):
    s.frame_set(f)
    motion.append((tuple(ship.location),tuple(ship.rotation_euler),[[k.value for k in keys.key_blocks[1:]] for keys in cloth]))
for f in range(145,313):
    loc,rot,values=motion[(f-1)%144]
    ship.location=loc;ship.rotation_euler=rot;ship.keyframe_insert('location',frame=f);ship.keyframe_insert('rotation_euler',frame=f)
    for keys,vals in zip(cloth,values):
        for key,value in zip(keys.key_blocks[1:],vals):key.value=value;key.keyframe_insert('value',frame=f)
data=bpy.data.cameras.new('Shot 02 • descending pass and bow reveal');data.type='PERSP';data.sensor_width=36;data.clip_end=300
cam=bpy.data.objects.new('Camera | BON VOYAGE inspired pass',data);s.collection.objects.link(cam)
# time, camera xyz, aim xyz, lens. Close passage is intentional at ~6.8 seconds.
knots=[(0,(-27,-5,48),(0,0,1.8),45),(.32,(-22,-6,35),(0,0,2.1),45),(.54,(-14,-10,21),(0,0,2.6),43),(.67,(-5,-11,11),(0,0,3.3),40),(.77,(4,-7,5.5),(0,0,3.6),38),(.84,(9,-3,3.1),(0,0,3.7),36),(.93,(16,-.7,2.6),(0,0,3.5),37),(1,(20,0,2.4),(0,0,3.5),40)]
def sample(t,field):
    i=next((i for i in range(len(knots)-1) if knots[i+1][0]>=t),len(knots)-2)
    a,b=knots[i],knots[i+1];u=(t-a[0])/(b[0]-a[0]);dt=b[0]-a[0]
    def v(k):return Vector(knots[k][field]) if field!=3 else knots[k][field]
    p,q=v(i),v(i+1)
    lo=max(0,i-1);hi=min(len(knots)-1,i+2)
    m0=(q-v(lo))/(knots[i+1][0]-knots[lo][0])*dt
    m1=(v(hi)-p)/(knots[hi][0]-knots[i][0])*dt
    return (2*u**3-3*u*u+1)*p+(u**3-2*u*u+u)*m0+(-2*u**3+3*u*u)*q+(u**3-u*u)*m1
for local in range(1,217):
    t=(local-1)/215;f=96+local
    cam.location=sample(t,1);aim=sample(t,2)
    cam.rotation_euler=(aim-cam.location).to_track_quat('-Z','Y').to_euler();data.lens=sample(t,3)
    cam.keyframe_insert('location',frame=f);cam.keyframe_insert('rotation_euler',frame=f);data.keyframe_insert('lens',frame=f)
for marker in list(s.timeline_markers):s.timeline_markers.remove(marker)
m=s.timeline_markers.new('SHOT 01 • aerial flyby',frame=1);m.camera=first
m=s.timeline_markers.new('CUT • SHOT 02 • descending pass',frame=97);m.camera=cam
s.frame_start=1;s.frame_end=312;s.render.fps=24
s['edit_notes']='13 seconds: shot 1 frames 1–96; hard cut at 97; shot 2 frames 97–312. Second camera inspired by local clip_0m18s-0m27s.mp4. Original ocean, geometry, materials and lighting unchanged. Boat/cloth motion repeated to cover the edit.'
s.frame_set(240);s.camera=cam
s.render.resolution_x=1920;s.render.resolution_y=1080;s.cycles.samples=128
s.render.filepath=str(root/'final-two-shots'/'frame_')
bpy.ops.wm.save_as_mainfile(filepath=str(root/'ELKANO-two-shots.blend'))
s.render.resolution_x=800;s.render.resolution_y=450;s.cycles.samples=8
out=root/'preview-second';out.mkdir(exist_ok=True)
import sys
test='--test' in sys.argv
frames=[97,166,213,240,263,277,296,312] if test else range(97,313)
for f in frames:
    path=out/f'{f:04d}.png'
    if path.exists():continue
    s.frame_set(f);s.camera=cam;s.render.filepath=str(path);bpy.ops.render.render(write_still=True)
