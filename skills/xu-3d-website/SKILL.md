---
name: xu-3d-website
description: Build cinematic scroll-driven websites through editable Blender scenes, fal video finishing and coded presentation layers. Use for the complete boat-style workflow, its tutorial, or an end-to-end 3D-to-video website; not for unrelated real-time 3D applications.
---

# XU-3D Website

Orchestrate the complete workflow that produced the Elkano boat presentation. Three layers have different jobs: **Blender controls structure and motion; fal generates the cinematic footage; the website controls playback and draws readable overlays.** Do not quietly replace this with a live Three.js scene or describe generated video as a real-time Blender model.

Use the accompanying `$xu-blender-animations`, `$xu-fal` and `$xu-scroll-video-website` skills for their specialized operations. This skill supplies the production sequence and the verified cross-stage decisions.

## Begin with the intended result

Determine the subject, recognizability constraints, branding, camera behavior, motion, scene order, text areas and cost preference from the conversation. Preserve existing authorizations. Missing artistic details usually permit an inexpensive draft; missing paid-spend authorization does not.

When recording a from-scratch tutorial, separate the **existing hackathon result** from the **new tutorial result**. Old output can be shown as evidence or inspiration, but do not secretly reuse it as a freshly generated artifact. Keep the user's requested empty future-result directory empty until real work for that run exists.

Read [the verified boat workflow](references/boat-workflow.md) when explaining how the original was made, choosing an example or reconstructing the tutorial. It distinguishes video 8, video 13 and uploaded-asset descriptions from submitted prompts.

## 1. Build controllable references

Use Blender's bundled Python through the installed executable. Preserve editable parts, camera and subject rigs, packed textures and reproducible source. Start with silhouette, scale and composition; inspect stills before a full animation.

Allocate space for website copy while staging the shot. Avoid cropping a mast or essential logo. Keep the camera truly fixed when asked; the original boat hero used subtle tracking, so its exact camera motion is not a fixed-camera template.

Use meaningful motion at several scales when appropriate: subject translation, restrained secondary movement and a responsive environment. Do not add rocking or cloth motion to an object that should not have it. For the boat, small heave/pitch/roll, breathing sails, a waving flag and water/wake movement all contributed.

Branding must belong to the material: exact supplied symbol, correct proportions and no unwanted white rectangle. Attach textures to deforming surfaces and check them through the timeline.

Render inexpensive beginning/middle/end frames; check framing, contact, scale, logos and exposed scene edges. Then encode a modest complete motion reference. Label held stills, resizing and retiming accurately.

## 2. Prove the visual finish with one short generation

Check the current fal endpoint schema, input-duration limits and price. Use the existing budget and a recorded request manifest. A short first test is cheaper than blindly generating the entire story.

The **turning-point prompt** behind final slide 1 is preserved verbatim in [references/turning-point-prompt.txt](references/turning-point-prompt.txt). Its critical division is:

- `@Video1`: camera, composition, action and recognizable object layout **only**.
- `@Image1`: the exact branding **only**.
- The model may reconstruct photographic materials, lighting, water and fine physical detail rather than preserve the render's finish.

Use concrete physical material descriptions and believable scale. “Higher resolution” is not equivalent to “photorealistic.” An extra CGI identity still may reinforce the crude appearance; include one only as an intentional choice, not an automatic requirement. The original breakthroughs did **not** require a photorealistic still first.

Inspect output and show it for the user's visual judgment. Do not let the agent's taste override explicit approval or imply that one model/prompt guarantees the same pixels. Keep failed takes and identify the changed variable before paying for another attempt.

## 3. Carry approved appearance across scenes

After a hero is approved, use a short clear excerpt as an appearance reference where useful. Keep role assignments explicit: the new scene's video controls action/camera; the hero excerpt controls object identity and finish; the logo controls branding. Do not let the hero's camera override an upward night shot or a stern-view closing.

Count combined input durations. The boat used a three-second hero excerpt; that is a verified example, not a universal prescribed length. Save exact requests, IDs, returned seeds, results and selection decisions. Never resubmit an uncertain paid job without checking its status.

## 4. Build the presentation from approved clips

Preserve originals and create seeking-friendly web encodes. Drive text and graphics from the same scene progress as the video. Coordinate native playback and manual scrolling so they do not compete. Support reverse, skip, reduced motion, delayed metadata, media errors and a valid final frame.

Keep typography, scores, constellation lines and interactive diagrams in HTML/Canvas/SVG. Register overlays to the actual new footage and use matching cover crop transforms. Old star coordinates are not transferable to a regenerated sky.

Use editorial cuts and holds when they serve the story; the boat chest only showed 60% of its generated clip. Prefetch adjacent slides and the next clip instead of loading the whole film. See [production tricks](references/production-tricks.md) for the concrete mechanisms verified in the original code.

Prune an archived result to the requested scope. A slide deck can keep its static product/case slides while excluding platform routes, databases, raw datasets, backend dependencies and platform controls. Record upstream provenance and preserve team credit.

## 5. Verify and package

Build/type-check the actual website, inspect key scenes in a real browser, exercise playback/scroll/reverse/skip, and test the intended viewport sizes. Check media dimensions/duration and decode complete files. Check links and included assets; do not call a folder of code a tested runnable result.

Deliver an intelligible repo: preserved existing result, genuinely separate tutorial output, prompts/evidence, source, media, skills and a concise visual README. Link the production presentation and source repo. Deploy only the authorized site; copying the archive does not authorize overwriting the live hackathon site.

The reference package is `EHxuban11/tutorial-barco`, with `hackathon-result/`, `skills/` and `docs/turning-point-prompt.md`. The original team source is `amarkosmarkos/Elkano_Embat`; production is https://elkano-embat-deck.vercel.app/intro/?present=1 .
