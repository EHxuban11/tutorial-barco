# The turning-point prompt: the boat in slide 1

This is the actual request that generated **video 13, Zarpar**, the boat used by the production presentation's first slide. It is not the descriptive caption shown for an uploaded clip in fal Assets.

| Evidence | Value |
| --- | --- |
| Saved request | `video/seedance-scenes/01-zarpar-request.json` in the original hackathon workspace |
| Request saved | **19 September 2026, 14:53:34 CEST** |
| Result receipt saved | 19 September 2026, 14:59:21 CEST |
| Video downloaded | **19 September 2026, 14:59:24 CEST** |
| Request ID | `01a0b9ba-af4a-7c40-b631-2f85de789dd1` |
| Model | `bytedance/seedance-2.0/fast/reference-to-video` |
| Output request | 12 seconds, 720p, 16:9, audio off |
| Actual output | 12.04 seconds, 289 frames at 24 fps |
| Input video | Blender's lateral scene, packaged as `01-barco-largo.mp4` |
| Input image | EMBAT sail symbol, `03-logo-embat-velas.jpg` |
| Photographic appearance reference | **None** |
| Later website file | `zarpar-seedance.mp4`, a seeking-friendly encode of video 13 |

Source times above are preserved file timestamps, corroborated by the main session's output at line 2903. The user approved the six-scene batch at 14:49:45; that is earlier than the actual saved request.

**The earlier breakthrough was video 8.** At 14:11:22, after that four-second test, Xuban approved it enthusiastically. Video 13 was produced later and explicitly selected as the common appearance reference at 17:09. Both matter; they are different generations.

## Before and after

| Blender motion/layout reference | Generated video 13 |
| --- | --- |
| ![Blender reference](media/blender-hero.jpg) | ![Generated hero](media/seedance-hero.jpg) |

[Blender input MP4](../hackathon-result/references/01-barco-largo.mp4) · [Original video 13](../hackathon-result/videos/13-original-hero.mp4) · [Live slide 1](https://elkano-embat-deck.vercel.app/escena/1/?present=1)

## Exact submitted prompt

```text
A shot from a lavish live-action historical ocean adventure feature film, photographed on location with a full-size working 16th-century sailing ship. Use @Video1 ONLY as a camera-motion, composition and vessel-layout guide. Completely replace its simple computer-rendered appearance with convincing live-action photographic realism. This is NOT an upscale of the render and NOT an animated film. A substantial ocean-going nao Victoria inspired by Juan Sebastian Elcano: three masts, high stern, deep weathered wooden hull, square beige canvas sails and a triangular lateen mizzen. Preserve this recognizable vessel layout, but reconstruct materials and fine physical detail as real objects. Water-darkened oak planks with fine irregular grain, caulked seams, subtle salt streaks, individually tensioned hemp rigging and heavy stitched canvas glowing translucently in backlight. Real seawater with irregular foam, fine spray, natural blue-green swells and atmospheric haze. Physically credible full-size scale and inertia, never a miniature. Restrained filmic contrast, natural highlight roll-off, 35mm cinema lens and realistic exposure. @Image1 is a branding reference ONLY: reproduce this exact navy geometric Embat symbol as ink printed directly on the beige sails in the positions seen in @Video1; ignore the white background of the logo image. Keep the small Embat flag. Do not transform the logo into another symbol. No cartoon, no game-engine appearance, no toy ship, no plastic wood, no smooth synthetic sails, no neon water, no artificial wire-like wakes, no added captions or music. Preserve empty space for website text but do not generate text. Prioritize live-action cinematography and believable physical materials over matching the source render's lighting or shading. One continuous lateral shot, no cuts, no orbit. The ship enters from the left and sails slowly rightwards, ending near the center-left. Keep the right third unobstructed with sea and sky. Follow the full twelve-second camera path and timing of the reference. Warm natural daylight, subtle tracking, heavy sails gently breathing, realistic bow wave.
```

## What the prompt changed

The earlier, less successful video 7 asked to improve rendering while preserving the source very closely. The successful requests separate **what must stay**—recognizable vessel, camera/action, composition and logo—from **what may be rebuilt**—materials, lighting, water and fine physical detail.

This is evidence for a working recipe, not proof that one phrase alone caused the result. The first success and this hero both used a Blender clip plus a logo; a photorealistic still was not a prerequisite in the historical workflow.

The long “A large, traditional wooden sailing ship…” paragraph belongs to the uploaded **three-second extract of video 13**, `13-referencia-estilo-3s.mp4`. It describes an already-created asset. Later shots used that extract as `@Video2` for appearance consistency.

For every recovered request, see [the fal prompt archive](audit/fal-prompts.md). For original user instructions and revisions, see [the conversation prompt archive](audit/user-prompts.md).
