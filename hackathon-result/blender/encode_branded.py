from pathlib import Path
import imageio.v2 as iio
root=Path(__file__).resolve().parent
frames=[root/'preview-branded'/f'{f:04d}.png' for f in range(1,313)]
assert all(p.exists() for p in frames)
with iio.get_writer(root/'ELKANO-branded-sails.mp4',fps=24,codec='libx264',quality=8,macro_block_size=2,ffmpeg_params=['-movflags','+faststart','-g','1']) as w:
    for p in frames:w.append_data(iio.imread(p))
