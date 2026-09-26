# The hackathon result

This is the existing result that motivated the tutorial, preserved separately from the future tutorial rebuild.

**[Watch the production presentation](https://elkano-embat-deck.vercel.app/intro/?present=1)** · [Original public source](https://github.com/amarkosmarkos/Elkano_Embat)

| Folder | Contents |
| --- | --- |
| `website/` | Runnable slides-only adaptation of the original Next.js deck |
| `videos/` | Final presentation clips/posters, plus original videos 8 and 13 |
| `blender/` | Original editable scenes, construction scripts and packed brand assets |
| `references/` | The Blender clips supplied to the first breakthrough and the final slide-1 generation |

The production website is unchanged. This archived copy removes platform routes, backend dependencies, company datasets, external platform controls and product-demo mode. Static product and case-study slides remain because they are part of the presentation.

## Run the slides

```sh
cd hackathon-result/website
npm ci
npm run dev
```

Open `http://localhost:4323/intro/?present=1`. `npm run build` produces `website/out/`; `npm run preview` serves that static export. Videos are copied from the canonical `videos/` directory before dev/build, so there is only one tracked media copy.

## Video map

| Packaged video | Original number | Role |
| --- | --- | --- |
| `08-first-breakthrough.mp4` | 8 | First explicitly celebrated cinematic test; 4 seconds requested |
| `13-original-hero.mp4` | 13 | Original generated file behind production slide 1 |
| `zarpar-seedance.mp4` | 13 | Web encode used by slide 1 |
| `isla-ref13.mp4` | 22 | Preserved island approach, outside the main slide order |
| `estrellas-ref13.mp4` | 23 | Starry background with separately coded overlays |
| `cofre-ref13.mp4` | 24 | Chest scene; presentation stops at 60% |
| `isla-ciudad-ref13.mp4` | 25 | Island-city / company-case scene |
| `puerto-seedance.mp4` | 17 | Older harbour, preserved outside the main slide order |
| `cierre-hq.mp4` | 28 | Final 1080p closing refinement |

Most files are the original web encodes, not untouched model outputs. The two explicitly numbered originals preserve the important 8/13 distinction.

All 13 packaged MP4s were fully decoded during the audit. [media-manifest.json](media-manifest.json) records their dimensions, durations, frame counts and SHA-256 hashes.

## Blender archive

Open `blender/ELKANO-scene01-zarpar.blend` for the slide-1 layout, or `ELKANO-v6-ocean.blend` for its source ship/ocean scene. The directory includes the earlier camera studies and later scene revisions. Textures are packed in the historical `.blend` files.

The Python files are historical source. Some encoders retain the old monorepo output layout; inspect their paths before running them. They are evidence and editable starting points, not a claim that the old folder layout is reproduced unchanged. The `scene_data.js` file supports the earliest procedural builder; it is not the financial platform or its raw dataset.

Provenance and exact upstream commit: [provenance.json](provenance.json). The central request is documented in [The turning-point prompt](../docs/turning-point-prompt.md).
