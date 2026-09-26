# Reusable skills

Start with [`xu-3d-website`](xu-3d-website/SKILL.md), the end-to-end workflow. Its supporting packages are:

- [`xu-blender-animations`](xu-blender-animations/SKILL.md): editable scenes and motion references.
- [`xu-fal`](xu-fal/SKILL.md): uploads, Assets registration, model requests, spending limits and verification.
- [`xu-scroll-video-website`](xu-scroll-video-website/SKILL.md): clip playback, scroll synchronization, overlays and delivery.

Copy all four folders into the skills directory supported by your agent. `SKILL.md` is the entry point. Helpers are run through the tools they name rather than automatically when a skill is loaded.

The boat-specific evidence lives in the umbrella skill's references and this repository's `docs/audit/`. No credentials are included: bring your own fal key through `FAL_KEY` or a Keychain entry you choose.
