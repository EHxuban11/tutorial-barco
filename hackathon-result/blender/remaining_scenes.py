"""Build the remaining five storyboard scenes from the unchanged V6 ship."""
import bpy, math, random, sys
from pathlib import Path
from mathutils import Vector

R = Path(__file__).resolve().parent
args = sys.argv[sys.argv.index('--')+1:]
number = int(args[0])
test = '--test' in args
random.seed(47)
bpy.ops.wm.open_mainfile(filepath=str(R/'ELKANO-v6-ocean.blend'))
s = bpy.context.scene
ship = bpy.data.objects['ELKANO | animated ship']
ship.animation_data_clear()
ship.location = (0,0,0)
ship.rotation_euler = (0,0,0)
for marker in list(s.timeline_markers): s.timeline_markers.remove(marker)
for ob in list(s.objects):
    if ob.type == 'LIGHT': bpy.data.objects.remove(ob, do_unlink=True)

def mat(name, color, emission=0):
    m = bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF'); p.inputs['Base Color'].default_value=(*color,1)
    p.inputs['Roughness'].default_value=.7
    if emission:
        p.inputs['Emission Color'].default_value=(*color,1);p.inputs['Emission Strength'].default_value=emission
    return m

def cube(name, loc, size, material, bevel=.03, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    ob=bpy.context.object;ob.name=name;ob.dimensions=size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    ob.data.materials.append(material)
    if bevel:
        mod=ob.modifiers.new('Soft crafted edges','BEVEL');mod.width=bevel;mod.segments=2
    if parent: ob.parent=parent
    return ob

def sphere(name, loc, scale, material):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=loc)
    ob=bpy.context.object;ob.name=name;ob.scale=scale;ob.data.materials.append(material)
    for p in ob.data.polygons:p.use_smooth=True
    return ob

def light(name, kind, loc, energy, color, size=5):
    bpy.ops.object.light_add(type=kind, location=loc);ob=bpy.context.object;ob.name=name
    ob.data.energy=energy;ob.data.color=color
    if kind=='AREA':ob.data.shape='DISK';ob.data.size=size
    ob.rotation_euler=(Vector((0,0,2))-ob.location).to_track_quat('-Z','Y').to_euler()
    return ob

world=bpy.data.worlds.new(f'Scene {number} atmosphere');world.use_nodes=True;s.world=world
bg=world.node_tree.nodes.get('Background');bg.inputs[0].default_value=(.38,.55,.7,1);bg.inputs[1].default_value=.5
sun=light('Story sunlight','SUN',(8,-8,15),2,(1,.88,.70));sun.data.angle=.12
light('Soft sky fill','AREA',(1,-8,12),450,(.65,.8,1),10)
sea=bpy.data.objects['V6 | open ocean'];ocean=sea.modifiers.get('Wind driven ocean spectrum')
ocean.wave_scale=.5;ocean.choppiness=.5;ocean.spatial_size=200
water=bpy.data.materials['V6 | cobalt turquoise ocean']
coord=water.node_tree.nodes.new('ShaderNodeTexCoord');coord.object=ship
for node in water.node_tree.nodes:
    if node.type=='SEPXYZ':water.node_tree.links.new(coord.outputs['Object'],node.inputs[0])

data=bpy.data.cameras.new(f'Scene {number} camera');data.clip_end=30000
cam=bpy.data.objects.new(f'Scene {number} camera',data);s.collection.objects.link(cam);s.camera=cam
def camera(loc, aim, lens=40):
    cam.location=loc;cam.rotation_euler=(Vector(aim)-cam.location).to_track_quat('-Z','Y').to_euler();data.lens=lens

wood=mat('Story warm oak',(.20,.085,.032))
metal=mat('Story dark iron',(.035,.04,.045))
stone=mat('Story warm limestone',(.49,.41,.29))
green=mat('Story island vegetation',(.10,.22,.11))
sand=mat('Story pale sand',(.64,.53,.32))
roof=mat('Story terracotta',(.32,.085,.035))
names={2:'isla',3:'estrellas',4:'cofre',5:'puerto',6:'cierre'}
name=names[number]
length={2:144,3:1,4:2,5:1,6:192}[number]

if number==2:
    sphere('Island sandy shelf',(9,22,-.9),(13,8,1.6),sand)
    sphere('Island green ridge',(11,25,.4),(9,6,3.7),green)
    sphere('Island rocky headland',(4,24,.6),(4,4,3),stone)
    for i in range(19):
        x=random.uniform(5,17);y=random.uniform(23,27);z=2.3
        cube('Distant tree trunk',(x,y,z+.6),(.16,.16,1.3),wood)
        sphere('Distant tree crown',(x,y,z+1.4),(.7,.65,.9),green)
    camera((17,-30,10),(3,8,3),40)
    for f in range(1,length+1):
        t=(f-1)/(length-1);ease=1-(1-t)**3
        ship.location=(-6+7*ease,2*ease,.035*math.sin(t*math.pi*4))
        ship.keyframe_insert('location',frame=f)
        sun.data.color=(1,.88-.25*t,.70-.34*t);sun.data.keyframe_insert('color',frame=f)
        sun.data.energy=2-.8*t;sun.data.keyframe_insert('energy',frame=f)
        bg.inputs[0].default_value=(.38+.08*t,.55-.22*t,.70-.4*t,1);bg.inputs[0].keyframe_insert('default_value',frame=f)

elif number==3:
    # Real celestial background, intentionally clear for the web constellation.
    bg.inputs[0].default_value=(.004,.009,.03,1);bg.inputs[1].default_value=.35
    n=world.node_tree.nodes;l=world.node_tree.links
    tc=n.new('ShaderNodeTexCoord');v=n.new('ShaderNodeTexVoronoi');v.inputs['Scale'].default_value=40
    l.new(tc.outputs['Normal'],v.inputs['Vector'])
    r=n.new('ShaderNodeValToRGB');r.color_ramp.elements[0].position=.04;r.color_ramp.elements[0].color=(5,5.5,6,1)
    r.color_ramp.elements[1].position=.065;r.color_ramp.elements[1].color=(.018,.035,.085,1)
    l.new(v.outputs['Distance'],r.inputs[0]);l.new(r.outputs[0],bg.inputs[0])
    sun.data.energy=.08;sun.data.color=(.35,.5,1)
    light('Moonlit canvas','AREA',(5,-6,11),450,(.35,.5,1),8)
    camera((3,-4,2.1),(3,1,7.5),20)

elif number==4:
    # A real hinged chest on the deck; both images use exactly the same camera.
    bg.inputs[0].default_value=(.018,.029,.07,1);bg.inputs[1].default_value=.2;sun.data.energy=.12
    chest=cube('Chest oak body',(-.2,-.35,1.85),(1.65,.95,.72),wood,.04)
    for x in [-.84,.44]:cube('Chest iron strap',(x,-.35,1.85),(.09,.98,.75),metal,.015)
    cube('Chest latch',(-.2,-.845,1.97),(.13,.04,.22),metal,.01)
    hinge=bpy.data.objects.new('Chest lid hinge',None);s.collection.objects.link(hinge);hinge.location=(-.2,.125,2.22)
    lid=cube('Chest wooden lid',(0,-.475,.075),(1.72,1.02,.15),wood,.05,hinge)
    for x in [-.64,.64]:cube('Lid iron strap',(x,-.475,.16),(.09,1.04,.055),metal,.01,hinge)
    hinge.rotation_euler.x=0;hinge.keyframe_insert('rotation_euler',frame=1)
    hinge.rotation_euler.x=math.radians(-105);hinge.keyframe_insert('rotation_euler',frame=2)
    gold=mat('Treasure warm glow',(.9,.44,.07),2)
    cube('Treasure inside',(-.2,-.35,2.20),(1.38,.73,.03),gold,.02)
    glow=light('Treasure light','POINT',(-.2,-.3,2.35),0,(1,.48,.12));glow.data.shadow_soft_size=.3
    glow.data.keyframe_insert('energy',frame=1);glow.data.energy=20;glow.data.keyframe_insert('energy',frame=2)
    cube('Lantern base',(-1.4,.1,1.65),(.3,.3,.08),metal)
    sphere('Lantern amber glass',(-1.4,.1,1.95),(.12,.12,.25),gold)
    light('Lantern pool','POINT',(-1.4,.1,2.1),35,(1,.55,.2))
    light('Chest readable warm fill','AREA',(0,-3,5),140,(1,.7,.4),4)
    camera((3.1,-4.7,3.5),(.4,-.1,2.05),42)

elif number==5:
    ship.location=(-3,-3,0)
    cube('Harbour quay',(3,9,.35),(29,4,1),stone,.08)
    cube('Wooden arrival pier',(1,3,.65),(2,10,.25),wood)
    for x in [-.05,2.05]:
        for y in [-1,2,5,8]:cube('Pier pile',(x,y,.2),(.23,.23,2.4),wood)
    for i in range(10):
        x=-11+i*2.7;h=random.uniform(2.5,5)
        cube('Port merchant house',(x,13,h/2),(2.3,3,h),stone,.06)
        cube('Port tiled roof',(x,13,h+.13),(2.5,3.2,.3),roof,.05)
        for z in [1.2,2.4,3.6]:
            if z<h-.3:cube('Port window',(x,11.47,z),(.44,.035,.65),metal,.01)
    cube('Port watchtower',(-10,13,4),(2.5,3,8),stone)
    sun.data.color=(1,.64,.36);sun.data.energy=1.5
    bg.inputs[0].default_value=(.36,.43,.53,1)
    camera((16,-25,11),(2,4,2.8),40)

elif number==6:
    bg.inputs[0].default_value=(.46,.24,.14,1);bg.inputs[1].default_value=.65
    sun.data.color=(1,.48,.20);sun.data.energy=1.7
    sun.rotation_euler=(.9,-.5,-2)
    camera((-17,-25,7),(9,8,5),32)
    for f in range(1,length+1):
        t=(f-1)/(length-1)
        ship.location=(22*t,15*t,.04*math.sin(t*math.pi*5))
        ship.rotation_euler=(.01*math.sin(t*math.pi*4),.01*math.cos(t*math.pi*5),math.atan2(15,22))
        ship.keyframe_insert('location',frame=f);ship.keyframe_insert('rotation_euler',frame=f)

if number in [2,5,6]:
    sky=world.node_tree.nodes.new('ShaderNodeTexSky');sky.sky_type='MULTIPLE_SCATTERING'
    sky.sun_disc=False;sky.sun_rotation=2.2;sky.air_density=1;sky.aerosol_density=.25
    sky.sun_elevation={2:.6,5:.08,6:.012}[number]
    if number==2:
        sky.keyframe_insert('sun_elevation',frame=1);sky.sun_elevation=.018;sky.keyframe_insert('sun_elevation',frame=length)
    world.node_tree.links.new(sky.outputs[0],bg.inputs[0]);bg.inputs[1].default_value=.3
s.view_settings.exposure=.15
if number==6:s.view_settings.exposure=-.4
s.frame_start=1;s.frame_end=length;s.render.fps=24
s.render.engine='CYCLES';s.cycles.samples=8;s.cycles.use_denoising=True;s.cycles.max_bounces=4
if number==3:s.cycles.samples=64;s.cycles.use_denoising=False
s.render.use_persistent_data=True;s.cycles.adaptive_threshold=.12
s.render.resolution_x=800;s.render.resolution_y=450;s.render.resolution_percentage=100
s.render.image_settings.file_format='PNG'
s['storyboard']='Blender blocking preview, not final cinematic finish. Same V6 vessel and branding. Seedance not run.'
s.frame_set(length)
bpy.ops.wm.save_as_mainfile(filepath=str(R/f'ELKANO-scene{number:02d}-{name}.blend'))
prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='METAL';prefs.get_devices()
for d in prefs.devices:d.use=d.type=='METAL'
s.cycles.device='GPU'
out=R/(f'scene{number:02d}-frames-v3' if number in [2,3,6] else f'scene{number:02d}-frames-v2');out.mkdir(exist_ok=True)
frames=sorted(set([1,max(1,length//2),length])) if test else range(1,length+1)
for f in frames:
    target=out/f'{f:04d}.png'
    if target.exists():continue
    s.frame_set(f);s.render.filepath=str(target);bpy.ops.render.render(write_still=True)
    print(f'SCENE {number}: {f}/{length}',flush=True)
