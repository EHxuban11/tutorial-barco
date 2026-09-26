# Verified boat lineage

Evidence was re-audited on 23 September 2026 from the two original agent sessions, saved scripts and fal receipts, the public team repository and read-only fal Assets metadata. No new model generations were needed for the audit.

## The important distinction

- **Video 7:** earlier conservative generation. It asked to improve rendering while preserving the source very closely. Xuban wanted more photographic realism. Exact prompt/output were recovered from Assets; not every original input setting is preserved.
- **Video 8:** first preserved cinematic test, Seedance 2.0 Fast, requested four seconds at 720p with a five-second Blender reference and the logo. At 14:11:22 CEST on 19 September, Xuban approved it enthusiastically. The assistant had just called it insufficiently Hollywood: this is a useful reminder that human approval and an agent's visual opinion differ.
- **Video 13 / Zarpar:** the final website's slide-1 boat. Request saved 19 September at 14:53:34 CEST; downloaded at 14:59:24. Fast reference-to-video, 12 seconds, 720p, 16:9, no audio. Inputs: `01-barco-largo.mp4` and the EMBAT sail logo, no photographic appearance still and no video 8. This is **the turning-point prompt** for the tutorial.
- **13-referencia-estilo-3s.mp4:** an extract made later from video 13. The paragraph beginning “A large, traditional wooden sailing ship…” describes this uploaded asset. It is not the prompt that generated video 13.
- At 17:09, Xuban explicitly chose **13, not 8**, as the common appearance reference for the remaining scenes.

## Scene lineage

| Scene | Blender input | First output | Shared-hero revision |
| --- | --- | --- | --- |
| Hero | 12-second lateral animation | 13 | Hero itself retained |
| Island | Six-second animation | 14 | 22 |
| Stars | A still held in a four-second video | 15 | 23 |
| Chest | Closed/open poses held for two/four seconds | 16 | Fully animated eight-second rebuild → 24 |
| Harbour | A still held for four seconds | 17 | Kept outside the main route order |
| Closing | Eight-second animation | 18 | 26, then standard Seedance 2.0 at 1080p/high bitrate → 28 |
| Island-city | Six-second rebuilt scene with 26 varied boats | — | 25 |

The original process generated six initial scenes before choosing the common hero. A streamlined tutorial may approve the hero first, but should label that as a better teaching order rather than rewrite history.

The final deck selects 13, 23, 24, 28 and 25, with 22/17 archived outside the main sequence. The chest stops at 60%. The stars' particles/constellations/score/logo are coded overlays; the background is generated video.

## Attribution and limits

The main Astra session authored the procedural ship and most scene work. Markos's commits `34aee47` and `cdd8780`, co-authored with Claude Opus 5, supplied the initial SkyStory overlay. Astra merged and refined it. Do not credit one agent with all team work.

There are 14 recovered video-generation prompts, 13 with complete saved request/result receipts, plus one Topaz poster upscale. Seven auxiliary image-generation calls made portrait, poster, company-boat and texture assets; they were not inputs to the first successful video.

Full evidence and original quotes live in the tutorial repo's `docs/audit/`. Public source: https://github.com/amarkosmarkos/Elkano_Embat .
