# Rebuild the boat from scratch: step-by-step guide and prompts

Before the generation step, follow the [file upload walkthrough](fal-upload-walkthrough.md): local files → hosted URLs → ordered model references → saved request ID → downloaded output.

This is a streamlined teaching sequence based on the verified production history. It has not yet been executed as a new clean-room build. The prompts below are newly written for the tutorial; the separately linked historical prompt file contains the exact original Seedance requests.

The explanation to use on camera:

> I directed Astra to build an editable ship and scene references in Blender using Python. I then used Seedance 2.0 on fal.ai to turn those references into cinematic videos. The website plays and scrubs those videos, with text and constellation animations drawn separately in code.

## What counts as starting from scratch

Start a new agent conversation in a new empty project directory. Have Blender installed and fal access ready, but show that the working folder contains no `.blend`, ship-building script, generated ship image or finished video. Supply only your logo and any openly identified historical reference material. Generate all scripts, geometry, renders and videos during this new run. A later scene may reuse the ship and hero video created earlier in this same run; that reuse is part of the demonstrated method.

Do not attach the old 13.mp4 as your style reference or copy the old ship builder into the workspace. Do not give the agent the old project folder as context. Keep this audit outside the rebuild folder. Prepared prose prompts are fine if shown as the recipe. Disclose any time-lapse or pause while rendering/generation completes, and retain unsuccessful attempts rather than silently substituting old outputs.

The historical run used Astra (medium effort) and Blender 5.2.2 LTS. Record the actual model and Blender version used in the new session. If they differ, say so. The tutorial’s principle is code-driven Blender plus reference-conditioned video generation, not a promise that every model/version produces the same pixels.

## 0. Install and check the tools

Install the desktop application from the [official Blender download page](https://www.blender.org/download/), open it once, and note its version. If Blender is already installed, verify that installation rather than reinstalling it. The original run used Blender 5.2.2 LTS; record the version actually used for the new tutorial.

**Do not install Blender MCP as a prerequisite.** The original workflow used Blender’s built-in Python API, `bpy`, executed by the Blender application. No MCP server or Blender add-on was required. Installing a standalone `bpy` package in ordinary Python is not the setup demonstrated here.

On the original Mac, the executable was `/Applications/Blender.app/Contents/MacOS/Blender`. Check the installation and scripting entry point with:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --version
/Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python-exit-code 1 --python-expr "import bpy; print('Blender Python ready:', bpy.app.version_string)"
```

The second command checks that Blender can execute Python; it does not create or save a ship. On Windows or Linux, have the agent locate the installed Blender executable and substitute that path.

Give the coding agent access to the new project folder and terminal. Confirm how it will show you rendered PNGs and open the editable `.blend`. Direct mouse/keyboard control of Blender is optional for this workflow.

Before the video stages, check `ffmpeg -version`, or have the agent document the FFmpeg executable supplied by its chosen tooling. Before the website stage, check `node --version` and `npm --version` and follow the framework’s current supported-version requirements. Before paid generation, confirm fal login/access, the selected model, available credit and the displayed cost. Keep API credentials outside this repository and the screen recording.

Record these versions and run a small rendering check before a long animation. Successful Python startup proves the scripting setup, not render performance or the final artistic result.

## 1. Establish the scene and make the first ship

Tell viewers which part each tool will do: agent writes code; local Blender produces controllable 3D references; fal generates final-looking footage; browser adds interaction. You do not need the hackathon financial dataset or its application to reproduce the visual workflow.

Create an empty folder with subfolders for references, Blender sources, renders, generated videos and the web app. Put your logo in `references/logo.png`. If you choose to add Victoria photographs, identify them as a deliberate improvement to the new tutorial: the historical log supports reading reference pages, not photo-to-3D reconstruction.

Paste this newly written starter prompt:

```text
We are recording a from-scratch tutorial. Work only in this new project folder.
Do not read or reuse any previous Elkano project, ship-building script, .blend,
render, generated image or video.

Create an editable Blender scene of a stylized 16th-century nao inspired by
the Victoria associated with Juan Sebastian Elcano. Use Blender's built-in
Python API through the local Blender executable. Create real 3D geometry;
do not import a prebuilt ship. Save the Python source and an editable .blend.

The recognizable features are a wooden hull, elevated stern and forecastle,
three masts, beige square sails and a triangular lateen mizzen. Use my supplied
logo on the sails and a waving flag. The sail fabric must remain beige around
the mark, with no white rectangular logo background. Preserve logo proportions.

Start with a simple blue ocean and warm daylight. Prioritize the silhouette,
readable branding and camera composition. We will use this as a reference for
video generation, so do not spend hours on tiny surface details.

Use keyframes or shape keys for gentle ship rocking, breathing sails and the
flag. Every frame must be renderable independently. Avoid simulations that
require an external cache. Pack image textures into the .blend.

First render a bow view, a side view and a stern view. Inspect those images and
fix visible geometry, framing and branding problems. Then show me the result
before rendering a full animation. Keep changes and renders versioned.
```

The historical execution pattern was:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --background --python blender/build_ship.py
```

That is a template for the newly generated script, not a command to run the old project. Have the agent detect the executable location on other operating systems. Blender executes `bpy`; ordinary system Python does not replace Blender for scene creation.

**Checkpoint:** open the new `.blend`, orbit the view, select some ship parts and scrub its timeline. Show the render beside the viewport. This demonstrates that an actual editable model exists. A solid-mode viewport may hide image textures; judge the logo in a material preview or render.

## 2. Make one useful Blender hero animation

The historical final hero used a fresh lateral shot, not the earlier One Piece camera flybys. Start directly with that composition:

```text
Using only the ship we just created, make the hero scene in a separate .blend.
A continuous 12-second shot at 24 fps: the ship enters from the left and ends
near center-left. Use a near-side view with a slight three-quarter angle so
the hull and sail logos read clearly. Gentle tracking, no cuts or orbit.
Keep the right third open for website copy. The ship should feel substantial,
with restrained rocking and cloth motion. No text or floating financial data
in the water. Render beginning, middle and end first; inspect framing and sea
edges. Once those are good, render a fast 800x450 preview and encode an MP4.
Save the scene, source script and numbered PNGs.
```

Use the three stills to correct scale, clipping, empty space and an exposed edge of the ocean. Only then render the whole shot. The historical preview used Cycles, eight samples and denoising for this stage. Those are a starting point; adjust if they obscure the geometry or logo.

**Checkpoint:** play the actual preview. Judge whether the action and composition are clear. It need not look like the final generated footage. A render that accidentally crops the sails or moves too fast is a poor reference regardless of finishing model.

## 3. Generate and approve the cinematic hero

Prepare a 1280×720 MP4 upload reference, as the historical workflow did. Keep the original 800×450 render separately. This resize satisfies the chosen upload format; it does not create additional modeled detail. Upload the video and logo through fal’s interface or storage API.

Use **ByteDance Seedance 2.0 Fast, reference-to-video**:

```json
{
  "resolution": "720p",
  "duration": "12",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

The historical endpoint is `bytedance/seedance-2.0/fast/reference-to-video`. Use the exact [turning-point prompt](turning-point-prompt.md), also preserved in [historical Seedance prompts](./historical-seedance-prompts.md), under `seedance-scenes / 01-zarpar-request`. Replace its brand/name references if appropriate. Supply the new Blender clip as Video1 and your logo as Image1. The important instruction is that the video guides composition, timing and vessel layout while the model reconstructs the appearance. These are historical settings: verify the current endpoint schema and price before submitting, within an explicit budget.

For the on-camera explanation, emphasize the division of responsibilities:

> Blender lets me decide where the ship is, how the camera moves and where the text will fit. Seedance is allowed to reinterpret the wood, canvas, water, light and fine detail.

Inspect the whole result, plus beginning/middle/end frames. Check the silhouette, masts, sail marks, flag, camera path and space for copy. If it fails, diagnose whether the problem is in the Blender reference or the generation. Change one relevant thing before trying again. Save the request, output, duration, cost and a brief decision in a manifest.

**Checkpoint:** approve one newly generated hero. This is the tutorial’s equivalent of 13.mp4; the old 13.mp4 is never an input.

Historical difference: you originally generated six scenes in parallel before selecting 13 as the reference. Approving the hero first is a lesson from that experience, not a claim that the weekend followed this exact order.

## 4. Create the remaining Blender scene references

Reuse the newly created ship across separate scene files. For the compact tutorial, demonstrate the night sky. The island approach, revised chest, city and closing are optional extensions. These are independent shots with narrative transitions; do not promise a single uninterrupted physically continuous voyage.

| Shot | Fresh Blender work | Reference duration | Acceptance condition |
|---|---|---|---|
| Island approach | Rough rocky island, shore and foliage; keyframe ship approaching and slowing | 6 s / 144 frames | Boat/island scale and approach clearly readable |
| Night sky | Deck/upward view, branded sails and mast at left, clean dark sky on right | One still held for 4 s | Most of the sky free for overlays; locked framing |
| Revised chest | Small chest on deck; camera approaches; lid hinged; three scrolls; one rises/unfurls | 8 s / 192 frames | Chest is small relative to ship; stages legible |
| Island-city | Simple coastal town/piers and 20–30 distinct varied boats | 6 s / 144 frames | Boats are separate and varied; selected boats readable |
| Closing | Stern view of ship moving into distance, generous sky | 8 s / 192 frames | Ship gets smaller; camera does not approach it |

Scene prompt for the island:

```text
Make a separate six-second Blender scene using our existing ship. It approaches
an island and gradually slows. Place the ship left and the island behind/right.
Block the coast with simple rocky landforms, a sandy cove and foliage. Keep
scale believable and the camera movement gentle. Shift warm daylight toward
late afternoon. Preview three frames before rendering the 144-frame animation
at 800x450, 24 fps. Save all editable sources and the video reference.
```

Scene prompt for the stars:

```text
Make a Blender night composition looking up from the deck. Keep the mast,
rigging and branded sails at the left edge/lower left. Leave the right two
thirds as a deep blue sky with restrained stars. Use moonlit canvas and a
locked camera. Render one clean image. Do not draw constellation lines, a
score, text or a logo in the sky: those will be browser overlays later.
Package the still as a four-second reference MP4. State clearly that it is
a held still, not a fully rendered Blender animation.
```

For the chest, use the actual eight-second staging: establish a large ship and small chest; approach during the first three seconds; open the lid; reveal three scrolls; pause; optionally lift/unroll one. The first historical closed/open two-still method is worth showing as a discarded shortcut, but it need not be repeated in the rebuild.

**Checkpoint:** show each raw reference before its generated version. A held still is legitimate input, but call it a still. If you choose to animate the night shot in Blender instead, label that as a change from the original workflow.

## 5. Carry the new hero’s appearance across scenes

Extract a three-second segment of the newly approved hero where the ship is clear. For each subsequent job provide:

1. Video1: that scene’s new Blender reference.
2. Video2: the new hero’s three-second segment.
3. Image1: the logo.

The preserved prompts are in [historical Seedance prompts](./historical-seedance-prompts.md), under `seedance-reference13`. Their role assignment is the essential teaching point: Video1 describes what happens; Video2 describes the ship’s appearance and finish; Image1 describes the mark. Tell the model not to copy Video2’s side-view camera into a night-deck or stern-view shot.

The historical requests used 720p, 16:9, no audio, and the output duration from the table. Count both reference videos and check current limits/settings in the [fal Fast API](https://fal.ai/models/bytedance/seedance-2.0/fast/reference-to-video/api). Generate one scene first to validate your new hero reference; any additional scenes must fit the approved budget.

The closing is optional extra finishing: historically its final pass used standard `bytedance/seedance-2.0/reference-to-video`, 1080p, `bitrate_mode: high`, and the previous generated closing as the action reference. Show that as an optional additional generation, not a universal requirement. [Standard endpoint documentation](https://fal.ai/models/bytedance/seedance-2.0/reference-to-video/api).

**Checkpoint:** put the generated shots next to the hero and inspect consistency. Shared references improve the instructions you give the model; they do not guarantee exact geometry, branding or continuity. Preserve every take and state which one you selected.

## 6. Build the website around the videos

Use the newly generated MP4s as assets. The scene is a video in the browser, not an exported interactive Blender model. Ask the agent to create a small Next.js site with one reusable scene component and a data file holding media paths, duration/progress intervals and text layers.

```text
Create a new Next.js presentation using only the videos generated in this
project. Make a reusable full-screen scene component with a sticky stage.
Map section scroll progress in [0,1] to video.currentTime. Keep text in HTML,
with entry/exit intervals controlled by the same progress value. Preserve
the right-hand copy area in the hero. Use a navy page background.

Implement one hero scene first. Wait for media metadata before seeking, use
the actual decoded duration, avoid conflicting seek requests, show a poster
before the video loads, and support reduced motion. Test forward and backward
scrolling in a real browser before adding scenes. Then add play/pause and
next/previous controls that stay synchronized with scroll progress.

Keep scene order and media paths in a small configuration file. Do not build
the financial platform; this tutorial demonstrates the visual presentation.
```

The conceptual mapping is:

```text
progress = clamp((scrollY - sectionTop) / (sectionHeight - viewportHeight), 0, 1)
videoTime = progress * videoDuration
```

The finished weekend site also added autoplay on entry, reverse playback and skip controls. For teaching, get manual scroll seeking working first so two controllers do not fight each other.

The historical packaging used the following encoding pattern. Let the agent run it on a *copy* of each new generated video:

```sh
ffmpeg -i generated.mp4 -c:v libx264 -preset slow -crf 23 \
  -g 12 -keyint_min 12 -sc_threshold 0 -pix_fmt yuv420p \
  -movflags +faststart -an web.mp4
```

At the historical 24 fps, this puts a keyframe every half-second. Keep originals untouched. Compare seeking and visual quality after encoding. This recipe is taken from the project’s actual packaging scripts, not a guarantee of identical playback on every device.

**Checkpoint:** scrub with the mouse wheel and trackpad, go backward, refresh at the start, and try a narrow viewport. Check that text does not cover the ship and that the last frame remains visible. Inspect failed media loads and reduced motion once.

## 7. Add the constellation overlay separately

Demonstrate the night video by itself before adding the overlay. This makes clear which tool made which pixels.

```text
Add a separate Canvas/SVG layer over our generated night video. Use a shared
16:9 coordinate space and exactly the same cover scale/crop as the video.
Inspect several frames of this new video, identify stable bright stars and
place constellation vertices on those coordinates. Do not reuse coordinates
from another video. If stars move substantially, tell me and propose tracked
positions or a separately drawn star layer rather than pretending they align.

Use four progress phases: scattered signals; five named constellations;
convergence into an explicitly illustrative score; then our logo traced as
star-linked outlines. Keep all text and numbers in code. Drive the phase
changes from the same progress as the background. Avoid covering the ship.
Show each phase paused and test alignment after resizing.
```

This is a new recreation of an overlay that originally came from the team’s Claude-assisted branch, then was refined by Astra. Credit that distinction if explaining the original project. You can use one agent for the tutorial; say you are consolidating the work into one reproducible session.

**Checkpoint:** pause at each phase; show the matching video/SVG crop; resize without losing alignment. The historical mistake was drawing a second, mismatched star field and then redesigning the scene too aggressively. Fix the alignment rather than unexpectedly changing the visual story.

## 8. Choose the final edit and publish the reproducible record

Build only what the tutorial needs: hero and stars, plus optional island/chest/city/closing. The old island-approach and old harbour were later removed from the main deck; recreating them demonstrates a technique, not necessarily the final edit.

For the chest, the weekend deck ultimately stopped the eight-second output at 60% (about 4.8 seconds), held on the three scrolls and overlaid product labels. It did not show the entire unfurling action in the final main sequence. Show editorial selection as part of the process.

Keep a manifest with one row per attempt: scene, input filenames, Blender source/version, prompt file, model endpoint, request settings, returned request ID, returned seed if provided, cost shown by the service, output filename and selected/rejected reason. A returned seed is useful provenance; do not promise bit-for-bit regeneration.

Run the new app’s build and visually review it in the actual browser. If publishing, deploy this as its own new site and confirm that its media URLs work outside the local machine. The original hackathon presentation was a static Next.js export on Vercel, but the financial platform and its deployment are unnecessary here.

The deliverable viewers should be able to follow contains the new conversation/prompts, newly generated Blender scripts, editable scene, raw reference renders, generation settings, selected output clips and website source. A downloaded old project demonstrates replay; this recording is intended to demonstrate fresh creation.

## What to skip from the weekend

Skip the initial financial-data HTML sea, the two One Piece camera studies, Neta/Dreamina/BytePlus account detours, poster creation, company still-image generation, water-to-button experiment and discarded harbour zooms. Explain that they existed if discussing the history, but they are not prerequisites for this pipeline. Do not call the whole process one prompt or an upscale. Do not promise the same visual result, a fixed number of attempts, or a fixed total cost.

## Related files

- [Historical workflow](./how-it-was-made.md)
- [Exact historical Seedance prompts](./historical-seedance-prompts.md)
- [Copy-and-paste prompt sequence](../prompts/README.md)

This guide has not yet been validated by a fresh end-to-end run. The original ship, videos and runnable website are archived in [hackathon-result/](../hackathon-result/). See [the verification limits](reproducibility.md).
