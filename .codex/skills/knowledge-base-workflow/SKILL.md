---
name: knowledge-base-workflow
description: Organize materials into this repository's personal LLM knowledge base lifecycle. Use when Codex needs to ingest, classify, summarize, digest, migrate, upgrade, or route links, PDFs, videos, books, articles, notes, watchlists, research drafts, experiments, outputs, templates, or user ideas in this repo; decide between inbox, sources, notes, knowledge, research, labs, methods, outputs, meta, and archive; update source cards, notes, manifests, topic maps, or lifecycle indexes.
---

# Knowledge Base Workflow

Use this skill to turn incoming material into durable knowledge in this repository. The core rule is: do not store material as a collection item; compile it through the lifecycle.

## Decision Tree

Classify lifecycle before theme:

| Current state | Home | Required action |
| --- | --- | --- |
| Raw clue, idea, or unprocessed link | `inbox/` | Capture briefly; do not pretend it is knowledge. |
| Source worth preserving but not digested | `sources/<domain>/` | Create a source card from `methods/templates/source-card.md`. |
| Read, watched, or understood material | `notes/<domain>/` | Write a note from `methods/templates/note.md` with own understanding and unverified items. |
| Cross-source stable judgment | `knowledge/<domain>/` | Write evergreen knowledge from `methods/templates/knowledge.md`. |
| Question-driven analysis | `research/` | Write research from `methods/templates/research.md` with evidence, judgment, and boundaries. |
| Claim needs runnable validation | `labs/` | Create only a minimal experiment from `methods/templates/lab.md`. |
| Final report, deck, article, or deliverable | `outputs/` | Add `manifest.md` from `methods/templates/output-manifest.md`. |
| Reusable process, prompt, or template | `methods/` | Store the method, not one-off content. |
| Repository rules or navigation | `meta/` | Update governance files such as `meta/topic-map.md`. |
| Historical but no longer maintained | `archive/` | Preserve with a reason and replacement entry. |

If a file seems to fit two places, choose by lifecycle. Theme only decides the subdirectory.

## Workflow

1. Read local context first when needed: `README.md`, `AGENTS.md`, `meta/topic-map.md`, and the target directory README.
2. Decide lifecycle, domain, status, and target path before writing.
3. Use the matching template in `methods/templates/` for new Markdown files.
4. Preserve source traceability with `source_refs`; do not invent sources.
5. Add `未验证事项` when content is based on LLM interpretation, ASR, unrun code, old docs, or unchecked claims.
6. Update nearby README or `meta/topic-map.md` only when navigation would otherwise break or a new durable theme appears.
7. In the final response, list created/updated paths, lifecycle classification, verified checks, and remaining unverified items.

## Domain Rules

Use the first-level domains from `meta/topic-map.md`: `ai`, `software-engineering`, `product-business`, `learning-research`, `life`, `reading`, `finance`, `health`, and `misc`.

Do not create a new top-level directory for a theme. Create subdirectories under lifecycle directories only when real material needs them.

## Upgrade Rules

- Upgrade `sources/` to `notes/` only after the material has been read, watched, or otherwise understood.
- Upgrade `notes/` to `knowledge/` only when the content is stable, reusable, and not just a single-source summary.
- Upgrade `notes/` or `knowledge/` to `research/` only when there is a clear question being answered.
- Upgrade to `labs/` only when there is a concrete claim that must be tested by running code or commands.
- After creating `outputs/`, back-write new stable judgments to `knowledge/`, new questions to `research/`, reusable procedures to `methods/`, and new evidence to `sources/`.

## Special Cases

- For learning videos or yt-dlp-supported URLs, also use the project `video-study-notes` skill. Store media assets under `local-media/`; keep Git focused on Markdown, source cards, and final artifacts.
- For current APIs, SDKs, model behavior, laws, prices, or other unstable facts, verify against current primary sources before writing them as facts.
- For high-risk actions such as shell execution outside a safe context, database writes, email, payment, deployment, or account actions, require explicit human review.
- For old files, do not bulk-add metadata just for consistency. Add metadata only when revising, migrating, or upgrading the file.

## Naming

Prefer:

```text
YYYY-MM-DD-topic.md
```

Use concise ASCII slugs for new source cards and experiments when practical. Existing Chinese filenames are fine; do not rename old files unless migration or readability requires it.

Top-level lifecycle directory names are fixed original English paths. Subdirectories and filenames may use concise ASCII slugs or Chinese titles; choose the name that is clearest for long-term navigation. Obsidian Chinese readability belongs in `00-首页.md`, MOCs, topic maps, and link labels, not in duplicate top-level folders.
