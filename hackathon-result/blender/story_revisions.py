"""Revised chest/papyri and 26-company harbor blockouts. Originals untouched."""
import bpy, math, random, sys, json
from pathlib import Path
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
R=Path(__file__).resolve().parent
args=sys.argv[sys.argv.index('--')+1:];kind=args[0];test='--test' in args
bpy.ops.wm.open_mainfile(filepath=str(R/'ELKANO-v6-ocean.blend'))
s=bpy.context.scene;ship=bpy.data.objects['ELKANO | animated ship'];ship.animation_data_clear();ship.location=(0,0,0);ship.rotation_euler=(0,0,0)
for marker in list(s.timeline_markers):s.timeline_markers.remove(marker)
random.seed(2026)
def mat(name,color):
 m=bpy.data.materials.new(name);m.use_nodes=True;m.diffuse_color=(*color,1);p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1);p.inputs['Roughness'].default_value=.65;return m
oak=bpy.data.materials['Deck • warm teak'];iron=mat('Revision iron',(.035,.04,.048));paper=mat('Blank parchment',(.83,.69,.43));ribbon=mat('Burgundy ribbon',(.24,.015,.026));sand=mat('Island sand',(.52,.4,.23));stone=mat('Limestone',(.62,.56,.44));green=mat('Island scrub',(.1,.22,.10));roof=mat('Clay roofs',(.30,.07,.025))
def box(name,loc,dims,material,parent=None):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=dims;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(material);o.parent=parent;be=o.modifiers.new('Edges','BEVEL');be.width=min(dims)*.06;be.segments=2;return o
def mesh(name,vs,fs,material,parent=None):
 me=bpy.data.meshes.new(name);me.from_pydata(vs,[],fs);me.update();o=bpy.data.objects.new(name,me);s.collection.objects.link(o);o.data.materials.append(material);o.parent=parent;return o
def sphere(name,loc,size,material):
 bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,location=loc);o=bpy.context.object;o.name=name;o.scale=size;o.data.materials.append(material);return o
def cyl(name,loc,radius,depth,material,parent=None):
 bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=radius,depth=depth,location=loc);o=bpy.context.object;o.name=name;o.rotation_euler.y=math.pi/2;o.data.materials.append(material);o.parent=parent;return o
def empty(name,loc):
 o=bpy.data.objects.new(name,None);s.collection.objects.link(o);o.location=loc;return o
def smooth(t):t=max(0,min(1,t));return t*t*(3-2*t)
camdata=bpy.data.cameras.new('Revision camera');cam=bpy.data.objects.new('Revision camera',camdata);s.collection.objects.link(cam);s.camera=cam;camdata.clip_end=30000
def camera(loc,target,lens):cam.location=loc;cam.rotation_euler=(Vector(target)-cam.location).to_track_quat('-Z','Y').to_euler();camdata.lens=lens
ocean=bpy.data.objects['V6 | open ocean'].modifiers.get('Wind driven ocean spectrum');ocean.spatial_size=200;ocean.wave_scale=.25;ocean.choppiness=.4
water=bpy.data.materials['V6 | cobalt turquoise ocean'];coord=water.node_tree.nodes.new('ShaderNodeTexCoord');coord.object=ship
for node in water.node_tree.nodes:
 if node.type=='SEPXYZ':water.node_tree.links.new(coord.outputs['Object'],node.inputs[0])
count=192 if kind=='cofre' else 144
if kind=='cofre':
 for ob in list(s.objects):
  if ob.name.startswith(('V6 | belaying rail','V6 | belaying pin')):ob.hide_render=True
 center=Vector((-.40,-.42,1.31));w,d,h=.52,.34,.25
 # Open-topped chest: walls, not a solid cube hiding the scrolls.
 box('Chest base',center+Vector((0,0,.025)),(w,d,.05),oak)
 for side in [-1,1]:
  box('Chest side',center+Vector((side*(w/2-.02),0,h/2)),(.04,d,h),oak)
  box('Chest face',center+Vector((0,side*(d/2-.02),h/2)),(w,.04,h),oak)
 for x in [-.17,.17]:box('Chest iron band',center+Vector((x,-d/2-.006,h/2)),(.026,.014,h),iron)
 hinge=empty('Small chest hinge',center+Vector((0,d/2,h)))
 box('Hinged lid',(0,-d/2,.015),(w+.025,d+.025,.035),oak,hinge)
 for x in [-.17,.17]:box('Lid iron band',(x,-d/2,.04),(.026,d+.025,.012),iron,hinge)
 scrolls=[]
 for i in range(3):
  root=empty(f'Papyrus {i+1}',center+Vector((0,-.10+i*.1,.20)))
  cyl('Rolled parchment',(0,0,0),.043,.39,paper,root)
  cyl('Tie ribbon',(0,0,0),.045,.022,ribbon,root)
  scrolls.append(root)
 # The middle scroll becomes a curling sheet; no cuts or mesh replacement.
 hero=scrolls[1]
 sheet=mesh('Unrolling blank papyrus',[(0,0,0)]*((40+1)*2),[(2*i,2*i+1,2*i+3,2*i+2) for i in range(40)],paper,hero)
 sheet.shape_key_add(name='Rolled');key=sheet.shape_key_add(name='Unrolled')
 for i in range(41):
  t=i/40
  for j in range(2):
   x=(j-.5)*.40
   sheet.data.shape_keys.key_blocks[0].data[2*i+j].co=(x,.039*math.sin(t*math.pi*5),.039*math.cos(t*math.pi*5))
   key.data[2*i+j].co=(x,.016*math.sin(t*math.pi*2),-.56*t)
 sol=sheet.modifiers.new('Paper thickness','SOLIDIFY');sol.thickness=.003
 for f in range(1,count+1):
  sec=(f-1)/24;t=smooth(sec/3)
  camera(Vector((7,-11,7)).lerp(Vector((.25,-2.0,2.7)),t),Vector((0,0,2.6)).lerp(center+Vector((0,0,.20+.63*smooth((sec-5)/2))),t),40+18*t)
  cam.keyframe_insert('location',frame=f);cam.keyframe_insert('rotation_euler',frame=f);camdata.keyframe_insert('lens',frame=f)
  hinge.rotation_euler.x=-math.radians(110)*smooth((sec-3)/1);hinge.keyframe_insert('rotation_euler',frame=f)
  rise=smooth((sec-5)/1.4);hero.location=center+Vector((0,-.10*rise,.20+1.1*rise));hero.scale=(1+.4*rise,)*3;hero.keyframe_insert('location',frame=f);hero.keyframe_insert('scale',frame=f)
  key.value=smooth((sec-5.7)/1.5);key.keyframe_insert('value',frame=f)
 # Ribbon slides out of view during release rather than staying across the paper.
 for child in hero.children:
  if child.name.startswith('Tie ribbon'):
   child.scale=(1,1,1);child.keyframe_insert('scale',frame=120);child.scale=(.001,)*3;child.keyframe_insert('scale',frame=145)
 s['chest_scale']='0.52 units wide versus approx 8-unit vessel; three separate rolled papyri, 1 second display pause.'
else:
 # City is pushed left; the entire right third remains open water.
 sphere('Large island',(-16,21,-.5),(23,17,2.4),sand)
 sphere('Green ridge',(-23,28,1),(14,10,3.8),green)
 box('Quay',(-14,9,.5),(34,3,1.1),stone)
 for x in [-28,-20,-12,-4]:
  box('Finger pier',(x,2,.5),(1,12,.3),oak)
  for y in [-3,0,3,6]:box('Pier pile',(x,y,.1),(.24,.24,1.6),oak)
 for row in range(3):
  for col in range(9):
   x=-31+col*3.2;y=13+row*3.9;h=random.uniform(1.4,3.5)
   box('Town house',(x,y,h/2+1),(2.6,3,h),stone)
   mesh('Pitched tile roof',[(x-1.4,y-1.6,h+1),(x+1.4,y-1.6,h+1),(x+1.4,y+1.6,h+1),(x-1.4,y+1.6,h+1),(x,y-1.6,h+2),(x,y+1.6,h+2)],[(0,1,4),(3,5,2),(0,4,5,3),(1,2,5,4)],roof)
   box('Town door',(x,y-1.51,1.7),(.4,.04,1.25),iron)
 hullmats=[mat('Healthy navy hull',(.015,.06,.13)),mat('Faded red hull',(.27,.055,.025)),mat('Old weathered hull',(.14,.12,.075))]
 anchors=[]
 def boat(name,loc,size,condition,angle):
  root=empty(name,loc);root.scale=(size,)*3;root.rotation_euler=(math.radians(24) if condition==2 else 0,0,angle)
  vs=[(-1.6,-.48,.3),(1.6,0,.3),(-1.6,.48,.3),(-1.9,0,.3),(-1.25,-.28,-.22),(1.3,0,-.15),(-1.25,.28,-.22)]
  mesh(name+' hull',vs,[(0,1,5,4),(1,2,6,5),(2,3,0,4,6),(4,5,6),(0,3,2,1)],hullmats[condition],root)
  box('Company mast',(0,0,1.18),(.065,.065,2.1),oak,root)
  cloth=mat(name+' canvas',(.82,.80,.67) if condition==0 else (.46,.42,.29))
  mesh('Company sail',[(0,0,2.15),(.07,0,.65),(1.1,.04,.65)],[(0,1,2)],cloth,root)
  if condition==0:box('Company deckhouse',(-.9,0,.49),(.65,.55,.45),oak,root)
  return root
 # Named boats in the left foreground, isolated from the background fleet.
 anchors.append(boat('COMPANY_A healthy large navy',(-26,-10,.05),1.35,0,.20))
 anchors.append(boat('COMPANY_B distressed red',(-16,-12,-.08),.9,2,-.35))
 for i in range(24):
  if i<16:x=-31+(i%8)*4;y=-3+(i//8)*6
  else:x=-31+(i-16)*4;y=-18
  boat(f'Company boat {i+3:02d}',(x,y,0),random.uniform(.5,1.0),i%3,random.uniform(-.5,.5))
 ship.location=(-10,-22,0);ship.rotation_euler.z=.15
 for f in range(1,count+1):
  t=(f-1)/(count-1);camera((12+2*t,-63+2*t,51),(0,5,0),38)
  cam.keyframe_insert('location',frame=f);cam.keyframe_insert('rotation_euler',frame=f)
  ship.location.x=-10+3*t;ship.keyframe_insert('location',frame=f)
 s.frame_set(count);bpy.context.view_layer.update()
 positions={o.name:dict(zip(['x','y','depth'],world_to_camera_view(s,cam,o.location+Vector((0,0,1))))) for o in anchors}
 (R/'city-company-anchors.json').write_text(json.dumps({'coordinates':'x from left, y from bottom; normalized camera frame','boats':positions},indent=2))
 s['company_fleet']='26 company boats plus the Embat Victoria. A: large navy boat left foreground. B: smaller tilted weathered boat to its right.'
s.render.engine='CYCLES';s.cycles.samples=12;s.cycles.use_denoising=True;s.cycles.max_bounces=4;s.render.use_persistent_data=True
s.render.resolution_x=800;s.render.resolution_y=450;s.render.resolution_percentage=100;s.render.fps=24;s.render.image_settings.file_format='PNG';s.frame_start=1;s.frame_end=count
s.frame_set(count);bpy.ops.wm.save_as_mainfile(filepath=str(R/f'ELKANO-revised-{kind}.blend'))
prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='METAL';prefs.get_devices()
for device in prefs.devices:device.use=device.type=='METAL'
s.cycles.device='GPU';out=R/f'revised-{kind}-frames-v3';out.mkdir(exist_ok=True)
frames=sorted(set([1,72,108,132,count])) if test else range(1,count+1)
for f in frames:
 path=out/f'{f:04d}.png'
 if path.exists():continue
 s.frame_set(f);s.render.filepath=str(path);bpy.ops.render.render(write_still=True);print(kind,f,count,flush=True)
