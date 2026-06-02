---
name: knowledge-base-workflow
description: Organize materials into this repository's Karpathy-style LLM Wiki lifecycle. Use when Codex needs to ingest, classify, summarize, digest, migrate, upgrade, or route links, PDFs, videos, books, articles, notes, watchlists, research drafts, experiments, outputs, templates, or user ideas in this repo; decide between raw/inbox, raw/sources, wiki/notes, wiki/topics, wiki/research, wiki/labs, schema/methods, wiki/outputs, schema/meta, and wiki/archive; update source cards, notes, manifests, topic maps, wiki index, or wiki log.
---

# Knowledge Base Workflow

Use this skill to turn incoming material into durable knowledge in this repository. The core rule is: do not store material as a collection item; compile it from `raw/` into `wiki/` under the rules in `schema/`.

## Decision Tree

Classify lifecycle before theme:

| Current state | Home | Required action |
| --- | --- | --- |
| Raw clue, idea, or unprocessed link | `raw/inbox/` | Capture briefly; do not pretend it is knowledge. |
| Source worth preserving but not digested | `raw/sources/<domain>/` | Create a source card from `schema/templates/source-card.md`. |
| Read, watched, or understood material | `wiki/notes/<domain-or-topic>/` | Write a note from `schema/templates/note.md` with own understanding and unverified items. |
| Cross-source stable judgment | `wiki/topics/<domain>/` | Write evergreen knowledge from `schema/templates/knowledge.md`. |
| Question-driven analysis | `wiki/research/` | Write research from `schema/templates/research.md` with evidence, judgment, and boundaries. |
| Claim needs runnable validation | `wiki/labs/` | Create only a minimal experiment from `schema/templates/lab.md`. |
| Final report, deck, article, or deliverable | `wiki/outputs/` | Add `manifest.md` from `schema/templates/output-manifest.md`. |
| Reusable process, prompt, or template | `schema/methods/` | Store the method, not one-off content. |
| Repository rules or navigation | `schema/meta/` | Update governance files such as `schema/meta/topic-map.md`. |
| Historical but no longer maintained | `wiki/archive/` | Preserve with a reason and replacement entry. |

If a file seems to fit two places, choose by lifecycle. Theme only decides the subdirectory.

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

- For learning videos or yt-dlp-supported URLs, also use the project `video-study-notes` skill. Store media assets under `raw/assets/local-media/`, old-compatible `local-media/`, or external paths; keep Git focused on Markdown, source cards, and final artifacts.
- For current APIs, SDKs, model behavior, laws, prices, or other unstable facts, verify against current primary sources before writing them as facts.
- For high-risk actions such as shell execution outside a safe context, database writes, email, payment, deployment, or account actions, require explicit human review.
- For old files, do not bulk-add metadata just for consistency. Add metadata only when revising, migrating, or upgrading the file.

## Naming

Prefer:

```text
YYYY-MM-DD-topic.md
```

Use concise ASCII slugs for new source cards and experiments when practical. Existing Chinese filenames are fine; do not rename old files unless migration or readability requires it.

Top-level directory names are fixed as `raw/`, `wiki/`, and `schema/`. Subdirectories and filenames may use concise ASCII slugs or Chinese titles; choose the name that is clearest for long-term navigation. Obsidian Chinese readability belongs in `00-首页.md`, MOCs, topic maps, and link labels, not in duplicate top-level folders.
