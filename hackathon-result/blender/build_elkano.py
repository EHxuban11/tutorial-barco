"""Build an editable, deterministic Blender scene. No simulation caches needed."""
import bpy, math, random, json, re
from pathlib import Path
from mathutils import Vector
from math import sin, cos, pi

ROOT = Path(__file__).resolve().parent
random.seed(18)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
for d in list(bpy.data.collections):
    if d.name != 'Collection': bpy.data.collections.remove(d)
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.samples = 24
scene.cycles.use_denoising = True
scene.render.resolution_x = 1600
scene.render.resolution_y = 1000
scene.render.resolution_percentage = 100
scene.render.fps = 24
scene.frame_start, scene.frame_end = 1, 144
scene.world.color = (0.12, 0.12, 0.12)
scene.view_settings.view_transform = 'AgX'
scene.render.image_settings.file_format = 'PNG'

def mat(name, color, metallic=0, rough=.45, emission=0):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value=(*color,1)
    p.inputs['Metallic'].default_value=metallic; p.inputs['Roughness'].default_value=rough
    if emission:
        p.inputs['Emission Color'].default_value=(*color,1); p.inputs['Emission Strength'].default_value=emission
    return m
navy=mat('Hull • aged oak',(.16,.067,.024),0,.58)
wood=mat('Deck • warm teak',(.29,.135,.047),0,.56)
gold=mat('Wales and rails • dark oak',(.095,.042,.018),0,.63)
brass=mat('Aged brass fittings',(.43,.27,.09),.65,.38)
ivory=mat('Sails • woven ivory',(.86,.81,.65),0,.72)
rope=mat('Rigging • flax',(.25,.19,.11),0,.8)
ink=mat('Typography • pearl',(.62,.88,.85),.15,.35,.35)
cyan=mat('Data • turquoise',(.025,.51,.56),.35,.25,.5)
amber=mat('Data • amber',(.95,.48,.08),.3,.3,.7)
water=mat('Ocean • subdued petrol',(.012,.051,.058),.2,.48)
# Longitudinal timber grain, with weathered variation rather than enamel.
for material in [navy,wood,gold]:
    nodes=material.node_tree.nodes; links=material.node_tree.links
    coord=nodes.new('ShaderNodeTexCoord'); mapping=nodes.new('ShaderNodeVectorMath'); mapping.operation='MULTIPLY'; mapping.inputs[1].default_value=(2,55,80)
    links.new(coord.outputs['Generated'],mapping.inputs[0])
    grain=nodes.new('ShaderNodeTexNoise');grain.inputs['Scale'].default_value=3;grain.inputs['Detail'].default_value=3
    links.new(mapping.outputs['Vector'],grain.inputs['Vector'])
    ramp=nodes.new('ShaderNodeValToRGB'); base=material.diffuse_color[:3]
    ramp.color_ramp.elements[0].position=.18;ramp.color_ramp.elements[0].color=(*(c*.5 for c in base),1)
    ramp.color_ramp.elements[1].position=.8;ramp.color_ramp.elements[1].color=(*(c*1.5 for c in base),1)
    links.new(grain.outputs['Fac'],ramp.inputs[0]);links.new(ramp.outputs[0],nodes.get('Principled BSDF').inputs['Base Color'])
    b=nodes.new('ShaderNodeBump');b.inputs['Strength'].default_value=.23;b.inputs['Distance'].default_value=.04
    links.new(grain.outputs['Fac'],b.inputs['Height']);links.new(b.outputs[0],nodes.get('Principled BSDF').inputs['Normal'])
pn=ivory.node_tree.nodes.get('Principled BSDF')
noise=ivory.node_tree.nodes.new('ShaderNodeTexNoise'); noise.inputs['Scale'].default_value=160
bump=ivory.node_tree.nodes.new('ShaderNodeBump'); bump.inputs['Strength'].default_value=.16; bump.inputs['Distance'].default_value=.035
ivory.node_tree.links.new(noise.outputs['Fac'],bump.inputs['Height']); ivory.node_tree.links.new(bump.outputs['Normal'],pn.inputs['Normal'])

def mesh(name, verts, faces, material, parent=None):
    me=bpy.data.meshes.new(name); me.from_pydata(verts,[],faces); me.update()
    ob=bpy.data.objects.new(name,me); scene.collection.objects.link(ob)
    ob.data.materials.append(material)
    if parent: ob.parent=parent
    return ob
def cube(name,loc,scale,material,parent=None,bevel=.03):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc); ob=bpy.context.object; ob.name=name; ob.dimensions=scale
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); ob.data.materials.append(material)
    if parent: ob.parent=parent
    if bevel: mod=ob.modifiers.new('Soft crafted edges','BEVEL'); mod.width=bevel; mod.segments=3; ob.modifiers.new('Normals','WEIGHTED_NORMAL')
    return ob
def line(name,points,radius,material,parent=None):
    cu=bpy.data.curves.new(name,'CURVE'); cu.dimensions='3D'; cu.bevel_depth=radius; cu.bevel_resolution=2
    sp=cu.splines.new('POLY'); sp.points.add(len(points)-1)
    for p,co in zip(sp.points,points): p.co=(*co,1)
    ob=bpy.data.objects.new(name,cu); scene.collection.objects.link(ob); ob.data.materials.append(material)
    if parent: ob.parent=parent
    return ob
def pole(name,a,b,r,material,parent=None):
    return line(name,[a,b],r,material,parent)
def text(name,body,loc,size,material,rotation=(0,0,0),parent=None):
    cu=bpy.data.curves.new(name,'FONT'); cu.body=body; cu.size=size; cu.align_x='CENTER'; cu.extrude=.001
    ob=bpy.data.objects.new(name,cu); scene.collection.objects.link(ob); ob.location=loc; ob.rotation_euler=rotation; ob.data.materials.append(material)
    if parent: ob.parent=parent
    return ob

ship=bpy.data.objects.new('ELKANO | animated ship',None); scene.collection.objects.link(ship)
# Hull: continuous curved stations, pointed bow and high stern.
stations=[(-3.5,.18,1.7),(-3.15,.88,1.55),(-2.5,1.22,1.3),(-1.4,1.38,1.15),(0,1.4,1.1),(1.4,1.18,1.2),(2.5,.72,1.43),(3.35,.04,1.78)]
verts=[]
for x,w,z in stations:
    for y,h in [(-w,z),(-w*.97,.65),(-w*.7,.04),(0,-.28),(w*.7,.04),(w*.97,.65),(w,z)]: verts.append((x,y,h))
faces=[]
for i in range(len(stations)-1):
    for j in range(6): a=i*7+j; faces.append((a,a+1,a+8,a+7))
faces += [tuple(range(6,-1,-1)),tuple(range(49,56))]
hull=mesh('Hand lofted hull',verts,faces,navy,ship)
sub=hull.modifiers.new('Hull smooth','SUBSURF'); sub.levels=2
for p in hull.data.polygons:p.use_smooth=True
deckverts=[(x,-w,z-.06) for x,w,z in stations]+[(x,w,z-.06) for x,w,z in reversed(stations)]
mesh('Teak main deck',deckverts,[tuple(range(len(deckverts)))],wood,ship)
for side in [-1,1]:
    for dz,rad in [(0,.055),(-.35,.032),(-.61,.023)]:
        line('Continuous brass strake',[(x,side*w*(1 if dz==0 else .95),z+dz) for x,w,z in stations],rad,gold,ship)
    for i in range(30):
        x=-3.1+i*.207
        for k in range(len(stations)-1):
            a,b=stations[k:k+2]
            if a[0]<=x<=b[0]:
                t=(x-a[0])/(b[0]-a[0]); w=a[1]*(1-t)+b[1]*t; z=a[2]*(1-t)+b[2]*t
                pole('Rail stanchion',(x,side*w,z),(x,side*w,z+.3),.018,gold,ship)
                break
    line('Upper railing',[(x,side*w,z+.3) for x,w,z in stations],.028,gold,ship)
    for level in range(1,8):
        t=level/9
        line('Hull | horizontal plank seam',[(x,side*w*(.73+.26*t),.05+(z-.1)*t) for x,w,z in stations],.009,gold,ship)
    for x in [-2.5,-1.8,-1.1,-.4,.3,1,1.7,2.3]:
        for a,b in zip(stations,stations[1:]):
            if a[0]<=x<=b[0]:
                t=(x-a[0])/(b[0]-a[0]);w=a[1]*(1-t)+b[1]*t;z=a[2]*(1-t)+b[2]*t
                line('Hull | heavy timber rib',[(x,side*w*.72,.08),(x,side*w*.98,.65),(x,side*w,z)],.038,gold,ship)
                break
for y in [i*.17 for i in range(-6,7)]: line('Deck caulking',[(-2.6,y,1.28),(1.6,y,1.28)],.008,rope,ship)
cube('Stern castle',(-2.5,0,1.82),(1.55,2.15,1.05),navy,ship)
cube('Poop deck',(-2.5,0,2.38),(1.68,2.28,.12),wood,ship)
for side in [-1,1]:
    for z in [1.4,1.63,1.88,2.12,2.39]:pole('Stern planking',(-3.29,side*1.08,z),(-1.7,side*1.08,z),.026,gold,ship)
    for i in range(9):
        x=-3.27+i*.195;pole('Stern gallery railing',(x,side*1.1,2.4),(x,side*1.1,2.76),.026,wood,ship)
    pole('Stern gallery rail',(-3.3,side*1.1,2.76),(-1.7,side*1.1,2.76),.045,gold,ship)
for y in [-.67,-.23,.23,.67]:cube('Stern gallery window',(-3.285,y,1.88),(.025,.24,.27),gold,ship,.015)
cube('Raised forecastle',(2.02,0,1.52),(1.0,1.38,.45),navy,ship)
cube('Forecastle deck',(2.02,0,1.77),(1.08,1.48,.10),wood,ship)
for i in range(6):cube('Companionway step',(-1.5+i*.11,0,2.22-i*.15),(.16,.6,.12),wood,ship)
# Rudder and tiller, visible below the rounded stern.
cube('Stern rudder',(-3.42,0,.52),(.26,.18,1.48),wood,ship)
pole('Tiller',(-3.4,0,1.3),(-2.4,0,1.4),.055,gold,ship)
cube('Deck hatch',(.65,0,1.36),(.8,.68,.12),gold,ship)
for y in [-.24,-.12,0,.12,.24]: line('Hatch grate',[(.32,y,1.43),(.98,y,1.43)],.016,navy,ship)
pole('Bowsprit',(2.5,0,1.5),(4.5,0,2.4),.065,wood,ship)
pole('Bowsprit gilding',(4.05,0,2.23),(4.5,0,2.4),.07,gold,ship)

def sail(name,x,z,width,height):
    nx,ny=22,26; vs=[]; fs=[]
    for j in range(ny+1):
        v=j/ny
        for i in range(nx+1):
            u=i/nx; y=(u-.5)*width*(.76+.24*v)
            vs.append((x+.55*sin(pi*u)*sin(pi*v),y,z-height*v+.12*sin(pi*u)*v))
    for j in range(ny):
        for i in range(nx):a=j*(nx+1)+i; fs.append((a,a+1,a+nx+2,a+nx+1))
    ob=mesh(name,vs,fs,ivory,ship)
    for p in ob.data.polygons:p.use_smooth=True
    ob.shape_key_add(name='Rest'); key=ob.shape_key_add(name='Wind fullness')
    for p in key.data:p.co.x += .19*sin((p.co.z-z)*2.4)*max(0,1-(p.co.y/(width*.52))**2)
    for f,v in [(1,.15),(37,.95),(73,.2),(109,.9),(144,.15)]:key.value=v;key.keyframe_insert('value',frame=f)
    sol=ob.modifiers.new('Canvas thickness','SOLIDIFY');sol.thickness=.014
    for i in [0,nx]:line('Sail edge bolt rope',[vs[j*(nx+1)+i] for j in range(ny+1)],.018,rope,ship)
    for j in [0,ny]:line('Sail hem',[vs[j*(nx+1)+i] for i in range(nx+1)],.018,rope,ship)
    for i in range(3,nx,4):line('Canvas panel seam',[(a+.009,b,c) for a,b,c in [vs[j*(nx+1)+i] for j in range(ny+1)]],.005,gold,ship)
    pole('Yard', (x,-width*.57,z+.035),(x,width*.57,z+.035),.048,wood,ship)

for x,top,w in [(-1,6.45,3.65),(1.55,5.2,2.7),(-2.65,4.65,1.7)]:
    pole('Tapered mast',(x,0,1.25),(x,0,top),.065,wood,ship)
    pole('Mast cap',(x,0,top-.22),(x,0,top+.12),.07,gold,ship)
    if x!=-2.65:
        sail('Lower canvas',x,top-1.45,w,2.15 if x==-1 else 1.65)
        sail('Topsail',x,top-.2,w*.64,1.03)
        bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=.28,depth=.20,location=(x,0,top-1.36))
        crow=bpy.context.object;crow.name='Mast top | lookout platform';crow.parent=ship;crow.data.materials.append(wood)
    for side in [-1,1]:
        for offset in [-.48,0,.48]:pole('Standing shroud',(x,0,top-.85),(x+offset,side*1.05,1.4),.012,rope,ship)
        if x!=-2.65:pole('Yard brace',(x,side*w*.55,top-1.4),(x-1,side*.85,1.6),.012,rope,ship)
        for rung in range(1,16):
            t=rung/17;z=1.4+(top-.85-1.4)*t
            pole('Ratline | rope ladder',(x-.48*(1-t),side*1.05*(1-t),z),(x+.48*(1-t),side*1.05*(1-t),z),.01,rope,ship)
    pole('Fore stay',(x,0,top),(3.8,0,2.2),.013,rope,ship)
text('Ship name','V I C T O R I A',(0,-1.405,.98),.15,brass,(pi/2,0,0),ship)
# Mizzen: triangular lateen canvas and its long inclined yard.
A=Vector((-3.95,0,3.25)); B=Vector((-1.85,0,5.25)); C=Vector((-2.25,0,2.45))
lv=[];lf=[];ids={};count=22
for j in range(count+1):
    for i in range(count+1-j):
        u=i/count;v=j/count;p=A*(1-u-v)+B*u+C*v;p.y-=.32*sin(pi*u)*sin(pi*v)
        ids[i,j]=len(lv);lv.append(tuple(p))
for j in range(count):
    for i in range(count-j):
        lf.append((ids[i,j],ids[i+1,j],ids[i,j+1]))
        if i+j<count-1:lf.append((ids[i+1,j],ids[i+1,j+1],ids[i,j+1]))
lateen=mesh('Mizzen | triangular lateen sail',lv,lf,ivory,ship)
for p in lateen.data.polygons:p.use_smooth=True
lateen.shape_key_add(name='Rest');lk=lateen.shape_key_add(name='Wind')
for p in lk.data:p.co.y*=1.6
for f,v in [(1,.2),(37,1),(73,.1),(109,.8),(144,.2)]:lk.value=v;lk.keyframe_insert('value',frame=f)
line('Lateen hem',[tuple(A),tuple(C),tuple(B)],.018,rope,ship)
pole('Lateen angled yard',tuple(A+(A-B)*.08),tuple(B+(B-A)*.1),.045,wood,ship)
pole('Mizzen sheet',tuple(C),(-3.15,-.8,2.4),.015,rope,ship)

# Texture-mapped Embat flag. Shape keys preserve random-access frame scrubbing.
flagmat=mat('Embat • official logo on ivory',(.9,.87,.75),0,.6)
im=bpy.data.images.load(str(ROOT/'assets/embat-user-flag.png')); im.pack()
tex=flagmat.node_tree.nodes.new('ShaderNodeTexImage');tex.image=im
flagmat.node_tree.links.new(tex.outputs['Color'],flagmat.node_tree.nodes.get('Principled BSDF').inputs['Base Color'])
nx,nz=36,16
def flagverts(phase):
    return [(-1-2.35*i/nx, .24*(i/nx)*sin(i/nx*9-j/nz*2+phase), 6.48+1.06*j/nz-.22*(i/nx)+.1*(i/nx)*sin(i/nx*8+phase)) for j in range(nz+1) for i in range(nx+1)]
fv=flagverts(0); ff=[]
for j in range(nz):
    for i in range(nx): a=j*(nx+1)+i;ff.append((a,a+1,a+nx+2,a+nx+1))
flag=mesh('EMBAT | wind animated flag',fv,ff,flagmat,ship)
uv=flag.data.uv_layers.new()
for poly in flag.data.polygons:
    poly.use_smooth=True
    for li in poly.loop_indices:
        vi=flag.data.loops[li].vertex_index;uv.data[li].uv=(1-(vi%(nx+1))/nx,(vi//(nx+1))/nz)
flag.shape_key_add(name='Basis')
for n in range(8):
    key=flag.shape_key_add(name=f'Wind phase {n+1}')
    for p,co in zip(key.data,flagverts((n+1)*pi/4)):p.co=co
    for f in range(1,145,3):
        phase=((f-1)/36*8)%8; d=abs(phase-(n+1)%8);d=min(d,8-d)
        key.value=max(0,1-d);key.keyframe_insert('value',frame=f)
pole('Flagstaff',(-1,0,6.1),(-1,0,7.68),.026,gold,ship)

# Water is geometric, animated with two cached morph targets.
N=180;extent=90
def wave(x,y,p=0):return .12*sin(x*.8+y*.45+p)+.07*sin(y*1.4-x*.25-p*.7)
vs=[(-extent/2+extent*i/N,-extent/2+extent*j/N,0) for j in range(N+1) for i in range(N+1)]
vs=[(x,y,wave(x,y)) for x,y,z in vs];fs=[]
for j in range(N):
    for i in range(N):a=j*(N+1)+i;fs.append((a,a+1,a+N+2,a+N+1))
sea=mesh('Ocean | animated surface',vs,fs,water)
for p in sea.data.polygons:p.use_smooth=True
sea.shape_key_add(name='Basis');key=sea.shape_key_add(name='Swell')
for p in key.data:p.co.z=wave(p.co.x,p.co.y,pi)
for f,v in [(1,0),(37,1),(73,0),(109,1),(144,0)]:key.value=v;key.keyframe_insert('value',frame=f)

raw=(ROOT.parent/'scene_data.js').read_text()
monthly=json.loads(re.search(r'const MONTHLY=(.*?);',raw,re.S).group(1))
for row in range(5):
    y=-7+row*3.2
    points=[]
    for k in range(181):
        x=-18+k*.2;z=.26+.12*sin(x*.8+y*.45)
        points.append((x,y+.22*sin(x*.45+row),z))
    line('Flow field',points,.005,cyan)
for row in range(2):
    y=-5+row*10
    for col in range(5):
        x=-13+col*3.8
        if abs(x)<4.5 and abs(y)<2.5:continue
        m=monthly[(row*8+col)%24]
        text('Dataset | monthly value',f'{m[0]}  /  {m[1]:,.1f}',(x,y,.31),.18,ink)
        pts=[(x-1.3+k*.11,y+.6+monthly[(k+col)%24][1]/25000*.62,.3) for k in range(24)]
        line('Dataset | cash-in sparkline',pts,.018,amber if col%3==0 else cyan)
# Long luminous wake and foam ribbons behind the stern.
for side in [-1,1]:
    for r in range(2):
        pts=[]
        for j in range(90):
            t=j/89; x=-2.8-t*10; y=side*(.65+t*(2+r*.2))+.08*sin(t*35+r)
            pts.append((x,y,.27+.025*sin(t*45)))
        line('Wake | filament',pts,.012,ink)
for i in range(35):
    x=random.uniform(-9,3);side=random.choice([-1,1]); y=side*(1.35+max(0,-x-2)*.22+random.random()*.45)
    line('Foam fleck',[(x,y,.26),(x+.06+random.random()*.16,y+.02,.27)],.016,ink)

for f in range(1,145,6):
    t=(f-1)/143
    ship.location=(.42*sin(2*pi*t),.12*sin(2*pi*t),.09*sin(4*pi*t))
    ship.rotation_euler=(.025*sin(4*pi*t),.025*cos(2*pi*t),.035*sin(2*pi*t))
    ship.keyframe_insert('location',frame=f);ship.keyframe_insert('rotation_euler',frame=f)
ship.location=(0,0,0);ship.rotation_euler=(0,.025,0);ship.keyframe_insert('location',frame=144);ship.keyframe_insert('rotation_euler',frame=144)

def area(name,loc,power,color,size,target=(0,0,2)):
    bpy.ops.object.light_add(type='AREA',location=loc);ob=bpy.context.object;ob.name=name;ob.data.energy=power;ob.data.color=color;ob.data.shape='DISK';ob.data.size=size;ob.rotation_euler=(Vector(target)-ob.location).to_track_quat('-Z','Y').to_euler()
area('Key | warm silk',(1,-8,13),2600,(1,.83,.61),8)
area('Rim | arctic',(-4,6,10),3200,(.33,.72,1),7)
area('Bow | softbox',(9,1,6),1500,(.74,.9,1),6)
bpy.ops.object.camera_add(location=(12,-19,11));camera=bpy.context.object;camera.name='Camera | scroll-ready voyage';scene.camera=camera
camera.data.type='ORTHO';camera.data.lens=48;camera.data.ortho_scale=19.8
for f,loc,target,scale in [(1,(10,-22,10),(-.25,0,3.5),14.2),(72,(7,-23,9),(-.25,0,3.55),13.7),(144,(4,-24,9.8),(-.25,0,3.5),14.2)]:
    camera.location=loc;camera.rotation_euler=(Vector(target)-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.ortho_scale=scale
    camera.keyframe_insert('location',frame=f);camera.keyframe_insert('rotation_euler',frame=f);camera.data.keyframe_insert('ortho_scale',frame=f)
scene['README']='ELKANO / Embat — 144 frames at 24 fps. All motion is keyframed: scrub freely, no bake required. Sea numbers and sparklines from scene_data.js. Decorative waves are not a financial score.'
scene['logo_source']='User supplied images.png, packed into blend'
scene['historical_reference']='Nao Victoria inspired interpretation, not an exact reconstruction. https://www.fundacionnaovictoria.org/the-nao-carrack/'
scene.frame_set(48)
for screen in bpy.data.screens:
    for a in screen.areas:
        if a.type=='VIEW_3D':a.spaces.active.region_3d.view_perspective='CAMERA'
bpy.ops.object.select_all(action='DESELECT');ship.select_set(True);bpy.context.view_layer.objects.active=ship
scene.render.filepath=str(ROOT/'renders/elkano-victoria.png')
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'ELKANO-victoria.blend'))
bpy.ops.render.render(write_still=True)
