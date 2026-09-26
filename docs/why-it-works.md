# Why the boat and the presentation work

These findings separate directly observed implementation from visual interpretation. The audit did not run new generations or test isolated causes of visual quality.

## The visible result is three different systems

**Blender provides controllable structure.** The agent wrote Python to create editable hulls, masts, sails, ropes, flags, cameras and scene layouts. Gentle ship pitch/roll, cloth shape keys and the ocean supplied motion references. This was not a downloaded photorealistic ship and did not require Blender MCP.

**Seedance rebuilds the photographic appearance.** The turning-point prompt gives the model permission to replace the simple render's finish while preserving its recognizable layout and action. Wood grain, caulked seams, cloth translucency, rope tension, foam, spray and haze are specified as physical phenomena. The finished video is not merely a sharpened Blender export.

**The website supplies readable storytelling.** Text, particles, constellation lines, the score and the large EMBAT star symbol are separately coded layers. Their typography stays sharp and their timing remains editable without paying for another video.

## Blender details that mattered

- The final hero was a new lateral scene. The earlier One Piece-inspired camera studies were experiments, not prerequisites for reproducing slide 1.
- The hero source has 288 frames at 24 fps, rendered at 800×450, eight Cycles samples and denoising. Upload preparation resized it to 1280×720; the resize did not add modeled detail.
- The ship travels 12 Blender units while the camera travels two. It is **almost fixed, with subtle tracking**, rather than mathematically stationary.
- The source animates small heave, pitch and roll, plus sails and flags. The Ocean modifier supplies a changing surface. Wake coordinates follow the moving ship rather than remaining attached to the world origin.
- The ship remains near center-left at the end, leaving the right third for copy. Scene composition was designed for a presentation, not only for a standalone film frame.
- The logo's white background is masked away, exposing beige sail material. The texture deforms with the cloth; the symbol is not a floating overlay.
- Night and harbour began as held stills, and the first chest used two poses. The revised chest and island-city later became genuine animated Blender references. A tutorial should say which kind each input is.

The boat's organic motion, transmitted light through sails and constantly changing water likely help the result feel alive. Distance and atmospheric depth may also conceal fine modeling limitations. These are plausible visual contributors, **not proven causal explanations**. Do not present a new photorealistic-image-first requirement as the historical method.

## Generation decisions

The first preserved cinematic test (video 8) was four seconds at 720p using Seedance 2.0 Fast. Xuban loved it even though the assistant's review was overly negative. Human approval is a production decision; the agent's taste is not an objective quality measurement.

Video 13 was generated independently from its Blender clip and logo. It did not use video 8 as an appearance reference. Xuban later explicitly rejected using 8 and chose **13 for all subsequent scenes**.

Those later requests assign separate roles: `@Video1` for the new shot's action, `@Video2` for a three-second extract of the approved hero, and `@Image1` for the exact mark. The prompt warns against copying the hero's side-view camera into a different scene.

The final closing, video 28, is a second-generation refinement: the previous generated closing plus the hero extract, through standard Seedance 2.0 at 1080p/high bitrate. It is not a direct fresh Blender render. No preserved production request uses Seedance 2.5.

## Website details worth teaching

The archived code retains the actual mechanisms:

- **Coordinated playback:** `Escena.tsx` lets native video playback update page progress; while paused, manual scrolling seeks the video. Wheel/touch input interrupts playback. The two modes do not continually fight over time.
- **Seek restraint:** metadata/readiness checks, `v.seeking` guards and small time tolerances avoid repeated overlapping seeks. The end is clamped short of an invalid timestamp.
- **Seeking-friendly files:** H.264, yuv420p, faststart and a GOP of 12 at 24 fps place a keyframe every half-second.
- **Entry behavior:** each video resets on entry and autoplays unless reduced motion or an explicit `?p=` progress is requested. Development builds warm slide routes; production prefetches neighbors and only the next clip, respecting data saving.
- **Readable pacing:** the night scene runs at 0.25×. Longer scroll distance gives its four visual phases room to breathe.
- **Matching crop coordinates:** the star layer uses a 1600×900 space. Canvas uses cover scaling and centered offsets; SVG uses `xMidYMid slice`, matching the video's cover crop.
- **Real star alignment:** constellation anchors were registered to stars in the new `estrellas-ref13.mp4`, rather than retaining coordinates from an older clip. The source records checks across 40 samples.
- **Efficient layers:** many small particles are drawn on Canvas; semantic labels and constellation geometry are SVG/HTML. Seeded particle placement keeps the composition stable.
- **Editorial selection:** the chest stops at 60% of its generated clip. A speed ramp slows the last 12% toward 0.12×, then the frame holds while labels identify the three scrolls. The audience does not see every generated frame.
- **Stable closing:** thank-you copy is present independently of video playback so it is not delayed by a decoder or transition.
- **Predictable controls:** single arrows play/reverse scene motion; double arrows skip sections; keyboard left/right skip slides. The control widget stays the same width.

## Iterations that should not become tutorial requirements

The six-scene batch came before the common hero reference historically. Approving one hero first is a sensible streamlined teaching order, but label it as an improvement to the process.

An unwanted fixed-sky redesign was rolled back; the user's request was to align the existing overlay to the video. The initial giant empty chest was rebuilt at sensible scale. A water-to-button effect and boat-to-company zoom transitions were removed. The island approach and old harbour remain archived but are omitted from the main slide order.

## Credit and evidence

The main asset work was in the original Astra session. The initial SkyStory implementation came from Markos's branch: commits `34aee47` and `cdd8780` credit Markos and Claude Opus 5; Astra integrated it in merge `1b5c5c5` and subsequent revisions. The deck is team work.

See [source provenance](../hackathon-result/provenance.json), [all recovered fal requests](audit/fal-prompts.md) and [the original user prompts](audit/user-prompts.md).
