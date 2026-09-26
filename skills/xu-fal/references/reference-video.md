# Reference-to-video notes

The historical boat used Seedance 2.0 Fast at 720p, with standard 2.0 for one 1080p finishing pass. Exact prompts are in this repository's `docs/historical-seedance-prompts.md`. These are examples, not current API guarantees or permission to reuse old assets.

Blender provides camera, layout and timing; generative finishing reconstructs materials and lighting, and may distort geometry. Inspect the whole result.

- `@Video1`: new shot's camera and action.
- `@Video2`: short approved hero excerpt for appearance only, when useful.
- `@Image1`: exact supplied logo.
- Additional images: clear identity views within current limits.

For fixed shots, explicitly prohibit pan, tilt, tracking, dolly, zoom, orbit and reframing, and provide a truly fixed reference. Specify which end leads and screen direction. Keep stars/scenery stationary for a slow night pass and reserve the overlay area.

Prompt real materials and scale. Preserve silhouettes, connected parts, ground contact and branding. Leave constellation lines and presentation text for the website when they are meant to be interactive.
