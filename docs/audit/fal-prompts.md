# Every recovered fal request

15 requests: 14 video generations and one poster upscale. Thirteen video jobs have complete saved request/result receipts. The earlier video 7 has its exact prompt and output recovered from Assets, but its full original settings are not claimed.

Assets descriptions for **uploaded files** are not generation prompts. The “A large, traditional wooden sailing ship…” paragraph describes the later three-second extract of video 13.

## earlier-ui-attempt

Video: 7 · Model: `fal-ai/seedance-2/reference-to-video` · Evidence: Assets response metadata plus conversation; full original input settings not recovered

Request ID: `01a0b975-6ba2-75a3-9622-59916000fc43`

```json
{}
```

```text
Recreate @Video1 as a premium cinematic ship shot with more detailed wood grain, realistic beige woven sails, natural daylight and convincing blue ocean waves. Preserve the exact original camera path, framing, ship silhouette, three masts, sail arrangement and motion. The ship is inspired by Juan Sebastian Elcano's nao Victoria, not a fantasy pirate ship. @Image1 is the exact navy Embat symbol: preserve its geometry and placement on every sail, printed directly on beige cloth with no white rectangle. Keep the existing Embat wordmark flag unchanged and readable. Do not invent letters or replace the symbols. Improve rendering realism and material detail without redesigning the ship. A single continuous five-second shot following the reference. No additional objects, no people, no captions, no cuts, no music or audio.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab0bb6/wVlAroY2n3n2Buoui1fye_video.mp4"}}`

## fal-cinematic-test

Video: 8 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0b98c-f007-79d1-9f6c-2808cb7021b9`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/-TtHn8asX5ngrM8ITXaeM_01-video-prueba-5s.mp4"
  ],
  "resolution": "720p",
  "duration": "4",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
A shot from a lavish live-action historical ocean adventure feature film, photographed on location with a full-size working 16th-century sailing ship. Use @Video1 ONLY as a camera-motion and vessel-layout guide. Completely replace its simple computer-rendered appearance with convincing live-action photographic realism. This is NOT an upscale of the render and NOT an animated film. A substantial ocean-going nao Victoria inspired by Juan Sebastian Elcano: three masts, high stern, deep weathered wooden hull, square beige canvas sails and a triangular lateen mizzen. Preserve this recognizable vessel layout, but reconstruct materials and fine physical detail as real objects. Water-darkened oak planks with fine irregular grain, caulked seams, subtle salt streaks, individually tensioned hemp rigging and heavy stitched canvas glowing translucently in backlight. The massive hull displaces real seawater with a turbulent bow wave, irregular white foam, fine spray and a broad wake. Long blue-green ocean swells, distant atmospheric haze, warm late-afternoon sunlight breaking through layered maritime clouds, cool shaded hull, restrained filmic contrast and natural highlight roll-off. Physically credible scale and inertia, not a miniature. Smooth continuous tracking camera following the reference movement, 35mm cinema lens, realistic exposure and restrained motion blur, four seconds without cuts. @Image1 is a branding reference ONLY: reproduce this exact navy geometric Embat symbol as ink printed directly on the beige sails in the positions seen in @Video1; ignore the white background of the logo image. Keep the small Embat flag. Do not transform the logo into another symbol. No cartoon, no game-engine appearance, no toy ship, no plastic wood, no smooth synthetic sails, no neon water, no artificial wire-like wakes, no added captions, no music. Prioritize live-action cinematography and believable physical materials over matching the source render's lighting or shading.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab0c4f/Kr6sSY08ObeO9P1P3GLMu_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 2297758}, "seed": 810467706}`

## 01-zarpar

Video: 13 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0b9ba-af4a-7c40-b631-2f85de789dd1`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0d40/yIkrAfcMpRWBm-aqoeRrK_01-barco-largo.mp4"
  ],
  "resolution": "720p",
  "duration": "12",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
A shot from a lavish live-action historical ocean adventure feature film, photographed on location with a full-size working 16th-century sailing ship. Use @Video1 ONLY as a camera-motion, composition and vessel-layout guide. Completely replace its simple computer-rendered appearance with convincing live-action photographic realism. This is NOT an upscale of the render and NOT an animated film. A substantial ocean-going nao Victoria inspired by Juan Sebastian Elcano: three masts, high stern, deep weathered wooden hull, square beige canvas sails and a triangular lateen mizzen. Preserve this recognizable vessel layout, but reconstruct materials and fine physical detail as real objects. Water-darkened oak planks with fine irregular grain, caulked seams, subtle salt streaks, individually tensioned hemp rigging and heavy stitched canvas glowing translucently in backlight. Real seawater with irregular foam, fine spray, natural blue-green swells and atmospheric haze. Physically credible full-size scale and inertia, never a miniature. Restrained filmic contrast, natural highlight roll-off, 35mm cinema lens and realistic exposure. @Image1 is a branding reference ONLY: reproduce this exact navy geometric Embat symbol as ink printed directly on the beige sails in the positions seen in @Video1; ignore the white background of the logo image. Keep the small Embat flag. Do not transform the logo into another symbol. No cartoon, no game-engine appearance, no toy ship, no plastic wood, no smooth synthetic sails, no neon water, no artificial wire-like wakes, no added captions or music. Preserve empty space for website text but do not generate text. Prioritize live-action cinematography and believable physical materials over matching the source render's lighting or shading. One continuous lateral shot, no cuts, no orbit. The ship enters from the left and sails slowly rightwards, ending near the center-left. Keep the right third unobstructed with sea and sky. Follow the full twelve-second camera path and timing of the reference. Warm natural daylight, subtle tracking, heavy sails gently breathing, realistic bow wave.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab0d83/5fNb4SEQ6lECtw_ns6bnp_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 4467246}, "seed": 1746021812}`

## 02-isla

Video: 14 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0b9ba-af49-7261-94c8-b596ee086a77`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0d40/vOj-N8d85Y4XSaO6Au_Wh_02-isla.mp4"
  ],
  "resolution": "720p",
  "duration": "6",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
A shot from a lavish live-action historical ocean adventure feature film, photographed on location with a full-size working 16th-century sailing ship. Use @Video1 ONLY as a camera-motion, composition and vessel-layout guide. Completely replace its simple computer-rendered appearance with convincing live-action photographic realism. This is NOT an upscale of the render and NOT an animated film. A substantial ocean-going nao Victoria inspired by Juan Sebastian Elcano: three masts, high stern, deep weathered wooden hull, square beige canvas sails and a triangular lateen mizzen. Preserve this recognizable vessel layout, but reconstruct materials and fine physical detail as real objects. Water-darkened oak planks with fine irregular grain, caulked seams, subtle salt streaks, individually tensioned hemp rigging and heavy stitched canvas glowing translucently in backlight. Real seawater with irregular foam, fine spray, natural blue-green swells and atmospheric haze. Physically credible full-size scale and inertia, never a miniature. Restrained filmic contrast, natural highlight roll-off, 35mm cinema lens and realistic exposure. @Image1 is a branding reference ONLY: reproduce this exact navy geometric Embat symbol as ink printed directly on the beige sails in the positions seen in @Video1; ignore the white background of the logo image. Keep the small Embat flag. Do not transform the logo into another symbol. No cartoon, no game-engine appearance, no toy ship, no plastic wood, no smooth synthetic sails, no neon water, no artificial wire-like wakes, no added captions or music. Preserve empty space for website text but do not generate text. Prioritize live-action cinematography and believable physical materials over matching the source render's lighting or shading. One continuous six-second shot. The same ship approaches a beautiful uninhabited island and slows almost to a stop. Replace the simple island blobs with real eroded coastal rock, sandy shore and dense coastal greenery, keeping its location and scale. Gradual transition from daylight to warm sunset. Match the reference framing and approach. No camera cuts.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab0d7f/ChVHcy_Ncnx1JRwQt7xiw_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 2003866}, "seed": 1955724869}`

## 03-estrellas

Video: 15 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0b9ba-af41-7160-9d38-e52d231e21c5`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0d40/Q1jhVOawMazDHvz2brvWy_03-estrellas.mp4"
  ],
  "resolution": "720p",
  "duration": "4",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
A shot from a lavish live-action historical ocean adventure feature film, photographed on location with a full-size working 16th-century sailing ship. Use @Video1 ONLY as a camera-motion, composition and vessel-layout guide. Completely replace its simple computer-rendered appearance with convincing live-action photographic realism. This is NOT an upscale of the render and NOT an animated film. A substantial ocean-going nao Victoria inspired by Juan Sebastian Elcano: three masts, high stern, deep weathered wooden hull, square beige canvas sails and a triangular lateen mizzen. Preserve this recognizable vessel layout, but reconstruct materials and fine physical detail as real objects. Water-darkened oak planks with fine irregular grain, caulked seams, subtle salt streaks, individually tensioned hemp rigging and heavy stitched canvas glowing translucently in backlight. Real seawater with irregular foam, fine spray, natural blue-green swells and atmospheric haze. Physically credible full-size scale and inertia, never a miniature. Restrained filmic contrast, natural highlight roll-off, 35mm cinema lens and realistic exposure. @Image1 is a branding reference ONLY: reproduce this exact navy geometric Embat symbol as ink printed directly on the beige sails in the positions seen in @Video1; ignore the white background of the logo image. Keep the small Embat flag. Do not transform the logo into another symbol. No cartoon, no game-engine appearance, no toy ship, no plastic wood, no smooth synthetic sails, no neon water, no artificial wire-like wakes, no added captions or music. Preserve empty space for website text but do not generate text. Prioritize live-action cinematography and believable physical materials over matching the source render's lighting or shading. A quiet four-second view looking up from the deck at night. Keep mast, branded canvas and rigging along the left edge and lower left; leave the right two thirds as clear deep navy night sky with restrained, realistic stars. Gentle fabric movement only, locked camera, no cuts. Soft moonlit canvas and rich timber. No large moon, no drawn constellations, no lines, no numbers, no celestial text.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab0d7d/RcVGM6sIumf4IZGnuj9cY_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 775915}, "seed": 991580445}`

## 04-cofre

Video: 16 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0b9ba-af3f-7383-992d-7f4c391b373c`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0d40/_xl7R3vgKnyTSaRWohP9D_04-cofre.mp4"
  ],
  "resolution": "720p",
  "duration": "6",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
A shot from a lavish live-action historical ocean adventure feature film, photographed on location with a full-size working 16th-century sailing ship. Use @Video1 ONLY as a camera-motion, composition and vessel-layout guide. Completely replace its simple computer-rendered appearance with convincing live-action photographic realism. This is NOT an upscale of the render and NOT an animated film. A substantial ocean-going nao Victoria inspired by Juan Sebastian Elcano: three masts, high stern, deep weathered wooden hull, square beige canvas sails and a triangular lateen mizzen. Preserve this recognizable vessel layout, but reconstruct materials and fine physical detail as real objects. Water-darkened oak planks with fine irregular grain, caulked seams, subtle salt streaks, individually tensioned hemp rigging and heavy stitched canvas glowing translucently in backlight. Real seawater with irregular foam, fine spray, natural blue-green swells and atmospheric haze. Physically credible full-size scale and inertia, never a miniature. Restrained filmic contrast, natural highlight roll-off, 35mm cinema lens and realistic exposure. @Image1 is a branding reference ONLY: reproduce this exact navy geometric Embat symbol as ink printed directly on the beige sails in the positions seen in @Video1; ignore the white background of the logo image. Keep the small Embat flag. Do not transform the logo into another symbol. No cartoon, no game-engine appearance, no toy ship, no plastic wood, no smooth synthetic sails, no neon water, no artificial wire-like wakes, no added captions or music. Preserve empty space for website text but do not generate text. Prioritize live-action cinematography and believable physical materials over matching the source render's lighting or shading. A six-second locked-camera close-up on the deck of the same ship. A substantial old oak chest with forged iron straps starts closed. The reference jumps from a closed to an open lid as a storyboard cue: instead create ONE smooth physically hinged lid-opening motion between seconds 2 and 4, without cuts, morphing or dissolves. A warm lantern illuminates rich oak grain, realistic iron and hemp ropes. A restrained warm golden glow emerges from inside the opened chest. No people, no hands, no floating coins, no cards. Preserve chest placement at center-left and leave right side available for website overlays.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab0d7a/GRrDq4gdL_CkbIGbEFocy_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 945186}, "seed": 2052108070}`

## 05-puerto

Video: 17 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0b9ba-af47-7492-a55a-a94f7b057c34`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0d40/1E3KNqC06oE7nO1aLYpcI_05-puerto.mp4"
  ],
  "resolution": "720p",
  "duration": "4",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
A shot from a lavish live-action historical ocean adventure feature film, photographed on location with a full-size working 16th-century sailing ship. Use @Video1 ONLY as a camera-motion, composition and vessel-layout guide. Completely replace its simple computer-rendered appearance with convincing live-action photographic realism. This is NOT an upscale of the render and NOT an animated film. A substantial ocean-going nao Victoria inspired by Juan Sebastian Elcano: three masts, high stern, deep weathered wooden hull, square beige canvas sails and a triangular lateen mizzen. Preserve this recognizable vessel layout, but reconstruct materials and fine physical detail as real objects. Water-darkened oak planks with fine irregular grain, caulked seams, subtle salt streaks, individually tensioned hemp rigging and heavy stitched canvas glowing translucently in backlight. Real seawater with irregular foam, fine spray, natural blue-green swells and atmospheric haze. Physically credible full-size scale and inertia, never a miniature. Restrained filmic contrast, natural highlight roll-off, 35mm cinema lens and realistic exposure. @Image1 is a branding reference ONLY: reproduce this exact navy geometric Embat symbol as ink printed directly on the beige sails in the positions seen in @Video1; ignore the white background of the logo image. Keep the small Embat flag. Do not transform the logo into another symbol. No cartoon, no game-engine appearance, no toy ship, no plastic wood, no smooth synthetic sails, no neon water, no artificial wire-like wakes, no added captions or music. Preserve empty space for website text but do not generate text. Prioritize live-action cinematography and believable physical materials over matching the source render's lighting or shading. Four-second calm dawn harbor establishing shot, camera almost locked. The same ship is alongside a timber pier at left. Replace the blockout buildings with a convincing early-sixteenth-century Iberian port: warm limestone warehouses, clay roofs and a modest watchtower, weathered wooden piles and still blue water with gentle reflections. Preserve reference arrangement, with the ship on left and port behind it. No modern cranes, no motorboats, no city signs. No cuts.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab0d76/4FVkg4hVHx1OUSLkPvDVG_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 1415406}, "seed": 825136838}`

## 06-cierre

Video: 18 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0b9ba-af51-7c13-950b-7572983955f3`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0d40/MRFyNMEAkaVyshZcVOitW_06-cierre.mp4"
  ],
  "resolution": "720p",
  "duration": "8",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
A shot from a lavish live-action historical ocean adventure feature film, photographed on location with a full-size working 16th-century sailing ship. Use @Video1 ONLY as a camera-motion, composition and vessel-layout guide. Completely replace its simple computer-rendered appearance with convincing live-action photographic realism. This is NOT an upscale of the render and NOT an animated film. A substantial ocean-going nao Victoria inspired by Juan Sebastian Elcano: three masts, high stern, deep weathered wooden hull, square beige canvas sails and a triangular lateen mizzen. Preserve this recognizable vessel layout, but reconstruct materials and fine physical detail as real objects. Water-darkened oak planks with fine irregular grain, caulked seams, subtle salt streaks, individually tensioned hemp rigging and heavy stitched canvas glowing translucently in backlight. Real seawater with irregular foam, fine spray, natural blue-green swells and atmospheric haze. Physically credible full-size scale and inertia, never a miniature. Restrained filmic contrast, natural highlight roll-off, 35mm cinema lens and realistic exposure. @Image1 is a branding reference ONLY: reproduce this exact navy geometric Embat symbol as ink printed directly on the beige sails in the positions seen in @Video1; ignore the white background of the logo image. Keep the small Embat flag. Do not transform the logo into another symbol. No cartoon, no game-engine appearance, no toy ship, no plastic wood, no smooth synthetic sails, no neon water, no artificial wire-like wakes, no added captions or music. Preserve empty space for website text but do not generate text. Prioritize live-action cinematography and believable physical materials over matching the source render's lighting or shading. One continuous eight-second farewell shot from behind the same ship. It sails slowly away toward the open horizon and becomes smaller, exactly following the reference trajectory. Vast sky above with warm sunset near the horizon, blue-gray seawater, gentle broad wake that fades naturally. Keep the upper half clean for closing credits but generate no text. Locked camera, no orbit, no cuts, no fade to black. Finish with a stable beautiful frame of the distant ship.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab0d77/UEjrrKpQJ9Yo9YkNv9mKp_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 2175736}, "seed": 261138791}`

## 10-isla

Video: 22 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0ba3d-8201-77c0-b68b-3cd9b983b8a1`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0d40/vOj-N8d85Y4XSaO6Au_Wh_02-isla.mp4",
    "https://v3b.fal.media/files/b/0aab10a4/a3Cy5d5rk-l2428pTAWJB_13-referencia-estilo-3s.mp4"
  ],
  "resolution": "720p",
  "duration": "6",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
Create a convincing live-action shot for a cinematic historical ocean adventure. REFERENCE ROLES: @Video2 is the approved definitive appearance of our ship and the visual finish to match across this entire film. Preserve its recognizable vessel, three masts, high stern, hull proportions, rigging, canvas colors, wood treatment and Embat branding. @Video1 is a rough Blender storyboard ONLY for scene layout, broad camera path and action order. Do not copy its primitive shapes, flat materials, mechanical motion or toy-like appearance. Reconstruct the scenery and props as real full-scale objects. @Image1 is the exact navy Embat symbol: print it directly on beige canvas without a white rectangular background, as in @Video2. Keep the Embat flag recognizable. For the main vessel, prioritize fidelity to @Video2 over the blockout. For props and scenery, allow natural realistic detail and graceful physical motion. Match the photographic finish of @Video2: richly detailed weathered oak, caulked seams, credible tension in hemp rigging, heavy stitched canvas, natural seawater and foam, realistic scale, subtle atmospheric depth and cinematic highlight roll-off. No toy ship, no game-engine look, no invented lettering, no captions, no music. Keep this a single continuous shot with no cuts. Do not replay the action or camera movement of @Video2: it is an identity and finish reference only. Six seconds. The approved ship approaches an uninhabited rocky green island and gradually slows. Follow the broad framing of @Video1, boat left and island behind right, but turn the island into a convincing natural coastline with eroded rock, scrub and a sandy cove rather than smooth geometric blobs. Warm late-afternoon light. Gentle tracking, no sudden zooms. Keep the shot composition stable and the ship identity consistent with @Video2.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab10d3/uF0qImDmx26Zj84lf_ZnI_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 2160794}, "seed": 1945848327}`

## 11-estrellas

Video: 23 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0ba3d-8207-7240-ab1b-b71e446c60d6`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0d40/Q1jhVOawMazDHvz2brvWy_03-estrellas.mp4",
    "https://v3b.fal.media/files/b/0aab10a4/a3Cy5d5rk-l2428pTAWJB_13-referencia-estilo-3s.mp4"
  ],
  "resolution": "720p",
  "duration": "4",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
Create a convincing live-action shot for a cinematic historical ocean adventure. REFERENCE ROLES: @Video2 is the approved definitive appearance of our ship and the visual finish to match across this entire film. Preserve its recognizable vessel, three masts, high stern, hull proportions, rigging, canvas colors, wood treatment and Embat branding. @Video1 is a rough Blender storyboard ONLY for scene layout, broad camera path and action order. Do not copy its primitive shapes, flat materials, mechanical motion or toy-like appearance. Reconstruct the scenery and props as real full-scale objects. @Image1 is the exact navy Embat symbol: print it directly on beige canvas without a white rectangular background, as in @Video2. Keep the Embat flag recognizable. For the main vessel, prioritize fidelity to @Video2 over the blockout. For props and scenery, allow natural realistic detail and graceful physical motion. Match the photographic finish of @Video2: richly detailed weathered oak, caulked seams, credible tension in hemp rigging, heavy stitched canvas, natural seawater and foam, realistic scale, subtle atmospheric depth and cinematic highlight roll-off. No toy ship, no game-engine look, no invented lettering, no captions, no music. Keep this a single continuous shot with no cuts. Do not replay the action or camera movement of @Video2: it is an identity and finish reference only. Four seconds. Looking up from the deck of the approved ship at night. Mast, rigging and Embat-branded canvas remain at the left edge and lower left. The right two thirds are uncluttered deep blue night sky with restrained realistic stars. Subtle cloth breathing and very gentle ship motion, almost locked camera. Preserve the materials of @Video2 but relight for believable moonlight, not daylight. No drawn constellations, giant moon, diagrams, numbers or text.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab10d1/9BVHAcTi6UmADoZF1KtxY_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 930583}, "seed": 2099498840}`

## 12-cofre-papiros

Video: 24 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0ba3d-81ff-77f3-a55d-a16f7657ed77`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab10a4/1DI1YKqwHl7u6HZ8_Rwre_20-cofre-papiros.mp4",
    "https://v3b.fal.media/files/b/0aab10a4/a3Cy5d5rk-l2428pTAWJB_13-referencia-estilo-3s.mp4"
  ],
  "resolution": "720p",
  "duration": "8",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
Create a convincing live-action shot for a cinematic historical ocean adventure. REFERENCE ROLES: @Video2 is the approved definitive appearance of our ship and the visual finish to match across this entire film. Preserve its recognizable vessel, three masts, high stern, hull proportions, rigging, canvas colors, wood treatment and Embat branding. @Video1 is a rough Blender storyboard ONLY for scene layout, broad camera path and action order. Do not copy its primitive shapes, flat materials, mechanical motion or toy-like appearance. Reconstruct the scenery and props as real full-scale objects. @Image1 is the exact navy Embat symbol: print it directly on beige canvas without a white rectangular background, as in @Video2. Keep the Embat flag recognizable. For the main vessel, prioritize fidelity to @Video2 over the blockout. For props and scenery, allow natural realistic detail and graceful physical motion. Match the photographic finish of @Video2: richly detailed weathered oak, caulked seams, credible tension in hemp rigging, heavy stitched canvas, natural seawater and foam, realistic scale, subtle atmospheric depth and cinematic highlight roll-off. No toy ship, no game-engine look, no invented lettering, no captions, no music. Keep this a single continuous shot with no cuts. Do not replay the action or camera movement of @Video2: it is an identity and finish reference only. Eight seconds, one elegant continuous camera move. This is a shot aboard a LARGE full-size ship, not a giant chest on a toy boat. Begin with enough of the approved vessel and sea visible to establish scale. A modest toolbox-sized oak chest sits in a corner of the deck near the mainmast. In the first three seconds the camera smoothly dollies toward it until it occupies about half the frame. The chest lid opens naturally on fixed rear hinges, with weight, smooth acceleration and a gentle stop. Reveal EXACTLY THREE rolled parchment scrolls, tied with narrow burgundy ribbons, side by side. Hold long enough to read all three, about one second. One scroll then lifts out in a graceful restrained magical movement, its ribbon loosens and it gently unfurls toward the camera, leaving two scrolls in the chest. End on a stable, blank parchment sheet centered in the frame, large enough for website text, with softly curled edges and subtle paper texture. CREATIVE FREEDOM: redesign the chest, lid construction, hinges, ribbons and scroll geometry to look beautiful and real. Improve the timing and camera path as needed to make this feel like a polished film shot. Do NOT reproduce the stiff blockout opening, rectangular slab-like paper or mechanical floating from @Video1. Its stages are a storyboard, not motion to trace. Do not distort or redesign the approved ship. No cuts, no dissolves, no hands or people, no writing on the parchment, no explosive glitter. Keep the final blank paper readable and stable for the last second.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab10e1/ks_Iq4DCizr0EFPFBwd20_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 3305038}, "seed": 728661449}`

## 13-isla-ciudad

Video: 25 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0ba3d-81fe-7073-9b63-e24912afd55a`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab10a4/Zg7ldSiz4Whyl3rsz--83_21-isla-ciudad.mp4",
    "https://v3b.fal.media/files/b/0aab10a4/a3Cy5d5rk-l2428pTAWJB_13-referencia-estilo-3s.mp4"
  ],
  "resolution": "720p",
  "duration": "6",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
Create a convincing live-action shot for a cinematic historical ocean adventure. REFERENCE ROLES: @Video2 is the approved definitive appearance of our ship and the visual finish to match across this entire film. Preserve its recognizable vessel, three masts, high stern, hull proportions, rigging, canvas colors, wood treatment and Embat branding. @Video1 is a rough Blender storyboard ONLY for scene layout, broad camera path and action order. Do not copy its primitive shapes, flat materials, mechanical motion or toy-like appearance. Reconstruct the scenery and props as real full-scale objects. @Image1 is the exact navy Embat symbol: print it directly on beige canvas without a white rectangular background, as in @Video2. Keep the Embat flag recognizable. For the main vessel, prioritize fidelity to @Video2 over the blockout. For props and scenery, allow natural realistic detail and graceful physical motion. Match the photographic finish of @Video2: richly detailed weathered oak, caulked seams, credible tension in hemp rigging, heavy stitched canvas, natural seawater and foam, realistic scale, subtle atmospheric depth and cinematic highlight roll-off. No toy ship, no game-engine look, no invented lettering, no captions, no music. Keep this a single continuous shot with no cuts. Do not replay the action or camera movement of @Video2: it is an identity and finish reference only. Six seconds. An aerial, slightly downward-looking view of a sizeable island with a small early-sixteenth-century Iberian coastal town and timber piers. The main Embat ship from @Video2 enters in the foreground, matching its appearance exactly. The harbor contains 20 to 30 OTHER clearly separate boats: large well-kept sailing vessels, medium merchant boats, and small weathered boats, several visibly listing. They must vary in size, hull color, sail condition and quality, rather than being identical copies. The boats represent different companies; their variety is the main subject. Preserve two readable isolated company boats in the left third: one larger, clean navy-hulled vessel with sound cream sails; to its right and lower, one smaller weathered vessel noticeably listing. These two will receive website labels. Keep the right third mostly clear open sea for accompanying text. Morning light, convincing stone houses, terracotta roofs, ropes, harbor reflections and natural shore geology. Allow creative freedom to reconstruct the crude island, town and small boats from @Video1 as real full-scale scenery while preserving the broad arrangement and the two featured boats. Slow smooth tracking without cuts. Do not add text, logos to the company boats, a modern marina, cranes or modern motorboats.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab10d8/HZwQlqvUsZ4F9DcBKKzha_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 2063496}, "seed": 1201672896}`

## 14-cierre

Video: 26 · Model: `bytedance/seedance-2.0/fast/reference-to-video` · Evidence: saved request and result

Request ID: `01a0ba3d-81ff-77f3-a55d-a1517bb1ee60`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab0d40/MRFyNMEAkaVyshZcVOitW_06-cierre.mp4",
    "https://v3b.fal.media/files/b/0aab10a4/a3Cy5d5rk-l2428pTAWJB_13-referencia-estilo-3s.mp4"
  ],
  "resolution": "720p",
  "duration": "8",
  "aspect_ratio": "16:9",
  "generate_audio": false
}
```

```text
Create a convincing live-action shot for a cinematic historical ocean adventure. REFERENCE ROLES: @Video2 is the approved definitive appearance of our ship and the visual finish to match across this entire film. Preserve its recognizable vessel, three masts, high stern, hull proportions, rigging, canvas colors, wood treatment and Embat branding. @Video1 is a rough Blender storyboard ONLY for scene layout, broad camera path and action order. Do not copy its primitive shapes, flat materials, mechanical motion or toy-like appearance. Reconstruct the scenery and props as real full-scale objects. @Image1 is the exact navy Embat symbol: print it directly on beige canvas without a white rectangular background, as in @Video2. Keep the Embat flag recognizable. For the main vessel, prioritize fidelity to @Video2 over the blockout. For props and scenery, allow natural realistic detail and graceful physical motion. Match the photographic finish of @Video2: richly detailed weathered oak, caulked seams, credible tension in hemp rigging, heavy stitched canvas, natural seawater and foam, realistic scale, subtle atmospheric depth and cinematic highlight roll-off. No toy ship, no game-engine look, no invented lettering, no captions, no music. Keep this a single continuous shot with no cuts. Do not replay the action or camera movement of @Video2: it is an identity and finish reference only. Eight seconds. Farewell view from behind the approved ship as it sails gently away toward an open horizon, becoming smaller along the trajectory in @Video1. Preserve the ship from @Video2, viewed from the stern and relit at sunset. Warm low horizon, blue-gray ocean, physically realistic wake that disperses naturally. Large clean sky above for credits, but do not generate any text. Camera almost fixed, no orbit, no dramatic zoom, no cuts or fade to black. End with a stable distant ship on the sea.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab10d7/iWDN7u_UqbQG0jpiNmDHa_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 1969509}, "seed": 733682393}`

## 16-cierre-hq

Video: 28 · Model: `bytedance/seedance-2.0/reference-to-video` · Evidence: saved request and result

Request ID: `01a0ba68-5129-7c03-8d1c-73d7d6e8e619`

```json
{
  "image_urls": [
    "https://v3b.fal.media/files/b/0aab0b9a/GxR0KXeV2aTBxmWNxMay3_03-logo-embat-velas.jpg"
  ],
  "video_urls": [
    "https://v3b.fal.media/files/b/0aab10d7/iWDN7u_UqbQG0jpiNmDHa_video.mp4",
    "https://v3b.fal.media/files/b/0aab10a4/a3Cy5d5rk-l2428pTAWJB_13-referencia-estilo-3s.mp4"
  ],
  "resolution": "1080p",
  "duration": "8",
  "aspect_ratio": "16:9",
  "generate_audio": false,
  "bitrate_mode": "high"
}
```

```text
Re-create the SAME farewell shot as @Video1 as a genuinely photoreal live-action historical maritime film shot, not a different shot. @Video1 defines the framing, camera position, eight-second duration, rear view, trajectory, pace and sunset horizon. Keep all of those. @Video2 defines the approved Embat ship identity and the quality of its materials ONLY; do NOT use its lateral camera angle, action or lighting time of day. @Image1 is the exact navy Embat sail symbol; preserve it directly on beige canvas without a white rectangle, and preserve the Embat flag. The substantial three-masted nao Victoria is seen FROM BEHIND and sails straight away from the viewer into the distance, gradually becoming smaller. The camera remains nearly locked. Keep the generous empty sunset sky and the ship's screen position from @Video1. No cuts, no orbit, no approach toward the ship, no side view, no zoom-in, no added land, ships or people.

The previous version has a flat synthetic ocean, a simple gradient sky and miniature-like materials. Correct those weaknesses completely while keeping the shot itself. This must look photographed from a real vessel at sea. Give the water physically plausible overlapping blue-gray swells, irregular small ripples, fine reflected highlights and real depth; the heavy hull leaves a widening turbulent wake with delicate foam that disperses and sinks naturally instead of white dotted ribbons. Fine-grained weathered oak on the stern with caulked seams, real railings, tensioned hemp rigging, thick woven cream canvas with stitching and subtle wind-driven folds. Preserve the approved hull proportions and recognisable rear silhouette. Full-size inertia and coherent sea scale, never a miniature model. Sunset provides low warm grazing light along the stern and canvas edges, cool ambient fill in the shadows, subtle distant sea haze and thin naturally layered clouds near the warm horizon, not a perfectly uniform computer gradient. Restrained high-end cinematic color, realistic exposure, fine natural detail, no oversharpening. Do not merely sharpen or upscale @Video1: replace its synthetic shading and water with real photographic appearance. No cartoon, no plastic, no game render, no stylized smooth water, no artificial white streaks, no new text, no captions, no music. End on the distant ship and hold the composition, without fading to black. One continuous eight-second stern-away shot with the same composition as @Video1.
```

Result: `{"video": {"url": "https://v3b.fal.media/files/b/0aab1208/pFjmdc79-GDzKelTzhnuI_video.mp4", "content_type": "video/mp4", "file_name": "video.mp4", "file_size": 19284578}, "seed": 1486535347}`

## poster-topaz-upscale

Video: image only · Model: `topaz/upscale/image/precision` · Evidence: saved request and result; image upscale, not boat video

Request ID: `01a0ba92-7f03-7bb2-8b81-6427a79293f0`

```json
{
  "image_url": "https://raw.githubusercontent.com/amarkosmarkos/Elkano_Embat/xubranch/posters/assets/ship-slide1-5p75s.png",
  "model": "High Fidelity V3",
  "upscale_factor": 4,
  "output_format": "png",
  "face_enhancement": false,
  "subject_detection": "All",
  "crop_to_fill": false
}
```

Result: `{"image": {"url": "https://v3b.fal.media/files/b/0aab12ea/pofINbLbA1XzF3XwE-2Zo_image.png", "content_type": "image/png", "file_name": "image.png", "file_size": 12246257}}`
