"""Fast six-second preview, with one PNG per source animation frame."""
import bpy
from pathlib import Path
root=Path(__file__).resolve().parent
(root/'preview-victoria').mkdir(exist_ok=True)
s=bpy.context.scene
s.render.engine='CYCLES'
s.cycles.samples=8
s.cycles.use_denoising=True
s.render.resolution_x=800
s.render.resolution_y=500
s.render.resolution_percentage=100
s.render.image_settings.file_format='PNG'
for f in range(1,145,2):
    out=root/'preview-victoria'/f'{f:04d}.png'
    if out.exists():continue
    s.frame_set(f)
    s.render.filepath=str(out)
    bpy.ops.render.render(write_still=True)
