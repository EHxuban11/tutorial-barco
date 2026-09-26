"""Version 6: sunny adventure art direction, continuous timber hull and real ocean.
Load ELKANO-branded-sails.blend. Original scenes and renders are never modified.
"""
import bpy, math, random, sys
from pathlib import Path
from mathutils import Vector
from math import sin, cos, pi
R=Path(__file__).resolve().parent
s=bpy.context.scene
ship=bpy.data.objects['ELKANO | animated ship']
ship.scale=(1.13,.88,1)
random.seed(23)

def material(name,color,rough=.5,metal=0):
    m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1)
    p.inputs['Roughness'].default_value=rough;p.inputs['Metallic'].default_value=metal
    return m
def mesh(name,vs,fs,mat,parent=None):
    me=bpy.data.meshes.new(name);me.from_pydata(vs,[],fs);me.update()
    ob=bpy.data.objects.new(name,me);s.collection.objects.link(ob);me.materials.append(mat)
    ob.parent=parent
    for p in me.polygons:p.use_smooth=True
    return ob
def curve(name,points,radius,mat,parent=ship):
    cu=bpy.data.curves.new(name,'CURVE');cu.dimensions='3D';cu.bevel_depth=radius;cu.bevel_resolution=3
    sp=cu.splines.new('POLY');sp.points.add(len(points)-1)
    for p,co in zip(sp.points,points):p.co=(*co,1)
    ob=bpy.data.objects.new(name,cu);s.collection.objects.link(ob);ob.parent=parent;cu.materials.append(mat)
    return ob
def cube(name,loc,dims,mat,bevel=.02):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.parent=ship;o.data.materials.append(mat)
    mod=o.modifiers.new('Hand finished edges','BEVEL');mod.width=bevel;mod.segments=3
    o.modifiers.new('Face normals','WEIGHTED_NORMAL');return o

# Remove the entire floating infographic treatment, including filament wakes.
prefixes=('Ocean |','Flow field','Dataset |','Wake |','Foam fleck','Hull | horizontal','Hull | heavy','Continuous brass strake','Canvas panel seam','Sail edge bolt rope','Sail hem','Lateen hem')
for o in list(s.objects):
    if o.name.startswith(prefixes) or o.name=='Hand lofted hull':bpy.data.objects.remove(o,do_unlink=True)
for o in list(s.objects):
    if o.type=='LIGHT':bpy.data.objects.remove(o,do_unlink=True)

# Rich, small-scale wood grain; remove oversized bump from the previous timber.
wood=bpy.data.materials['Deck • warm teak'];dark=bpy.data.materials['Wales and rails • dark oak']
hullmat=bpy.data.materials['Hull • aged oak'];brass=bpy.data.materials['Aged brass fittings']
rope=bpy.data.materials['Rigging • flax']
for mat,base in [(hullmat,(.22,.075,.021)),(wood,(.34,.17,.063)),(dark,(.07,.029,.012))]:
    for node in mat.node_tree.nodes:
        if node.type=='BUMP':node.inputs['Distance'].default_value=.006;node.inputs['Strength'].default_value=.2
        if node.type=='VALTORGB':
            node.color_ramp.elements[0].color=(*(c*.75 for c in base),1)
            node.color_ramp.elements[1].color=(*(c*1.3 for c in base),1)
    mat.node_tree.nodes.get('Principled BSDF').inputs['Roughness'].default_value=.4

# Dense continuous hull loft. Planking follows exactly the same surface.
stations=[(-3.5,.18,1.7),(-3.15,.88,1.55),(-2.5,1.22,1.3),(-1.4,1.38,1.15),(0,1.4,1.1),(1.4,1.18,1.2),(2.5,.72,1.43),(3.35,.035,1.78)]
def station(x):
    i=next((i for i in range(len(stations)-1) if x<=stations[i+1][0]),len(stations)-2)
    a,b=stations[i:i+2];u=(x-a[0])/(b[0]-a[0])
    return a[1]*(1-u)+b[1]*u,a[2]*(1-u)+b[2]*u
def hullpoint(x,theta,offset=0):
    w,z=station(x)
    return (x,(w+offset)*sin(theta),-.35+(z+.35)*(1-cos(theta)))
nx,ny=140,48
vs=[hullpoint(-3.5+6.85*i/nx,-pi/2+pi*j/ny) for i in range(nx+1) for j in range(ny+1)]
fs=[]
for i in range(nx):
    for j in range(ny):
        a=i*(ny+1)+j;fs.append((a,a+1,a+ny+2,a+ny+1))
fs.extend([tuple(range(ny,-1,-1)),tuple(range(nx*(ny+1),(nx+1)*(ny+1)))])
mesh('V6 | watertight timber hull',vs,fs,hullmat,ship)
for side in [-1,1]:
    for k in range(2,12):
        theta=side*k/11*pi/2
        curve('V6 | flush plank caulking',[hullpoint(-3.48+6.80*i/160,theta,.003) for i in range(161)],.006,dark)
    for theta in [.92,1.32,pi/2]:
        curve('V6 | structural oak wale',[hullpoint(-3.47+6.78*i/160,side*theta,.017) for i in range(161)],.034,dark)

# Give every animated sail the same fine folds at all shape-key poses.
for o in s.objects:
    if o.type!='MESH' or not o.data.shape_keys or 'canvas' not in o.name.lower():continue
    for key in o.data.shape_keys.key_blocks:
        for v in key.data:
            v.co.x+=.016*sin(v.co.y*24+v.co.z*3)+.009*sin(v.co.y*39-v.co.z*5)
    sub=o.modifiers.new('Fine canvas silhouette','SUBSURF');sub.levels=1;sub.render_levels=1
for mat in bpy.data.materials:
    if 'Sails' not in mat.name:continue
    nodes=mat.node_tree.nodes;p=nodes.get('Principled BSDF')
    if p:
        p.inputs['Roughness'].default_value=.78
        p.inputs['Sheen Weight'].default_value=.25
        p.inputs['Subsurface Weight'].default_value=.035
    for n in nodes:
        if n.type=='BUMP':n.inputs['Distance'].default_value=.0025;n.inputs['Strength'].default_value=.2

# Small readable deck details: coopered barrels, rope coils, belaying pins.
iron=material('V6 | forged iron',(.025,.033,.041),.36,.7)
for x,y,z in [(-2.65,-.62,2.46),(-2.1,-.65,2.46),(.35,.75,1.28)]:
    n=24;vs=[]
    for j in range(9):
        t=j/8;r=.19+.036*sin(pi*t)
        vs.extend([(x+r*cos(2*pi*i/n),y+r*sin(2*pi*i/n),z+.48*t) for i in range(n)])
    fs=[(j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i) for j in range(8) for i in range(n)]
    fs+=[tuple(range(8*n,9*n))];mesh('V6 | coopered oak barrel',vs,fs,wood,ship)
    for h in [.07,.24,.41]:
        r=.195+.036*sin(pi*h/.48)
        curve('V6 | barrel iron hoop',[(x+r*cos(2*pi*i/64),y+r*sin(2*pi*i/64),z+h) for i in range(65)],.012,iron)
for x,y,z in [(.55,-.65,1.32),(1.9,.4,1.85),(-2.15,.65,2.48)]:
    curve('V6 | coiled deck rope',[(x+(.045+.19*i/240)*cos(i/240*8*pi),y+(.045+.19*i/240)*sin(i/240*8*pi),z+.007*sin(i*.3)) for i in range(241)],.012,rope)
for side in [-1,1]:
    cube('V6 | belaying rail',(-.6,side*.94,1.69),(.85,.1,.1),wood)
    for i in range(6):curve('V6 | belaying pin',[(-.96+i*.14,side*.94,1.58),(-.96+i*.14,side*.94,1.83)],.017,brass)

# Bright maritime sky. Soft cloud banks live in the world, with no horizon edge.
w=bpy.data.worlds.new('V6 | ocean daylight');w.use_nodes=True;s.world=w
n=w.node_tree.nodes;l=w.node_tree.links;n.clear()
out=n.new('ShaderNodeOutputWorld');bg=n.new('ShaderNodeBackground');bg.inputs['Strength'].default_value=.65;l.new(bg.outputs[0],out.inputs[0])
tc=n.new('ShaderNodeTexCoord');sep=n.new('ShaderNodeSeparateXYZ');l.new(tc.outputs['Normal'],sep.inputs[0])
sky=n.new('ShaderNodeValToRGB');sky.color_ramp.elements[0].position=0;sky.color_ramp.elements[0].color=(.58,.79,.92,1)
sky.color_ramp.elements[1].position=.7;sky.color_ramp.elements[1].color=(.075,.32,.65,1);l.new(sep.outputs['Z'],sky.inputs[0])
noise=n.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=5;noise.inputs['Detail'].default_value=3;noise.inputs['Roughness'].default_value=.65;l.new(tc.outputs['Normal'],noise.inputs[0])
cloud=n.new('ShaderNodeValToRGB');cloud.color_ramp.elements[0].position=.53;cloud.color_ramp.elements[1].position=.72;l.new(noise.outputs['Fac'],cloud.inputs[0])
mix=n.new('ShaderNodeMixRGB');mix.inputs[2].default_value=(.88,.94,1,1);l.new(cloud.outputs[0],mix.inputs[0]);l.new(sky.outputs[0],mix.inputs[1])
# A physical sky avoids enormous soft cloud reflections looking like white paint.
physical=n.new('ShaderNodeTexSky');physical.sky_type='MULTIPLE_SCATTERING';physical.sun_elevation=.65;physical.sun_rotation=2.2;physical.sun_disc=False;physical.air_density=1;physical.aerosol_density=.25
bg.inputs['Strength'].default_value=.3;l.new(physical.outputs[0],bg.inputs['Color'])
bpy.ops.object.light_add(type='SUN',location=(2,-4,12));sun=bpy.context.object;sun.name='V6 | warm trade-wind sun';sun.rotation_euler=(.42,-.5,-.45);sun.data.energy=2.1;sun.data.angle=.12;sun.data.color=(1,.89,.73)
bpy.ops.object.light_add(type='AREA',location=(6,-7,11));key=bpy.context.object;key.name='V6 | sky bounce';key.data.energy=650;key.data.shape='DISK';key.data.size=9;key.rotation_euler=(Vector((0,0,3))-key.location).to_track_quat('-Z','Y').to_euler()

# Actual FFT ocean geometry, keyframed time: all 312 frames remain scrubbable.
water=material('V6 | cobalt turquoise ocean',(.006,.10,.19),.28)
n=water.node_tree.nodes;l=water.node_tree.links;p=n.get('Principled BSDF')
p.inputs['IOR'].default_value=1.333;p.inputs['Specular IOR Level'].default_value=.3;p.inputs['Coat Weight'].default_value=.10;p.inputs['Coat Roughness'].default_value=.22
tc=n.new('ShaderNodeTexCoord');noise=n.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=.42;noise.inputs['Detail'].default_value=2;l.new(tc.outputs['Object'],noise.inputs[0])
ramp=n.new('ShaderNodeValToRGB');ramp.color_ramp.elements[0].color=(.007,.065,.17,1);ramp.color_ramp.elements[1].color=(.016,.28,.34,1);l.new(noise.outputs['Fac'],ramp.inputs[0])
attr=n.new('ShaderNodeAttribute');attr.attribute_name='OceanFoam'
foam=n.new('ShaderNodeValToRGB');foam.color_ramp.elements[0].position=.65;foam.color_ramp.elements[1].position=.95;l.new(attr.outputs['Fac'],foam.inputs[0])
mix=n.new('ShaderNodeMixRGB');mix.inputs[2].default_value=(.66,.88,.88,1);l.new(foam.outputs[0],mix.inputs[0]);l.new(ramp.outputs[0],mix.inputs[1]);l.new(mix.outputs[0],p.inputs['Base Color'])
rip=n.new('ShaderNodeTexNoise');rip.inputs['Scale'].default_value=5.5;rip.inputs['Detail'].default_value=2;l.new(tc.outputs['Object'],rip.inputs[0])
bump=n.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.36;bump.inputs['Distance'].default_value=.055;l.new(rip.outputs['Fac'],bump.inputs['Height']);l.new(bump.outputs[0],p.inputs['Normal'])
# Wake painted into the actual ocean shader, never separate floating ribbons.
def mathnode(op,a,b=None):
    m=n.new('ShaderNodeMath');m.operation=op
    for idx,v in enumerate([a,b]):
        if v is None:continue
        if isinstance(v,(int,float)):m.inputs[idx].default_value=v
        else:l.new(v,m.inputs[idx])
    return m.outputs[0]
geo=n.new('ShaderNodeNewGeometry');xy=n.new('ShaderNodeSeparateXYZ');l.new(geo.outputs['Position'],xy.inputs[0])
x=xy.outputs['X'];y=xy.outputs['Y']
aft=mathnode('MAXIMUM',mathnode('SUBTRACT',-1.8,x),0)
center=mathnode('ADD',mathnode('MULTIPLY',aft,.20),1.13)
delta=mathnode('ABSOLUTE',mathnode('SUBTRACT',mathnode('ABSOLUTE',y),center))
band=mathnode('LESS_THAN',delta,mathnode('ADD',.22,mathnode('MULTIPLY',aft,.07)))
band=mathnode('MULTIPLY',band,mathnode('GREATER_THAN',x,-13))
band=mathnode('MULTIPLY',band,mathnode('LESS_THAN',x,2.1))
grain=n.new('ShaderNodeTexNoise');grain.noise_dimensions='4D';grain.inputs['Scale'].default_value=7;grain.inputs['Detail'].default_value=2;l.new(geo.outputs['Position'],grain.inputs[0])
grain.inputs['W'].default_value=0;grain.inputs['W'].keyframe_insert('default_value',frame=1)
grain.inputs['W'].default_value=4;grain.inputs['W'].keyframe_insert('default_value',frame=312)
speck=mathnode('GREATER_THAN',grain.outputs['Fac'],mathnode('ADD',.55,mathnode('MULTIPLY',aft,.008)))
band=mathnode('MULTIPLY',band,speck)
combined=mathnode('MAXIMUM',foam.outputs['Color'],band)
l.new(combined,mix.inputs[0])
sea=mesh('V6 | open ocean',[(0,0,0)],[],water)
o=sea.modifiers.new('Wind driven ocean spectrum','OCEAN');o.geometry_mode='GENERATE';o.resolution=7;o.viewport_resolution=7;o.spatial_size=60;o.wave_scale=1.15;o.choppiness=1.1;o.wind_velocity=20;o.wave_scale_min=.15;o.use_foam=True;o.foam_layer_name='OceanFoam';o.foam_coverage=.05;o.repeat_x=5;o.repeat_y=5
o.time=0;o.keyframe_insert('time',frame=1);o.time=13;o.keyframe_insert('time',frame=312)
# Beyond the detailed sea, a matching flat expanse takes the horizon to infinity.
mesh('V6 | distant ocean horizon',[(-12000,-12000,-.3),(12000,-12000,-.3),(12000,12000,-.3),(-12000,12000,-.3)],[(0,1,2,3)],water)

for cam in [o for o in s.objects if o.type=='CAMERA']:cam.data.clip_end=30000
s.render.engine='CYCLES';s.cycles.samples=32;s.cycles.use_denoising=True
prefs=bpy.context.preferences.addons['cycles'].preferences
try:
    prefs.compute_device_type='METAL';prefs.get_devices()
    for d in prefs.devices:d.use=d.type=='METAL'
    # Metal kernel compilation crashes in this installed Blender build.
    s.cycles.device='CPU'
except Exception as exc:print('GPU unavailable:',exc)
s.cycles.max_bounces=6;s.cycles.transparent_max_bounces=6
s.render.resolution_x=1280;s.render.resolution_y=720;s.render.resolution_percentage=100
s.render.image_settings.file_format='PNG';s.render.fps=24
s.view_settings.view_transform='AgX';s.view_settings.exposure=-.45
try:s.view_settings.look='AgX - Medium High Contrast'
except TypeError:pass
s['version_6']='New sunny art direction, open ocean, no data filaments, flush planking, sail folds and deck details. Original Embat UV prints and both camera shots preserved.'
s.frame_set(240)
bpy.ops.wm.save_as_mainfile(filepath=str(R/'ELKANO-v6-ocean.blend'))
out=R/'frames-v6';out.mkdir(exist_ok=True)
frames=[96,240,312] if '--test' in sys.argv else range(1,313)
for f in frames:
    path=out/f'{f:04d}.png'
    if path.exists() and '--test' not in sys.argv:continue
    s.frame_set(f);s.render.filepath=str(path);bpy.ops.render.render(write_still=True)
print('V6 COMPLETE',flush=True)
