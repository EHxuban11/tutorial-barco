# From the hackathon traces to a teachable workflow

The traces explain how the finished experience was built and refined. They do not measure audience engagement or prove a single cause of its reception. Here, **observed** means supported by prompts, code or artifacts; **interpretation** means a plausible explanation of the visual effect.

## The result was directed, not produced by one magic prompt

The work contains a sequence of human decisions: choose a recognizable ship, put the actual brand on it, improve its motion reference, ask for a different photographic finish, select a hero, reuse its appearance, rewrite the story, fix timing/alignment, and delete effects that did not help. The tutorial should make those decisions visible.

### 1. The visual metaphor did useful work

**Observed:** in [main:3369](audit/user-prompts.md#main-3369), Xuban explicitly defines three section types: animation, ordinary web content, and a hybrid. The night sky is not just decoration: scattered signals form patterns, then a score and the EMBAT symbol. The chest reveals three products. Boats in the harbour stand for companies.

**Interpretation:** one visual world connects otherwise different presentation subjects. The audience sees a progression instead of a collection of unrelated demos. The brand mark becomes part of the story rather than a sponsor sticker.

**Teach:** write the narrative function of each shot before building it. A shot needs an explanation of what it contributes, not just a visual prompt.

### 2. The boat was designed as a composition, not only a model

**Observed:** the final hero has a 45 mm camera, a lateral entrance, a small two-unit camera movement, and room on the right for copy. Small heave/pitch/roll, animated sails and flag, an Ocean modifier, and a wake attached to the hull supply related motions. See `scene01_zarpar.py`, `art_directed_voyage.py`, and the saved scene.

**Interpretation:** motion across several scales, sea/ship contact, atmospheric depth and transmitted light through sails plausibly increase the impression of life and scale. This is not an experiment proving that distance or undulation is the decisive factor.

**Teach:** show the composition and simple motion first. An attractive static model with an unsuitable camera can still be a poor video reference.

### 3. The generation prompt separated structure from finish

**Observed:** video 7's prompt emphasizes preserving the original while improving rendering. Video 8 and the later turning-point request for video 13 explicitly say to use the video only for camera/layout and to replace its rendered appearance with live-action photographic realism. Both successes used a Blender clip plus a logo, without a photographic still first.

**Interpretation:** this gives the generative model a clearer division between constraints and creative freedom. It is consistent with the improvement, but does not prove that a particular phrase alone caused it.

**Teach:** show the actual before/after and highlight the preservation/reconstruction boundary. Do not sell “HD” or a resolution switch as the whole trick. The [turning-point prompt](turning-point-prompt.md) is the central worked example.

### 4. Human selection established a consistent identity

**Observed:** Xuban praises video 8 at [main:2194](audit/user-prompts.md#main-2194). Later, [main:3941](audit/user-prompts.md#main-3941) rejects using 8 as the shared reference; [main:3951](audit/user-prompts.md#main-3951) explicitly selects **13 for all scenes**. Main:3957 extracts seconds 5–8 of video 13 for that purpose.

**Interpretation:** once a recognizable look is selected, consistency matters more than repeatedly asking a model to rediscover it from prose. The small appearance clip gives later shots a common visual reference.

**Teach:** approve a real output, then assign separate roles to action, appearance and branding inputs. Do not propagate an agent's preferred take when the human chose another.

### 5. Code supplied the precise part of the magic

**Observed:** the constellation background comes from video 23. Canvas draws particles; SVG draws lines, labels, score and the logo. Both follow the same crop as the video. Main:4381 identifies the mismatch with the older background; [web:424](audit/user-prompts.md#web-424) demands a rollback of a redesign and asks only for alignment to the actual stars. The final code records checks across 40 video samples.

**Interpretation:** photographic footage provides atmosphere while code provides precise, readable, interactive meaning. Baking all labels into generated video would make corrections harder and typography less controllable.

**Teach:** display the unadorned night clip, then enable the overlay. Explain which tool made which pixels. Measure positions on the new video instead of copying old coordinates.

### 6. Pacing and responsiveness made it feel like a product

**Observed:** [web:318](audit/user-prompts.md#web-318) asks to slow the stars; [web:617](audit/user-prompts.md#web-617) reports navigation lag; [web:744](audit/user-prompts.md#web-744) reports delayed closing copy; [web:852](audit/user-prompts.md#web-852) asks for autoplay. The code uses quarter-speed night playback, coordinated scroll/video progress, seek guards, adjacent-route prefetch, next-clip warming, consistent controls and closing copy independent of video state.

**Interpretation:** a beautiful clip loses impact when controls hesitate or its explanation moves too quickly. Perceived polish includes the time between an action and its response.

**Teach:** review the presentation interactively, not only as screenshots or a successful build. Test scroll, pause, reverse, skip and re-entry with real media.

### 7. Removing work improved the story

**Observed:** [main:4465](audit/user-prompts.md#main-4465) removes the island approach because it adds little. Main:3744 demands a believable small chest on a large ship; [main:3907](audit/user-prompts.md#main-3907) gives Seedance freedom to improve the clunky prop action. The final chest is cut at 60%, with a slowdown and hold on its three scrolls. Main:5407 removes the water-button effect; [main:5499](audit/user-prompts.md#main-5499) removes the boat zoom transitions.

**Interpretation:** the final experience benefits from selection and restraint. The amount of rendering or coding already invested did not determine what the audience had to watch.

**Teach:** include one example of a rejected or shortened effect. “What did we leave out?” belongs in the tutorial alongside “What did we generate?”

## What the audience actually asked for

After [the tweet](https://x.com/EHxuban11/status/2102178233001156782), public replies asked for a tutorial, for the tool and for the prompt (“Pasa el prompt”). Several praised the landing and its design.

This supports teaching the tools, prompts and actual intermediate outputs. It does not establish that respondents already understood the Blender/Seedance split or that they specifically requested a frame-sequence website. Those details must come from the production evidence.

## The minimum tutorial that teaches the mechanism

Build **hero → night → scroll website → constellation overlay**. This captures the essential workflow without the financial platform or all historical experiments. The chest, island-city and closing become optional extensions.

1. Show the finished hero and star scene briefly, then state the three-layer architecture.
2. Start an actually empty tutorial workspace. Record tools/versions and the supplied logo.
3. Ask the agent for editable geometry and restrained animation. Show the `.blend`, not only a screenshot.
4. Stage the lateral hero with a clear copy area. Inspect three frames, then the complete modest reference.
5. Prepare valid media and submit the turning-point-style request. Save its exact inputs and receipt. Show the raw reference beside the generated result.
6. Select the hero based on the actual result. Do not claim one prompt guarantees a perfect take.
7. Reuse the new ship for an upward night composition. Explain that a held still was the original method. Create a short appearance extract from the **new** hero.
8. Generate the night scene with action/appearance/brand roles separated. Inspect the output before coding star positions.
9. Build one reusable scroll scene and one scene configuration file. Use real media metadata, poster/error states and reduced-motion behavior.
10. Add HTML copy and a separately aligned Canvas/SVG overlay. Make play/pause/reverse/skip use a coherent timeline.
11. Re-encode web copies, test the actual website and package the real new result.
12. Publish the source, prompts, versions, selected outputs and failed attempts. Disclose rendering waits, resizing, held stills and editorial cuts.

The detailed [tutorial](tutorial.md), [prompt sequence](../prompts/README.md) and [workflow skill](../skills/xu-3d-website/SKILL.md) implement this teaching order. It is a streamlined reconstruction, not a claim that the hackathon happened in exactly that order.

## What remains unproven

The archived website builds and the central Blender scenes render locally. We have not rerun a complete fresh model → generated hero → generated night → website rehearsal, and no new paid generation was authorized for this audit. A fresh run is the necessary final test before advertising the tutorial as validated end to end.

The audit covers the locally available agent production traces and Git evidence. It cannot claim every teammate's conversation, every manual GUI choice or absent session. The later reaction data shows visible interest and specific requests; it does not isolate the causes of sharing or measure all viewers' opinions. Those limitations do not erase the verified recipe; they define what we can responsibly teach.
