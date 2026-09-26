# Clip-site delivery checks

- Asset provenance: approved generated output, raw Blender reference or held still? Keep the labels honest.
- Re-encode a copy; preserve the original. Keyframes every 0.5 seconds are a useful starting point for scrubbing, not a universal optimal value.
- Use the decoded video duration, including editorial cuts. Never hardcode the nominal requested generation duration.
- Maintain one scroll/playback controller. Reverse movement and skip buttons must update the same progress state as scrolling.
- Text and interactive overlays remain separate from cinematic footage. Cover crop must match between video and SVG/Canvas at every tested size.
- Reduced motion should show a stable visual until the user explicitly enables animation. Ensure navigation still works.
- Test failed media rather than leaving an invisible video or a permanently disabled-looking page.
- If metadata has not loaded, preserve the desired scroll position and seek once it does. Avoid flooding the decoder with overlapping seeks.
- At the end, hold a valid final frame rather than seeking to an invalid timestamp and flashing black.
- In the historical boat project, the hero was a generated clip; the night reference began as a held Blender still; constellation overlays were browser code. Do not describe all three as the same kind of animation.
- Keep deployment scope explicit. A request to make a reusable skill or local draft does not authorize replacing the existing live deck.
