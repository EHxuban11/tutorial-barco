"""Print Embat on the existing beige cloth using a white-free shader mask."""
import bpy, shutil, sys
from pathlib import Path
root=Path(__file__).resolve().parent;s=bpy.context.scene
asset=root/'assets/embat-symbol.jpg'
image=bpy.data.images.load(str(asset),check_existing=True);image.pack()
cloth=bpy.data.materials.get('Sails • woven ivory')
assert cloth
printed=cloth.copy();printed.name='Sails | Embat navy ink on original beige canvas'
nodes=printed.node_tree.nodes;links=printed.node_tree.links
p=nodes.get('Principled BSDF');beige=tuple(p.inputs['Base Color'].default_value)
tex=nodes.new('ShaderNodeTexImage');tex.name='Supplied Embat symbol';tex.image=image;tex.extension='EXTEND'
uv=nodes.new('ShaderNodeUVMap');uv.uv_map='Embat print'
links.new(uv.outputs['UV'],tex.inputs['Vector'])
grey=nodes.new('ShaderNodeRGBToBW');links.new(tex.outputs['Color'],grey.inputs[0])
mask=nodes.new('ShaderNodeValToRGB');mask.name='Remove white background; preserve canvas'
mask.color_ramp.elements[0].position=.08;mask.color_ramp.elements[0].color=(1,1,1,1)
mask.color_ramp.elements[1].position=.8;mask.color_ramp.elements[1].color=(0,0,0,1)
links.new(grey.outputs[0],mask.inputs[0])
mix=nodes.new('ShaderNodeMixRGB');mix.blend_type='MIX';mix.inputs[1].default_value=beige;mix.inputs[2].default_value=(.006,.009,.033,1)
links.new(mask.outputs['Color'],mix.inputs[0]);links.new(mix.outputs[0],p.inputs['Base Color'])
modified=[]
for o in s.objects:
    if o.type!='MESH' or not any(m==cloth for m in o.data.materials):continue
    for i,m in enumerate(o.data.materials):
        if m==cloth:o.data.materials[i]=printed
    uv=o.data.uv_layers.get('Embat print') or o.data.uv_layers.new(name='Embat print')
    coords=[v.co for v in o.data.vertices]
    lateen='Mizzen' in o.name
    # Square sails face the bow (+X); their print reads left-to-right from +X.
    ax=0 if lateen else 1
    lo=min(v[ax] for v in coords);hi=max(v[ax] for v in coords)
    bottom=min(v.z for v in coords);top=max(v.z for v in coords)
    for poly in o.data.polygons:
        for li in poly.loop_indices:
            co=o.data.vertices[o.data.loops[li].vertex_index].co
            u=(co[ax]-lo)/(hi-lo);v=(co.z-bottom)/(top-bottom)
            if lateen:
                # Smaller emblem inside the widest region of the triangular cloth.
                u=(co[ax]-(lo+.64*(hi-lo)))/1.3+.5
                v=(co.z-(bottom+.46*(top-bottom)))/1.3+.5
            else:
                u=(co[ax]-(lo+hi)/2)/(top-bottom)*.92+.5
                v=(v-.51)*.92+.5
            uv.data[li].uv=(u,v)
    modified.append(o.name)
assert len(modified)==5,modified
s['sail_branding']='User supplied Embat symbol on all five sails. White background masked in material; original beige, fabric bump and roughness preserved. UVs deform with the animated cloth. Flag unchanged.'
s.frame_set(312);s.render.resolution_x=1920;s.render.resolution_y=1080;s.cycles.samples=64
s.render.filepath=str(root/'renders/elkano-branded-front.png')
bpy.ops.wm.save_as_mainfile(filepath=str(root/'ELKANO-branded-sails.blend'))
bpy.ops.render.render(write_still=True)
s.render.resolution_x=800;s.render.resolution_y=450;s.cycles.samples=16
out=root/'preview-branded';out.mkdir(exist_ok=True)
frames=[96,240,277,312] if '--test' in sys.argv else range(1,313)
for f in frames:
    p=out/f'{f:04d}.png'
    if p.exists() and '--test' not in sys.argv:continue
    s.frame_set(f);s.render.filepath=str(p);bpy.ops.render.render(write_still=True)
print('BRANDED SAILS:',modified)
