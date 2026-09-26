# Concrete production tricks

## Blender

- Build silhouette and composition before tiny detail. The successful hero reference was 800×450, eight Cycles samples, denoised, 288 frames at 24 fps.
- It moved the ship 12 units and camera two units: restrained tracking, not an exact locked camera. Leave the right third for copy and keep the ship recognizable on the left.
- Small heave/pitch/roll plus independently animated sails and flag avoid a frozen subject. The water changes too. These motions fit a sailing ship; apply physical judgment to other subjects.
- Bind wake coordinates to the moving hull. A wake left at the world origin breaks contact and scale.
- Mask logo background into the original sail material and let UVs deform with the cloth.
- Inspect low-resolution shots before long renders. Distinguish a held still from an animated reference and preserve each attempt.

## fal

- Split preservation constraints from reconstruction freedom. The boat prompt preserves recognizable layout/action while replacing CGI finish with real wood, fabric, rope, water, haze and light.
- Specific physical detail beats a vague request for “HD.” Avoid adding constraints that accidentally pin the generated appearance to a crude render.
- Approve an actual result before propagating its appearance. Keep each reference's role explicit and respect the combined duration limit.
- Upload to storage and register in Assets separately when using the API. Save URLs and IDs, and verify the library entries. Reuse a pending job ID instead of paying for a duplicate after a timeout.
- Treat visual causes as hypotheses unless tested. Distance and organic motion may help the boat; the evidence does not establish them as the single reason it succeeded.

## Website

- H.264/yuv420p, faststart, half-second keyframes; originals remain untouched.
- Native playback updates progress/scroll. Manual scroll seeks only when paused. Wheel/touch interrupts playback. Check metadata, readiness and in-flight seeks.
- Reset on scene entry; allow an explicit progress query for reviews. Respect reduced motion.
- Night footage runs at 0.25× to give overlays time. Overlay phases are progress intervals, not independent competing animations.
- Canvas handles many particles. SVG/HTML handle lines and text. Share a 1600×900 coordinate space with the video and matching cover crop; cap Canvas DPR where useful.
- Register star anchors against the actual generated footage. Replacing the background with a fixed image was not an acceptable substitute for the requested alignment correction.
- The chest decelerates into a cut at 60%, holds on the three scrolls, then advances. Generating eight seconds does not require showing all eight seconds.
- Thank-you copy is static HTML so media loading does not delay it.
- Keep navigation width stable. Single arrows operate scene playback; double arrows and keyboard left/right skip sections. Prefetch adjacent routes and only the next clip.
- Remove discarded experiments instead of carrying them as hidden dependencies. The water-button effect and boat zoom transitions were removed; one case-slide zoom entrance remained.

## Recording the tutorial

Show the editable model, raw reference, exact submitted request, returned video, and website layers separately. Preserve failures, timestamps and costs. Disclose held frames, resized inputs, reused appearance excerpts and time spent rendering. Do not promise identical generations or imply the entire final frame came from Blender.
