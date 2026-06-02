---
name: knowledge-base-workflow
description: Organize materials into this repository's Karpathy-style LLM Wiki lifecycle. Use when Codex needs to ingest, automatically capture, classify, summarize, digest, migrate, upgrade, or route links, PDFs, videos, books, articles, WeChat articles, web pages with images, GitHub repos, AI research reports, notes, watchlists, experiments, outputs, templates, or user ideas in this repo; decide between raw/inbox, raw/sources single source documents, wiki/notes, wiki/topics, wiki/research, wiki/labs, schema/methods, wiki/outputs, schema/meta, and wiki/archive; update source documents, local assets, manifests, topic maps, wiki index, or wiki log.
---

# Knowledge Base Workflow

Use this skill to turn incoming material into durable knowledge in this repository. The core rule is: automatically capture evidence into a readable Markdown document under `raw/`, but compile knowledge into `wiki/` only after the material has been understood, questioned, and rewritten.

## Decision Tree

Classify lifecycle before theme:

| Current state | Home | Required action |
| --- | --- | --- |
| Raw clue, idea, or unprocessed link | `raw/inbox/` | Capture briefly; do not pretend it is knowledge. |
| Source worth preserving but not digested | `raw/sources/<domain>/<source-type>/<YYYY-MM-DD-title-slug>.md` | Create one source document from `schema/templates/source-card.md`; put images or small assets in a same-name `.assets/` directory. |
| Read, watched, or understood material | `wiki/notes/<domain-or-topic>/` | Write a note from `schema/templates/note.md` with own understanding and unverified items. |
| Cross-source stable judgment | `wiki/topics/<domain>/` | Write evergreen knowledge from `schema/templates/knowledge.md`. |
| Question-driven analysis | `wiki/research/` | Write research from `schema/templates/research.md` with evidence, judgment, and boundaries. |
| Claim needs runnable validation | `wiki/labs/` | Create only a minimal experiment from `schema/templates/lab.md`. |
| Final report, deck, article, or deliverable | `wiki/outputs/` | Add `manifest.md` from `schema/templates/output-manifest.md`. |
| Reusable process, prompt, or template | `schema/methods/` | Store the method, not one-off content. |
| Repository rules or navigation | `schema/meta/` | Update governance files such as `schema/meta/topic-map.md`. |
| Historical but no longer maintained | `wiki/archive/` | Preserve with a reason and replacement entry. |

If a file seems to fit two places, choose by lifecycle. Theme only decides the subdirectory.

## Automated Capture

When the user gives a URL, video link, WeChat article, GitHub repository, PDF, AI research report, or local file, try to capture it before asking for manual processing. Capture is evidence work, not knowledge work.

Default capture output is one Markdown source document:

```text
raw/sources/<domain>/<source-type>/<YYYY-MM-DD-title-slug>.md
raw/sources/<domain>/<source-type>/<YYYY-MM-DD-title-slug>.assets/
  cover.<ext>
  images/
    001.<ext>
    002.<ext>
```

- The Markdown file contains frontmatter, the captured original content, capture log, and unverified items.
- Use the source material's title for the filename slug when possible. Prefer `YYYY-MM-DD-title-slug.md`.
- Do not create `source.md`, `snapshot.md`, `metadata.json`, or `capture-log.md` by default.
- The same-name `.assets/` directory is optional and only needed for local images or small evidence assets.
- Large video/audio/ASR/bulk screenshots stay under `raw/assets/local-media/` or an external path and are linked from the source document.

If capture fails, still create one source document with `status: capture_failed`, the original URL or path, the failure reason, and the next action. Do not silently drop a source.

Do not create `wiki/notes/`, `wiki/research/`, or `wiki/topics/` during capture unless the user explicitly asks to digest, research, or upgrade the material.

## Capture Workflows

Use `schema/meta/source-types.md` for source type, evidence level, media format, and status values.

### WeChat Articles

For `mp.weixin.qq.com` links, use the `wechat-article-extractor` skill when available.

1. Extract title, author, account, publish time, cover image URL, original URL, source URL, and HTML content.
2. Create one Markdown source document named from the article title.
3. Download cover image to `<slug>.assets/cover.<ext>` when available.
4. Extract body images, download them to `<slug>.assets/images/`, and rewrite the Markdown body to local relative paths.
5. Mark `source_type: wechat_article`, `source_level: secondary`, and `media_format: html`.
6. Record deleted, expired, rate-limited, blocked, or image-download failures in the document's `采集日志`.

### Web Articles and Official Docs

For normal web pages, extract title, author, publish time, canonical URL, main content, cover image, and body images. Use a browser extractor, structured web extraction, or `summarize --extract-only` when appropriate.

- For ordinary blogs/media pages, mark `source_type: web_article` and `source_level: secondary`.
- For official product/API/SDK docs, mark `source_type: official_doc` and `source_level: primary`.
- For unstable facts such as APIs, SDKs, model behavior, prices, laws, or product behavior, add a "需要核验的事实" item requiring current primary-source verification before any wiki claim.

### Image Localization

WeChat and web article capture must localize images by default:

- Download body images; do not rely on remote hotlinks in the source document.
- Name body images by order of appearance: `<slug>.assets/images/001.<ext>`, `<slug>.assets/images/002.<ext>`.
- Save the cover separately as `<slug>.assets/cover.<ext>`.
- In Markdown, use local references such as `![图片 001](<slug>.assets/images/001.jpg)`.
- Record image counts and failures in frontmatter and the `采集日志` section.
- Skip obvious non-content images: avatars, site logos, share icons, tracking pixels, and script/stat images.
- Keep ads, QR codes, and author cards when they appear inside the article body; mark them in `采集日志` as possible non-content material.
- If a body image fails, keep a Markdown placeholder such as `![图片 003 下载失败](<slug>.assets/images/003.missing.md)` and record the original URL and error in `采集日志`.

### Videos

For learning videos or yt-dlp-supported URLs, also use the project `video-to-wiki` skill.

- Default collection mode is capture-only: capture metadata, subtitles or ASR transcript, chapter transcript, keyframes, comments digest, and `asset-manifest.md`.
- Store large assets under `raw/assets/local-media/youtube/<slug>/` unless explicitly using the legacy-compatible `local-media/` path.
- Create one video source document under `raw/sources/<domain>/videos/<YYYY-MM-DD-title-slug>.md` and link to the asset manifest.
- Do not create a `wiki/notes/` video note unless the user explicitly asks to digest or write the note.

### GitHub Repositories

For GitHub repository URLs, default to lightweight analysis. Do not clone, install, run tests, or execute project code unless the user explicitly asks for validation or a lab.

Create one Markdown source document containing:

- owner/repo, description, topics, stars, license, default branch, latest update, README, and top-level tree;
- key manifests when accessible, such as `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `pom.xml`, and `README*`;
- one-line positioning, main capabilities, likely tech stack, initial directory judgment, likely entrypoints, risks, and whether deep research is worth doing.

Mark repository URLs as `source_type: github_repo`, `source_level: primary`, and mark the lightweight analysis itself as unverified.

### AI Research Reports

For Deep Research reports from external AI platforms or temporary Codex/Claude outputs:

- save the report body as the source document's `原始内容`;
- record only basic metadata such as platform, model/tool if known, prompt/topic, generated date, imported date, export format, and original location;
- mark `source_type: ai_report` and `source_level: ai_secondary`;
- do not summarize, critique, verify, extract cited URLs, or create primary-source documents by default;
- when the user explicitly asks to digest or research the report, then extract cited URLs as source clues and decide which primary sources need separate source documents;
- never write AI report conclusions directly into `wiki/topics/`.

Use `source_level: derived` only when the report is a reviewed output from this knowledge base with traceable `source_refs`.

## Workflow

1. Read local context first when needed: `README.md`, `AGENTS.md`, `schema/agent-protocol.md`, `wiki/index.md`, `schema/meta/topic-map.md`, and the target directory README.
2. Decide lifecycle, domain, status, and target path before writing.
3. Use the matching template in `schema/templates/` for new Markdown files.
4. Preserve source traceability with `source_refs`; do not invent sources.
5. Add `未验证事项` when content is based on LLM interpretation, ASR, unrun code, old docs, or unchecked claims.
6. Update `wiki/index.md` and append `wiki/log.md` for ingest, query, lint, migration, and output write-back.
7. Update nearby README or `schema/meta/topic-map.md` only when navigation would otherwise break or a new durable theme appears.
8. In the final response, list created/updated paths, lifecycle classification, verified checks, and remaining unverified items.

## Domain Rules

Use the first-level domains from `schema/meta/topic-map.md`: `ai`, `software-engineering`, `product-business`, `learning-research`, `life`, `reading`, `finance`, `health`, and `misc`.

Do not create a new top-level directory for a theme. Create subdirectories under `raw/`, `wiki/`, or `schema/` only when real material needs them.

## Upgrade Rules

- Upgrade `raw/sources/` to `wiki/notes/` only after the material has been read, watched, or otherwise understood.
- Upgrade `wiki/notes/` to `wiki/topics/` only when the content is stable, reusable, and not just a single-source summary.
- Upgrade `wiki/notes/` or `wiki/topics/` to `wiki/research/` only when there is a clear question being answered.
- Upgrade to `wiki/labs/` only when there is a concrete claim that must be tested by running code or commands.
- After creating `wiki/outputs/`, back-write new stable judgments to `wiki/topics/`, new questions to `wiki/research/`, reusable procedures to `schema/methods/`, and new evidence to `raw/sources/`.

## Special Cases

- For learning videos or yt-dlp-supported URLs, also use the project `video-to-wiki` skill. Store evidence assets under `raw/assets/local-media/`, create one source document under `raw/sources/`, and compile understanding under `wiki/notes/` only when requested. Keep Git focused on Markdown source documents, manifests, and final artifacts. `video-study-notes` is the old skill name; do not add new references to it except compatibility notes.
- For current APIs, SDKs, model behavior, laws, prices, or other unstable facts, verify against current primary sources before writing them as facts.
- For high-risk actions such as shell execution outside a safe context, database writes, email, payment, deployment, or account actions, require explicit human review.
- For old files, do not bulk-add metadata just for consistency. Add metadata only when revising, migrating, or upgrading the file.

## Naming

Prefer:

```text
YYYY-MM-DD-title-slug.md
```

Use concise ASCII slugs for source documents and experiments when practical. Existing Chinese filenames are fine; do not rename old files unless migration or readability requires it.

Top-level directory names are fixed as `raw/`, `wiki/`, and `schema/`. Subdirectories and filenames may use concise ASCII slugs or Chinese titles; choose the name that is clearest for long-term navigation. Obsidian Chinese readability belongs in `00-首页.md`, MOCs, topic maps, and link labels, not in duplicate top-level folders.
