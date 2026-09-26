from pathlib import Path
import imageio.v2 as iio
root=Path(__file__).resolve().parent
frames=sorted((root/'preview-victoria').glob('*.png'))
assert len(frames)==72, f'Expected 72 frames; found {len(frames)}'
with iio.get_writer(root/'ELKANO-victoria-preview.mp4',fps=12,codec='libx264',quality=8,macro_block_size=2,ffmpeg_params=['-movflags','+faststart','-g','1']) as writer:
    for f in frames:writer.append_data(iio.imread(f))
