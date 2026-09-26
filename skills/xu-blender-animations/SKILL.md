---
name: xu-blender-animations
description: Build and revise editable Blender models, branded scenes, and camera-controlled animation references using Blender Python. Use for procedural 3D animation work and Blender-to-video workflows.
---

# XU-blender-animations

For the complete Blender → cinematic video → website workflow and its verified boat example, use `$xu-3d-website`.

Deliver editable geometry, Python source, a reproducible `.blend`, inspected stills and a verified animation. Blender supplies layout, motion and camera; use `$xu-fal` for generative photographic finishing and `$xu-scroll-video-website` for the final presentation.

## Establish the scene

Read workspace instructions and inspect existing files before rebuilding. Save new shots under separate filenames. Distinguish exact reconstruction from artistic interpretation; identify visual references and approximate dimensions/livery.

Take camera instructions literally. **Fixed means no pan, tilt, translation, tracking, animated constraints or zoom.** Move the subject instead. Do not quietly turn a fixed shot into a tracking shot.

Reuse supplied logos as actual SVG outlines or mapped textures. Preserve proportions, lettering and orientation; avoid unwanted rectangular backgrounds. Parent branding and fittings to the appropriate moving part, and inspect both sides for mirroring.

## Execute with Blender Python

Check the installed executable and version. On macOS, for example:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --version
/Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup \
  --python-exit-code 1 --python blender/build_scene.py
```

Use Blender's bundled `bpy`; Blender MCP and standalone system-Python `bpy` are not prerequisites. Inspect RNA properties when version differences cause errors. Read [local notes](references/local-notes.md) for verified 5.2 behavior and geometry pitfalls.

Name collections for the subject, rig, setting, cameras/lights and branding. Give moving assemblies clear roots. Prefer independently evaluable keyframes, drivers or shape keys; pack textures and account for external simulation caches.

For articulated subjects, preserve rigid part lengths and common junction positions. Test alignment through the animation, especially on curves. A visual rig is not automatically an engineering simulation.

## Inspect before rendering the whole shot

Render useful views plus the beginning/middle/end. Inspect silhouette, framing, readable logos, joins, wheel/ground or hull/water contact, and exposed scene edges. Fix visible faults before a full render and retain meaningful attempts.

Render an economical reference first, then encode and fully decode the resulting MP4. Verify actual duration, fps and dimensions; inspect the movement. Label held stills, retiming and resizing honestly. Resizing adds no geometric detail. Do not claim to have watched playback when only individual frames were inspected.

The bundled [render helper](scripts/render_frames.py) renders a loaded `.blend` without modifying its source. Invoke it after the scene path through Blender, followed by `-- --help` for options.

For night scenes, preserve the requested open sky area and keep stars fixed in world space when the camera is fixed. Leave text, constellation lines and interactive diagrams for the website layer unless the user explicitly wants them baked into video.

Deliver source, `.blend`, selected stills, reference video and the actual validation record. Open a separate Blender instance when needed to protect an unsaved session.

The boat example lives in this repository under `hackathon-result/blender/`. It is an example, not a set of assets to silently reuse in a claimed from-scratch build.
