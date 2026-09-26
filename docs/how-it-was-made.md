# How the original was made

Reconstructed from the original agent tool calls, Blender source scripts and frame directories, 13 saved fal requests, media verification reports and weekend Git history. This is a production summary; private conversation logs and original request receipts are not distributed here.

## Three layers

1. **Blender:** Astra wrote and executed Python using `bpy`. The result was an editable ship with materials, cameras, keyframes and sail/flag shape keys. Computer use helped inspect the app and operate browser interfaces. A Blender MCP was not needed.
2. **Seedance:** ByteDance Seedance 2.0 on fal.ai regenerated the reference shots with different materials, water, light and fine detail. This was generative finishing, not just upscaling.
3. **Website:** Next.js controlled MP4 playback through scroll and navigation. HTML, Canvas and SVG supplied text, particles, constellations, score and logo overlays.

The production session records Astra (medium effort) and Blender 5.2.2 LTS. These are historical versions, not guarantees about what will be available or required for a new attempt.

## The ship

The brief asked for a ship inspired by Elcano’s Victoria. The agent consulted historical reference pages and built a stylized interpretation procedurally. The reviewed evidence does not establish reconstruction from ship photographs or use of an imported ship mesh. The supplied images were used for branding.

The model evolved through improvements to the hull, rigging, sails, ocean, materials and light. Early camera studies were inspired by two One Piece clips. The final hero used a separate lateral shot, so those camera studies are not prerequisites for the tutorial.

## The first six references

| Scene | Blender input | First generated output filename |
|---|---|---|
| Hero / Zarpar | 12-second animation, 288 frames | 13.mp4 |
| Island approach | 6-second animation, 144 frames | 14.mp4 |
| Night sky | Single still held for four seconds | 15.mp4 |
| Chest | Closed/open stills held for two/four seconds | 16.mp4 |
| Harbour | Single still held for four seconds | 17.mp4 |
| Closing | 8-second animation, 192 frames | 18.mp4 |

Most animated previews were 800×450, then resized to 1280×720 for upload. The six outputs used Seedance 2.0 Fast reference-to-video at 720p, 16:9, with audio disabled. Verification recorded 24 fps. Each request supplied its scene reference and the logo, but no common hero video yet.

## What changed after the first batch

The hero, 13.mp4, became the approved appearance reference. Later jobs paired each scene’s layout/action reference with a three-second extract of that hero and the logo. The prompts assigned a different role to each input.

The chest was rebuilt as a full eight-second Blender animation: approach a small chest on a large ship, open it, reveal three scrolls, and lift/unfurl one. The island-city used a full six-second animation with 26 varied boats. These generated replacements became 24.mp4 and 25.mp4.

The revised stars were 23.mp4. The improved closing, 28.mp4, used standard Seedance 2.0 at 1080p with high bitrate, using the previous generated closing as the action reference and the hero as the appearance reference. Seedance 2.5 was discussed but is not the model in the saved production requests.

## The web animations and team contributions

The night-video background and the constellations are separate layers. The initial `SkyStory` overlay came from the team’s branch: commits `34aee47` and `cdd8780` credit Markos and Claude Opus 5. Astra merged the work and later refined alignment and playback. The tutorial can recreate it with one agent, but that consolidates the original contributions.

The website re-encoded videos with frequent keyframes for seeking, mapped progress to `video.currentTime`, and added playback/skip controls. The browser did not run the Blender model in real time.

Several experiments were discarded, including water turning into a button and camera-like zooms into individual harbour boats. The island approach and original harbour were removed from the main presentation order. The chest clip was ultimately stopped at 60% so the three scrolls could carry product labels before the unfurling action.

## What the tutorial changes

The tutorial approves a hero before generating other scenes. Historically, that decision followed the first six-scene batch. It also omits account-setup detours, posters, unrelated product work and discarded visual experiments.

The [historical prompts](historical-seedance-prompts.md) preserve the original generation instructions. The [tutorial](tutorial.md) provides a clearer teaching sequence. Matching the original output exactly is not guaranteed.
