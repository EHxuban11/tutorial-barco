---
name: xu-fal
description: Use fal.ai to inspect models and account readiness, upload media, submit budgeted generations, track jobs, and retrieve results. Use for fal Assets, reference-to-video and other fal model workflows.
---

# XU-fal

For the complete Blender → cinematic video → website workflow and its verified boat example, use `$xu-3d-website`.

Distinguish local files, storage uploads, Assets-library entries, submitted requests and verified outputs. Preserve the user's model, budget and desired result.

## Choose a working route

Prefer the official `fal-client` Python SDK or `@fal-ai/client` when an authorized credential exists. A signed-in website does not mean the terminal has `FAL_KEY`; check presence without printing values. A masked dashboard key is not a recoverable secret.

Use the browser for the Assets library and playground when appropriate. Read its current upload documentation. Do not treat browser cookies or hidden application state as substitute API credentials.

Read [upload troubleshooting](references/uploads.md) before diagnosing file-transfer failures. The bundled [upload helper](scripts/fal_upload.py) plans or uploads explicitly listed files and saves hash-based receipts; it never runs a model. **Storage upload success does not prove registration in the website's Assets library.** Verify that separately when requested.

The verified route is SDK upload followed by the public Assets registration API; both helpers and the exact runbook are in the upload reference. Provide an API-only key through `FAL_KEY` or a Keychain entry of your choice. No browser picker is needed for this route.

## Prepare a concrete request

Inspect the intended account, current credits, credential availability and actual model restrictions without collecting unrelated billing data. Check the selected model's live fal API schema and pricing: versions, enum values, input limits and formulas change.

Inspect media dimensions, duration, fps and size. Validate combined reference limits. Record the exact endpoint, prompt, ordered file URLs, resolution, duration, aspect ratio, audio and quality settings. Describe retiming and resizing accurately.

## Budget and submission

Carry forward an approved spending limit; do not ask again. If none exists, obtain it before a paid request. Generation approval does not authorize top-ups, subscriptions, key creation or account-wide changes.

Use the live formula, including reference duration when charged. Choose tier, duration and resolution to match the user's cost/quality preference. For cheap trials, inspect one first attempt before buying variants.

Save the request and returned request ID immediately. Poll that ID. A timeout or lost page does not justify another paid submission; inspect request history if its outcome is ambiguous. Resolve status and remaining budget before retrying, and stop if the cap could be exceeded.

Prefer recoverable queue submission over an unrecorded blocking call. Keep receipts, ordered inputs and outputs in the project without credentials. Download the actual completed request's URL, not the playground sample.

## Verify

Fully decode outputs and inspect motion, camera behavior, identity, logo integrity, connected parts and unwanted text. HTTP success is not visual approval. For multi-scene continuity, give the new action clip and approved appearance clip distinct roles; read [reference-video notes](references/reference-video.md).

Report actual states and spend; label estimates. Keep a ledger across turns to prevent accidental duplicate jobs.

Official references: https://fal.ai/docs/model-apis/file-uploads and https://fal-ai.github.io/fal/client/fal_client.html plus the chosen model's `/api` page.

Use `$xu-blender-animations` for editable scene references and `$xu-scroll-video-website` for the final presentation.
