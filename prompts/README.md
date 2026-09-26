# Prompt sequence

Start a fresh agent conversation in an empty project folder. Copy these prompts individually as you reach each checkpoint in the [tutorial](../docs/tutorial.md). Do not paste the whole sequence as a single unattended job.

Prompts 01, 02, 04, 05, 07 and 08 are newly written teaching prompts based on the original workflow. Prompts 03 and 06 are verbatim historical Seedance prompts; adapt their Embat references to your own brand before use.

| Step | Prompt | Where to use it | Inputs |
|---|---|---|---|
| 1 | [Build the ship](01-build-ship.txt) | Local coding agent | Your logo; disclosed historical references if wanted |
| 2 | [Hero animation](02-hero-animation.txt) | Local coding agent | Ship made in step 1 |
| 3 | [Generate the hero](03-seedance-hero.txt) | Seedance Fast reference-to-video | Video1: new Blender hero; Image1: logo |
| 4 (optional) | [Island approach](04-island-scene.txt) | Local coding agent | Ship made in step 1 |
| 5 | [Night scene](05-night-sky-scene.txt) | Local coding agent | Ship made in step 1 |
| 6 | [Generate the night scene](06-seedance-night-with-hero-reference.txt) | Seedance Fast reference-to-video | Video1: night reference; Video2: 3-second extract of your newly approved hero; Image1: logo |
| 7 | [Scroll website](07-scroll-website.txt) | Local coding agent | New generated videos |
| 8 | [Constellation overlay](08-constellation-overlay.txt) | Local coding agent | Working night-video webpage |

For step 3, use `bytedance/seedance-2.0/fast/reference-to-video`: 720p, 12 seconds, 16:9, audio off. For step 6, use the same settings but four seconds of output. Respect the endpoint’s combined reference-duration limit, counting both input videos.

The complete prompts for the island, chest, city and closing are in [historical Seedance prompts](../docs/historical-seedance-prompts.md). Use the `seedance-reference13` variants for shared-hero conditioning; “13” is the old filename, not a file you need to download. Supply your own hero from this run.

Check the [current fal endpoint documentation](https://fal.ai/models/bytedance/seedance-2.0/fast/reference-to-video/api) before running paid generations. Keep API credentials outside prompts, source files and recordings.
