# What can we honestly reproduce?

## Three different claims

| Claim | Current evidence | Status |
| --- | --- | --- |
| Run the existing presentation with its existing videos | Packaged slides-only source, local media/fonts, package lock, successful static build and type check | Verified build; browser checks cover the hero, navigation and media loading |
| Re-render the original Blender layouts | Original editable scenes, packed brand assets and Python source are included | Local smoke renders check the hero and night files; a full fresh animation render has not been rerun during this audit |
| Recreate the project from an empty folder and regenerate comparable cinematic footage | Original creative prompts, the exact generation requests and a staged tutorial are documented | Plausible and actionable, but **not yet validated by an end-to-end clean-room rehearsal** |

We can teach the method with strong evidence. We cannot guarantee an identical generative result from the same prompt, returned seed or nominal model name. Model behavior can change and output varies. The original team also selected takes and edited how much of each clip was shown.

## The two central scenes

### Daytime hero

`hackathon-result/blender/ELKANO-scene01-zarpar.blend` contains the 288-frame, 24 fps lateral scene. `scene01_zarpar.py` explains its construction from the V6 ship. The archived upload input is `references/01-barco-largo.mp4`.

The [turning-point prompt](turning-point-prompt.md) plus the sail logo generated video 13 at 720p. This became `videos/zarpar-seedance.mp4` in the website. No photographic still was supplied first.

### Starry night

`hackathon-result/blender/ELKANO-scene03-estrellas.blend` contains the upward night composition. Historically, **one rendered still was held for four seconds** in `references/03-estrellas.mp4`; it was not a fully rendered four-second Blender animation.

The final night generation, video 23, used that held-still reference, the exact sail logo and `references/13-referencia-estilo-3s.mp4`. The latter is seconds **5 through 8** of generated video 13. Its exact request is `11-estrellas` in [fal-requests.json](audit/fal-requests.json).

Seedance supplied the cinematic background motion. `SkyStory.tsx` supplied the particles, constellation lines, score and large logo separately. Anyone teaching “both animations in Blender” must explain this distinction.

## Transcript coverage

The two primary logs have 6,399 and 2,110 records. The extraction includes 161 user messages in the visual-production scope, 14 recovered video prompts (13 with full saved receipts), one poster upscale and seven auxiliary image calls. The earlier inventory checked 11 top-level conversations plus a poster subagent and an approval log.

We do **not** claim universal transcript completeness: conversations not available locally, earlier Claude work, teammate sessions and manual GUI decisions may not be present. Git history supplies evidence for the team's constellation implementation. Current source files may consolidate several earlier edits rather than preserve every intermediate file version.

## Known limitations

- The historical encoders retain old monorepo paths. Use the portable skill render/media helpers or adapt those paths explicitly; do not imply every historical command runs unchanged in this archive layout.
- A new generative sky needs newly registered constellation coordinates. The archived coordinates are specific to the archived video.
- The archived presentation was designed for a wide screen. In a tall viewport, the cover crop can cut off right-side constellation/score content. A fresh tutorial website needs a deliberate narrow-screen layout; the archive is not claimed to be fully responsive.
- The historical request URLs may eventually expire. The key hero/night inputs and selected final clips are included locally; not every discarded take or intermediate input is bundled. Upload new references under the user's account for a new run.
- The short teaching prompts are a reconstruction, not verbatim historical Blender instructions. The original quotes and exact fal prompts are separately labeled.
- Full fresh Blender animation rendering and new paid generations have deliberately not been repeated in this audit.

The readiness bar for calling the tutorial validated is a recorded fresh run: model → hero reference → approved generated hero → night reference → generated night → working website, with inputs, versions, receipts, costs and failed attempts retained.

## Archive checks completed on 23 September 2026

- Static Next.js build: passed, 20 exported routes; TypeScript check: passed.
- Browser: hero/media loading, navigation and reverse progress checked; night Canvas/SVG layers present. Tall-screen crop limitation recorded above.
- Blender: one hero and one night frame rendered and visually inspected at 640×360, four samples.
- Media: all 13 bundled MP4s decoded fully; dimensions, duration, frame count and SHA-256 are recorded in [the media manifest](../hackathon-result/media-manifest.json).
- Portable media helper: held-still night encoding and the three-second hero excerpt produced valid 720p/24 fps MP4s. The full 288-frame hero encoding has not been repeated in this audit.
- Skills: all four packages passed the skill structure validator. That checks package format, not end-to-end artistic performance.
- Repository: local documentation links and included text were checked for missing targets and credential patterns; raw session logs are not included.

## Portable replay commands for the two archived references

Run from the repository root. These replay the archived scenes; they are **not** the from-scratch tutorial. Replace the Blender executable on another OS. The two smoke renders below were executed successfully and visually inspected during this audit.

```sh
# Hero smoke test: one frame, without changing the saved scene.
/Applications/Blender.app/Contents/MacOS/Blender --background \
  hackathon-result/blender/ELKANO-scene01-zarpar.blend --python-exit-code 1 \
  --python skills/xu-blender-animations/scripts/render_frames.py -- \
  --output verification/hero --frames 144 --width 640 --height 360 --samples 4

# Night: the historical input was one still.
/Applications/Blender.app/Contents/MacOS/Blender --background \
  hackathon-result/blender/ELKANO-scene03-estrellas.blend --python-exit-code 1 \
  --python skills/xu-blender-animations/scripts/render_frames.py -- \
  --output verification/night --frames 1 --width 640 --height 360 --samples 4
```

For a new full hero reference, omit `--frames 144` and choose a fresh output directory to render all 288 frames at the desired reference quality. Then package:

```sh
uv run --with imageio-ffmpeg python scripts/prepare_boat_reference.py hero \
  --frames verification/hero-full --output verification/hero-reference.mp4
uv run --with imageio-ffmpeg python scripts/prepare_boat_reference.py night \
  --image verification/night/000001.png --output verification/night-reference.mp4
uv run --with imageio-ffmpeg python scripts/prepare_boat_reference.py style \
  --video hackathon-result/videos/13-original-hero.mp4 --start 5 --seconds 3 \
  --output verification/hero-style.mp4
```

For the fresh tutorial, the last command must use the **newly approved hero**, not the old video 13. These helpers perform only local rendering/encoding; uploads and paid generation remain separate steps with explicit inputs and budget.
