# ELKANO — Blender scene

Rendered videos have been moved to `../videos/`, ordered oldest to newest:

| File | Original render |
| --- | --- |
| `../videos/1.mp4` | ELKANO-preview.mp4 |
| `../videos/2.mp4` | ELKANO-victoria-preview.mp4 |
| `../videos/3.mp4` | ELKANO-camera-flyby.mp4 |
| `../videos/4.mp4` | ELKANO-two-shots.mp4 |
| `../videos/5.mp4` | ELKANO-branded-sails.mp4 |
| `../videos/6.mp4` | V6 — new ocean, sunny lighting and refined Victoria |

The sections below retain the original render names for identification. Source
reference clips remain in `../video/`. Stills remain in `renders/`.

## Current version: V6 / open ocean

`ELKANO-v6-ocean.blend` is a separate art-directed revision of the branded scene.
The boat remains a stylized Nao Victoria interpretation, with a narrower,
elongated hull, raised wooden stern, three masts, square sails and a lateen
mizzen. It is not an archaeological reconstruction. Historical reference:
https://www.fundacionnaovictoria.org/es/nao-victoria/

- All floating data, sparklines, filament wakes and old sea geometry removed.
- Animated FFT Ocean modifier, distant horizon, blue water, ripple normals,
  whitecaps and a fragmented wake integrated into the water shader.
- Daylight sky and sun, richer contrast, smaller-scale wood grain.
- Continuous new hull with surface-following plank joints and wales; cloth
  folds, deck barrels, coiled ropes and belaying pins.
- Original Embat sail prints and flag, two shots and cut at frame 97 retained.
- `frames-v6/`: 312 native 1280 × 720 PNG frames, 24 fps, Cycles with denoising.
- `renders/elkano-v6-hero.png`: 1920 × 1080, up to 96 samples.
- `../videos/6.mp4`: 13 seconds, silent, H.264 all-intra for later seeking.

Build and inspect three key poses:

```sh
/Applications/Blender.app/Contents/MacOS/Blender -b blender/ELKANO-branded-sails.blend --python blender/art_directed_voyage.py -- --test
```

Render the remaining frames (resumes existing frames) and encode:

```sh
/Applications/Blender.app/Contents/MacOS/Blender -b blender/ELKANO-v6-ocean.blend --python blender/render_v6.py
.venv/bin/python blender/encode_v6.py
```

The encoder refuses to overwrite `6.mp4`. If changing the scene, use a fresh
frame directory and next numbered video; do not mix old and new frames.
The initial Metal attempt crashed during kernel compilation in `path_cache_get`.
CPU fallback worked. A separate Metal test then succeeded using an isolated,
short cache path (`XDG_CACHE_HOME=/tmp/elk.n6lVRb`); the remaining frames can be
rendered with that environment and `-- --gpu` on `render_v6.py`. The saved
scene defaults to CPU for portability. First GPU use compiles kernels and can
take several minutes. Original `.blend` files and videos 1–5 remain untouched.

## Embat on all sails

`ELKANO-branded-sails.blend` / `ELKANO-branded-sails.mp4` retain the two-shot
13-second edit and add the supplied Embat symbol to all five sails. The image
is packed into the blend. A luminance mask uses only the navy mark: white
image areas reveal the original beige fabric material, retaining its bump and
roughness. UV coordinates deform with the animated cloth and maintain the
symbol's proportions. The separate Embat wordmark flag is unchanged.

`renders/elkano-branded-front.png` shows the result from the bow at 1920 × 1080.
`preview-branded/` contains all 312 frames, rendered at 800 × 450, 16 samples.
The original ocean, camera edit, model geometry and lighting are unchanged.

Rebuild with `logo_sails.py` inside Blender, loading `ELKANO-two-shots.blend`,
then run `.venv/bin/python blender/encode_branded.py`.

## Two-shot edit

`ELKANO-two-shots.blend` has two timeline camera markers, with a hard cut at
frame 97. Shot 1 is the previous four-second aerial flyby. Shot 2 is a new
nine-second overhead descent, close side passage and low frontal pullback,
inspired by `video/clip_0m18s-0m27s.mp4` (BON VOYAGE!).

`ELKANO-two-shots.mp4` is the complete 13-second, 312-frame, 24 fps preview.
The first 96 frames are reused from the previous flyby; `preview-second/`
contains frames 97–312. `renders/second-pan-contact.jpg` previews the new path.
Boat/flag motion repeats to cover the longer edit. Ocean, geometry, materials
and lighting are unchanged. The low angle exposes the existing neutral world
background; this is a camera study, not a final environment treatment.

To rebuild, run `two_shot_edit.py` in Blender with `ELKANO-camera-flyby.blend`
loaded, then run `.venv/bin/python blender/encode_two_shots.py`. Add `-- --test`
to the Blender command to render only eight key poses, and `--test` to the
encoder to generate only the contact sheet.

## Camera study: aerial flyby

`ELKANO-camera-flyby.blend` adds a perspective camera to the Victoria scene.
The ship geometry, materials, ocean and lighting are preserved. The four-second
camera path is inspired by the supplied `video/clip_0m54s-0m58s.mp4`: distant
overhead approach, descent and an accelerating sweep to a three-quarter view.
It is an interpretation of the shot, not a tracked camera solve.

- `ELKANO-camera-flyby.mp4`: 96 frames, 24 fps, 800 × 450 motion preview.
- `preview-flyby/`: individually rendered frames for random-access scrolling.
- `renders/elkano-flyby.png`: 1920 × 1080, 128-sample Cycles still.
- `renders/elkano-flyby-contact.jpg`: overview of six stages of the camera path.

Run `camera_flyby.py` inside Blender with `ELKANO-victoria.blend` loaded to
reproduce the scene and renders, then `.venv/bin/python blender/encode_flyby.py`.
Material Preview is enabled in the saved workspace so the Embat flag texture
is visible. No changes have been made to the original Victoria blend.

## Earlier version: Victoria

`ELKANO-victoria.blend` is the revised scene: aged wooden hull, raised stern and
forecastle, triangular lateen mizzen, ratlines and mast-top platforms. It is a
stylized interpretation inspired by the Nao Victoria, not an exact historical
reconstruction. Reference: https://www.fundacionnaovictoria.org/the-nao-carrack/

The waving flag uses the user's supplied `images.png`, copied into
`assets/embat-user-flag.png` and packed into the blend. The camera frames the
boat more closely and the water/data decoration has been reduced.

- Still: `renders/elkano-victoria.png`
- Preview: `ELKANO-victoria-preview.mp4`
- Frame sequence: `preview-victoria/`

The original `ELKANO.blend`, hero and preview remain available for comparison.
The scripts now build and render the Victoria revision. In the render command
below, use `blender/ELKANO-victoria.blend` for this version.

## Original version

Open `ELKANO.blend` in Blender. Press Numpad 0 for the camera, Space to play.
The timeline has 144 frames at 24 fps (six seconds). The ship, sails, flag,
ocean and camera are animated. Animation is keyframed and requires no external
simulation caches, so jumping directly to any frame works.

The flag uses Embat's actual logo, downloaded from its website, packed into the
blend: https://www.embat.io/wp-content/uploads/2026/04/0426_LOGO_696px_Navy.svg

Sea labels and sparklines reuse the monthly aggregates in `../scene_data.js`.
Ocean waves and ship movements are art direction, not financial predictions.

`renders/elkano-hero.png`: 1600 × 1000 Cycles still.
`ELKANO-preview.mp4`: 800 × 500, six-second preview, 12 fps, all-intra encoding.
`preview/`: 72 numbered PNGs (every second timeline frame), suitable for a later
scroll-controlled image sequence. The website is intentionally not built yet.

For a full-resolution sequence, open the blend, set the output directory to a
new `final/` directory, keep PNG output and render Animation (Cmd/Ctrl F12).
Map scroll progress to `1 + round(progress * 143)` for the full 144-frame render.

Rebuild from project root:

```sh
.venv/bin/python blender/prepare_assets.py
/Applications/Blender.app/Contents/MacOS/Blender -b -t 8 --python blender/build_elkano.py
/Applications/Blender.app/Contents/MacOS/Blender -b blender/ELKANO-victoria.blend -t 8 --python blender/render_preview.py
.venv/bin/python blender/encode_preview.py
```

Asset preparation needs resvg-py and Pillow; video encoding uses imageio and
imageio-ffmpeg. These are installed in the project's existing `.venv`.
