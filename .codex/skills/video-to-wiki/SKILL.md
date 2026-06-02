---
name: video-to-wiki
description: Turn learning videos and yt-dlp-supported URLs into this repository's Karpathy-style LLM Wiki evidence and notes. Use when Codex needs to capture video media, subtitles, local ASR transcripts, metadata, keyframes, comments, companion links, code repositories, or course materials; register the video as one raw source document; optionally compile it into a standard wiki note when the user asks for digestion; and update wiki index/log/watchlists without treating video assets as knowledge.
---

# Video To Wiki

Use this skill to process a video as one source in the repository lifecycle. Do not create a parallel "video note" taxonomy. Route evidence to `raw/`, compiled understanding to `wiki/`, and rules/templates to `schema/`.

## Core Rule

Videos, subtitles, comments, screenshots, ASR output, and thumbnails are evidence. They are not knowledge. Knowledge begins only after the material has been understood, compressed, questioned, rewritten in Chinese, and linked back to its sources.

## Workflow

### 1. Evidence Capture

Locate the video URL first. If the user points to a watchlist, read it and pick the named video without rewriting unrelated rankings.

Capture assets with the helper script:

```bash
python3 .codex/skills/video-to-wiki/scripts/video_to_wiki_assets.py capture \
  'VIDEO_URL' \
  --slug 'YYYY-MM-DD-channel-topic'
```

Default asset home:

```text
raw/assets/local-media/youtube/<slug>/
```

Use the old-compatible path only when explicitly needed:

```bash
python3 .codex/skills/video-to-wiki/scripts/video_to_wiki_assets.py capture \
  'VIDEO_URL' \
  --slug 'YYYY-MM-DD-channel-topic' \
  --media-root local-media/youtube
```

The helper captures media, subtitles, metadata, transcripts, chapter transcript, keyframes, comments, and `asset-manifest.md`. It prefers QuickTime-compatible MP4 media: H.264/`avc1` video up to 1080p plus AAC/`mp4a` audio. Do not download AV1/Opus "best" formats unless the user explicitly values archival quality over macOS compatibility.

For missing downloadable captions, use the local ASR fallback rules in `references/asr-fallback.md`. Never call ASR output official subtitles.

### 2. Source Registration

Create or update one source document for each video:

```text
raw/sources/<domain>/videos/<YYYY-MM-DD-title-slug>.md
```

Use `schema/templates/source-card.md`. Fill it as follows:

- `source_type: video`
- `source_level: secondary` unless the video is an official primary source
- `media_format: video`
- 作者 / 机构：channel or uploader
- 原始链接：original video URL
- 本地资产：`raw/assets/local-media/youtube/<slug>/asset-manifest.md`
- 原始内容：captured evidence inventory, not the video's learned content
- 关键线索：candidate code links, official docs, course pages, pinned comments, uploader replies, corrections, and implementation caveats
- 处理状态：mark read, converted to note, entered research, extracted stable knowledge, or used in output as actually completed

The document's `采集日志` records missing subtitles, ASR use, failed comments, failed keyframes, and other capture issues.

Treat comments as source clues, not facts. Do not promote commenter claims unless verified against the video, code, official docs, or experiments.

### 3. Capture-Only Mode

When `knowledge-base-workflow` routes a video for collection, or when the user only asks to collect/save/register the video, stop after evidence capture and source registration.

A capture-only video ingest leaves:

```text
raw/assets/local-media/youtube/<slug>/asset-manifest.md
raw/sources/<domain>/videos/<YYYY-MM-DD-title-slug>.md
```

Do not create `wiki/notes/` in capture-only mode. Mark the source as `captured` or `to_digest`.

### 4. Knowledge Compilation

Only compile the video into a wiki note when the user explicitly asks to digest, understand, summarize as a note, or write a video note.

Write the compiled note under:

```text
wiki/notes/<domain-or-topic>/<note-title>.md
```

Use `references/note-template.md`. The note must be a standard `type: note` wiki node with frontmatter and `source_refs`. At minimum, `source_refs` includes:

- original video URL
- `raw/sources/<domain>/videos/<YYYY-MM-DD-title-slug>.md`
- `raw/assets/local-media/youtube/<slug>/asset-manifest.md`

Read only the generated files needed for the note:

- `asset-manifest.md` for metadata, asset paths, subtitle source, and candidate code links
- `transcript-clean.txt` for content
- `chapter-transcript.md` for timeline structure
- `comments-digest.md` for pinned comments, uploader replies, corrections, caveats, and links
- `frames/contact-keyframes.jpg` and selected `frames/frame-*.jpg` when diagrams, UI flows, architecture, or visual processes matter

Do not paste long transcript blocks. Rebuild the content in your own Chinese explanation. Use Mermaid only when the video actually contains a process, architecture, interaction, state loop, or data flow worth preserving.

### 5. Wiki Maintenance

A capture-only video ingest must leave one source document and the asset manifest. A complete video digest must additionally leave a compiled note:

```text
raw/assets/local-media/youtube/<slug>/asset-manifest.md
raw/sources/<domain>/videos/<YYYY-MM-DD-title-slug>.md
wiki/notes/<domain-or-topic>/<note-title>.md  # only for digest mode
```

Then maintain the global wiki:

- Update `wiki/index.md`.
- Append `wiki/log.md` with `## [YYYY-MM-DD] ingest | <title>`.
- If the source came from a watchlist, add a short `已沉淀` backlink to the new note. Do not treat the watchlist backlink as a replacement for index/log.

## Upgrade Rules

Keep the first compiled video note in `wiki/notes/` by default.

- Upgrade to `wiki/topics/` only when the conclusion is stable, reusable, and cross-source.
- Upgrade to `wiki/research/` only when there is a clear question being answered.
- Upgrade to `wiki/labs/` only when there is a concrete API, SDK, toolchain, failure mode, benchmark, or engineering claim that needs a minimal runnable validation.

Use the standard `是否需要升级` checklist in the note. Do not invent video-specific archive categories.

## Accuracy Rules

- Distinguish transcript-derived understanding from verified facts.
- Verify current APIs, SDKs, models, product behavior, prices, laws, and unstable facts against current primary sources before writing them as facts.
- If example code from the video was not run locally, list it under `未验证事项`.
- If `subtitle_source` indicates local ASR, say that the transcript was generated by local `whisper.cpp` ASR and was not fully human-proofread.
- If no subtitle, ASR transcript, or human-reviewed transcript exists, do not claim the video has been fully digested.
- For high-risk agent actions, explicitly mention human review: shell commands, file writes outside the workspace, database mutations, email, payment, deployment, and account actions.

## Final Response

Report the lifecycle classification and the paths created or updated:

- asset directory and manifest
- source document
- wiki note, only when digest mode was requested
- `wiki/index.md` update
- `wiki/log.md` append
- watchlist backlink, if applicable
- verified checks and remaining `未验证事项`

## Compatibility

`video-study-notes` was the old name. Use `video-to-wiki` for new work and do not add new references to the old skill name except compatibility notes.
