"""Scene 01 preview. Load V6; never overwrite the source scene."""
import bpy, math, sys
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parent
s = bpy.context.scene
ship = bpy.data.objects['ELKANO | animated ship']
ship.animation_data_clear()
for marker in list(s.timeline_markers):
    s.timeline_markers.remove(marker)
data = bpy.data.cameras.new('Zarpar | 40mm lateral')
cam = bpy.data.objects.new('Zarpar | camera', data)
s.collection.objects.link(cam)
data.lens = 45
data.clip_end = 30000
data.dof.use_dof = False
s.camera = cam
s.frame_start = 1
s.frame_end = 288
s.render.fps = 24

# A continuous, almost fixed lateral shot. Bow points right, cards live right.
for frame in range(1, 289):
    t = (frame - 1) / 287
    ship.location = (-11 + 12*t, 0, .045*math.sin(t*math.pi*6))
    ship.rotation_euler = (.012*math.sin(t*math.pi*5), .012*math.cos(t*math.pi*6), 0)
    ship.keyframe_insert('location', frame=frame)
    ship.keyframe_insert('rotation_euler', frame=frame)
    cam.location = (12 + 2*t, -29, 7.5)
    aim = Vector((2 + 2*t, 0, 4.2))
    cam.rotation_euler = (aim-cam.location).to_track_quat('-Z', 'Y').to_euler()
    cam.keyframe_insert('location', frame=frame)
    cam.keyframe_insert('rotation_euler', frame=frame)

# The existing wake was expressed in world coordinates. Attach its coordinate
# origin to the moving hull so it never remains stranded at the old position.
water = bpy.data.materials['V6 | cobalt turquoise ocean']
nodes = water.node_tree.nodes
links = water.node_tree.links
coord = nodes.new('ShaderNodeTexCoord')
coord.object = ship
coord.label = 'Wake follows the ship'
for node in nodes:
    if node.type == 'SEPXYZ':
        links.new(coord.outputs['Object'], node.inputs[0])
sea = bpy.data.objects['V6 | open ocean']
ocean = sea.modifiers.get('Wind driven ocean spectrum')
ocean.wave_scale = .65
ocean.choppiness = .65
ocean.spatial_size = 200

s.render.engine = 'CYCLES'
s.cycles.samples = 8
s.cycles.use_denoising = True
s.cycles.adaptive_threshold = .12
s.cycles.max_bounces = 4
s.render.use_persistent_data = True
s.render.resolution_x = 800
s.render.resolution_y = 450
s.render.resolution_percentage = 100
s.render.image_settings.file_format = 'PNG'
s['scene01_notes'] = '12s / 24fps. Blender blocking preview 800x450. Continuous lateral shot. Right side reserved for web cards. Original V6 untouched.'
s.frame_set(144)
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'ELKANO-scene01-zarpar.blend'))

prefs = bpy.context.preferences.addons['cycles'].preferences
prefs.compute_device_type = 'METAL'
prefs.get_devices()
for device in prefs.devices:
    device.use = device.type == 'METAL'
s.cycles.device = 'GPU'
out = ROOT/'scene01-frames-v2'
out.mkdir(exist_ok=True)
frames = [1, 144, 288] if '--test' in sys.argv else range(1, 289)
for frame in frames:
    path = out/f'{frame:04d}.png'
    if path.exists():
        continue
    s.frame_set(frame)
    s.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    print(f'ZARPAR {frame}/288', flush=True)
