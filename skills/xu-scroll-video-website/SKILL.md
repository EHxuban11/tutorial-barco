---
name: xu-scroll-video-website
description: Turn approved video clips into scroll-driven websites and presentations with synchronized text, navigation and overlays. Use for cinematic clip-based pages like Xuban's Elkano deck; integrates with existing frameworks or a standalone starter.
---

# XU-scroll-video-website

For the complete Blender → cinematic video → website workflow and its verified boat example, use `$xu-3d-website`.

Build the presentation from the user's actual approved clips. The browser plays/seeks video; it does not need to run the Blender model. Use `$xu-blender-animations` for new geometry/motion and `$xu-fal` for generative finishing.

## Inspect the project and media

Follow its framework, routing and deployment instructions. Inspect the existing player before replacing it. Keep scene order, source/poster paths, cut points and text intervals in one configuration file.

Check real video duration, fps, dimensions, orientation and audio. Preserve originals. Make seeking-friendly web copies with frequent keyframes, compatible H.264/yuv420p encoding and faststart. The bundled [media helper](scripts/prepare_media.py) encodes a copy and verifies full decoding. Never upscale silently or label interpolated frames as new rendered detail.

## One timeline owns playback

Use a tall section and a sticky full-screen stage. Derive progress from its current bounding rectangle:

`progress = clamp(-sectionTop / (sectionHeight - viewportHeight), 0, 1)`

Map progress to the actual usable video interval after `loadedmetadata`. Clamp away from an invalid end timestamp. Coalesce seek requests while a seek is in flight; update to the latest desired time after `seeked`. Show a poster while media loads and a useful fallback if it fails.

Play/pause, reverse and skip controls must use the same timeline as manual scrolling. Do not let native video playback and a scroll seeker fight each other. Manual wheel/touch/keyboard interaction should interrupt automatic progression. Keep the last frame visible at a section's end.

Keep captions and product text in HTML. Use Canvas/SVG only for graphics needing it. Match video and overlay crop transforms: for `object-fit: cover`, an SVG using the same source aspect ratio and `preserveAspectRatio="xMidYMid slice"` can align directly. Inspect stars in the **new** clip; do not reuse coordinates from another video. If stars drift, track them or draw a separate stable star layer rather than asserting false alignment.

## Starter and integration

For a new standalone page, copy [assets/scroll-site](assets/scroll-site) and populate `scenes.js` with real clips. It supplies sticky stages, a coalescing seeker, play/pause, previous/next, reduced-motion support and error states. It has no external runtime dependencies. This is a starter, not a finished branded design.

In Next.js/React, adapt the controller to a reusable client component and effect cleanup; do not introduce a separate framework just to use the starter. Reference implementation: `hackathon-result/website/` in this repository, archived from [amarkosmarkos/Elkano_Embat](https://github.com/amarkosmarkos/Elkano_Embat).

## Verify and deliver

Test forward/backward scrolling, rapid seeking, play/pause, next/previous, refresh mid-page, metadata arriving late, failed media and reduced motion. Check narrow and wide viewports, readable text, correct crop alignment, no cropped essential branding and a stable final frame. Use the current browser's supported local-development workflow.

Run the project's relevant build/type checks. Deploy only to the intended authorized site and verify the real public URL; do not claim a local build is deployed. Report which clips and controls were actually tested and any missing generated footage.

See [the delivery checklist](references/delivery.md) for the original workflow's useful constraints.
