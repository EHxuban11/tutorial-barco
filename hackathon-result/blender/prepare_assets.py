from pathlib import Path
import resvg_py
from PIL import Image
import shutil

root = Path(__file__).resolve().parent
(root/'assets/embat-logo.png').write_bytes(resvg_py.svg_to_bytes(svg_string=(root/'assets/embat-official.svg').read_text(), width=1400, height=1400))
im = Image.open(root/'assets/embat-logo.png').convert('RGBA')
im = im.crop(im.getbbox())
flag = Image.new('RGBA', (1200, 600), '#f4eee0')
im.thumbnail((960, 330))
flag.alpha_composite(im, ((1200-im.width)//2, (600-im.height)//2))
flag.save(root/'assets/embat-flag.png')
if not (root/'assets/embat-user-flag.png').exists():
    raise FileNotFoundError('The supplied Embat flag image is missing.')
