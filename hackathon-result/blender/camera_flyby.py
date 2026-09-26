"""Camera-only revision inspired by the supplied 54–58s reference clip."""
import bpy, math, json
from pathlib import Path
from mathutils import Vector
root=Path(__file__).resolve().parent
s=bpy.context.scene
original_objects={o.name: (tuple(o.location),tuple(o.rotation_euler),tuple(o.scale),o.data.as_pointer() if o.data else None) for o in s.objects}
data=bpy.data.cameras.new('Flyby • perspective lens')
cam=bpy.data.objects.new('Camera | aerial approach and quarter sweep',data)
s.collection.objects.link(cam);s.camera=cam
data.type='PERSP';data.lens=45;data.sensor_width=36;data.clip_end=300
# An accelerating aerial approach: overhead stern view into a close three-quarter.
# The path is sampled per frame so arbitrary scroll seeking remains deterministic.
for f in range(1,97):
    t=(f-1)/95
    az=math.radians(-166+108*t**2.05)
    radius=30*(1-t)**1.45+14*t
    height=61*(1-t)**1.65+11*t
    cam.location=(radius*math.cos(az),radius*math.sin(az),height)
    target=Vector((-.2,0,1.6+1.8*t))
    cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler()
    data.shift_x=-.23*(1-t)**1.4
    data.shift_y=-.13*(1-t)**1.4
    data.lens=45-10*t*t
    cam.keyframe_insert('location',frame=f)
    cam.keyframe_insert('rotation_euler',frame=f)
    data.keyframe_insert('shift_x',frame=f);data.keyframe_insert('shift_y',frame=f)
    data.keyframe_insert('lens',frame=f)
s.frame_start=1;s.frame_end=96;s.render.fps=24
s.render.resolution_x=1920;s.render.resolution_y=1080;s.render.resolution_percentage=100
s.cycles.samples=128
s['camera_reference']='Local video/clip_0m54s-0m58s.mp4: aerial approach, descending camera, accelerating quarter sweep. Camera interpretation; boat and ocean unmodified.'
for f,label in [(1,'01 • High and distant'),(32,'02 • Aerial approach'),(64,'03 • Descend'),(96,'04 • Quarter sweep')]:
    s.timeline_markers.new(label,frame=f)
for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type=='VIEW_3D':
            area.spaces.active.region_3d.view_perspective='CAMERA'
            area.spaces.active.shading.type='MATERIAL'
            area.spaces.active.overlay.show_overlays=False
assert all((tuple(s.objects[n].location),tuple(s.objects[n].rotation_euler),tuple(s.objects[n].scale),s.objects[n].data.as_pointer() if s.objects[n].data else None)==state for n,state in original_objects.items()), 'Unexpected edit to existing objects'
s.frame_set(96)
s.render.filepath=str(root/'renders/elkano-flyby.png')
bpy.ops.wm.save_as_mainfile(filepath=str(root/'ELKANO-camera-flyby.blend'))
bpy.ops.render.render(write_still=True)
s.render.resolution_x=800;s.render.resolution_y=450;s.cycles.samples=8
out=root/'preview-flyby';out.mkdir(exist_ok=True)
for f in range(1,97):
    s.frame_set(f);s.render.filepath=str(out/f'{f:04d}.png');bpy.ops.render.render(write_still=True)
