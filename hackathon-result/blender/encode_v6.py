from pathlib import Path
import imageio.v2 as iio
R=Path(__file__).resolve().parent
frames=[R/'frames-v6'/f'{i:04d}.png' for i in range(1,313)]
assert all(p.exists() for p in frames),'Incomplete render'
target=R.parent/'videos'/'6.mp4'
assert not target.exists(),'Do not overwrite an existing numbered video'
with iio.get_writer(target,fps=24,codec='libx264',quality=8,macro_block_size=2,ffmpeg_params=['-movflags','+faststart','-g','1','-pix_fmt','yuv420p']) as w:
    for p in frames:w.append_data(iio.imread(p))
reader=iio.get_reader(target)
print(target,reader.get_meta_data(), 'frames',reader.count_frames())
