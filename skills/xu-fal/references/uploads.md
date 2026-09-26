# Upload routes and diagnostics

## Official SDK

`fal_client.upload_file(path)` returns an access URL. `SyncClient(key=...)` accepts a credential kept in memory. Check the current official SDK reference when updating the helper.

`scripts/fal_upload.py` defaults to a local-only plan. Add `--upload` only for authorized files/destination. Use `FAL_KEY`, a specifically named Keychain service, or its hidden interactive prompt. Never put keys in CLI arguments, committed files, logs or chat.

Reuse a matching hash receipt. Use `--refresh` deliberately if the URL expired/deleted. The helper records `storage_uploaded`, not `assets_library_verified`.

## Browser Assets

Navigate to `https://fal.ai/assets`. Observed September 2026 controls: **Upload media**, **Upload folder as collection**, **All media**. Read current UI; never bake volatile element IDs into a skill.

Stage only approved files in a dedicated folder for bulk selection. Check multi-file support. Use the documented chooser flow: register `filechooser`, click the upload control, set absolute paths, then verify completion.

### Browser pickers can fail

Automated file choosers may be blocked by browser or extension permissions. The native picker usually works if focus is in the file list before selecting files; verify the selection before confirming. If the UI stays unreliable, use the SDK route below rather than retrying the same transfer.

After a diagnosed failure, try a materially different supported route. Do not repeat identical rejected transfers, bypass policy rejection or invoke private fal endpoints. If the UI is unreliable, use an authorized SDK credential or provide the exact prepared folder for manual upload.

## Verify and reuse

Confirm filenames, thumbnails, types and count in Assets. Save actual asset IDs/URLs exposed by the UI. Verify Image1/Video1 ordering in the generation form; upload order alone is not proof. Search before repeating an upload with uncertain outcome. Update this runbook with the specific route that succeeds.

## Verified resolution: SDK storage plus public Assets registration

The working route in this session was **not another browser picker retry**:

1. With explicit user approval, create an API-only key. Keep it in `FAL_KEY` or a macOS Keychain entry (read it with `security find-generic-password -s <service> -w` inside a process); never print the value or store it in a skill.
2. Use the official `fal-client` SDK (tested version 1.0.3) to upload the files and save their CDN URLs with `scripts/fal_upload.py`.
3. Register those existing URLs in the public **Assets API** using [scripts/register_assets.py](../scripts/register_assets.py). It posts to `https://api.fal.ai/v1/assets/uploads` with `Authorization: Key ...`, a body containing `url`, `type`, `prompt`, `favorite` and `tag_ids`, plus a stable `Idempotency-Key` derived from the content hash.
4. Refresh `https://fal.ai/assets` and verify the four named entries. This worked for the logo and the Blender references.

The public contract was verified in the fal-maintained community CLI source: https://github.com/fal-ai-community/genmedia-cli/blob/main/src/commands/assets/upload.ts and `src/lib/assets.ts`, `src/lib/api.ts`. Listing works with `GET https://api.fal.ai/v1/assets?section=uploads&limit=20`. This API-only key successfully accessed it; administrator scope was unnecessary.

Storage uploads alone initially did **not** appear in the Assets UI. Registration was the missing step. Prefer this proven two-step route when an authorized key is available.
