---
name: knowledge-base-workflow
description: Organize materials into this repository's personal LLM knowledge base lifecycle. Use when Codex needs to ingest, classify, summarize, digest, migrate, upgrade, or route links, PDFs, videos, books, articles, notes, watchlists, research drafts, experiments, outputs, templates, or user ideas in this repo; decide between 00-收件箱, 10-来源索引, 20-资料笔记, 30-稳定知识, 40-问题研究, 50-实验验证, 60-方法库, 70-输出成品, 80-仓库治理, and 90-历史归档; update source cards, notes, manifests, topic maps, or lifecycle indexes.
---

# Knowledge Base Workflow

Use this skill to turn incoming material into durable knowledge in this repository. The core rule is: do not store material as a collection item; compile it through the lifecycle.

## Decision Tree

Classify lifecycle before theme:

| Current state | Home | Required action |
| --- | --- | --- |
| Raw clue, idea, or unprocessed link | `00-收件箱/` | Capture briefly; do not pretend it is knowledge. |
| Source worth preserving but not digested | `10-来源索引/<domain>/` | Create a source card from `60-方法库/templates/source-card.md`. |
| Read, watched, or understood material | `20-资料笔记/<domain>/` | Write a note from `60-方法库/templates/note.md` with own understanding and unverified items. |
| Cross-source stable judgment | `30-稳定知识/<domain>/` | Write evergreen knowledge from `60-方法库/templates/knowledge.md`. |
| Question-driven analysis | `40-问题研究/` | Write research from `60-方法库/templates/research.md` with evidence, judgment, and boundaries. |
| Claim needs runnable validation | `50-实验验证/` | Create only a minimal experiment from `60-方法库/templates/lab.md`. |
| Final report, deck, article, or deliverable | `70-输出成品/` | Add `manifest.md` from `60-方法库/templates/output-manifest.md`. |
| Reusable process, prompt, or template | `60-方法库/` | Store the method, not one-off content. |
| Repository rules or navigation | `80-仓库治理/` | Update governance files such as `80-仓库治理/topic-map.md`. |
| Historical but no longer maintained | `90-历史归档/` | Preserve with a reason and replacement entry. |

If a file seems to fit two places, choose by lifecycle. Theme only decides the subdirectory.

## Workflow

1. Read local context first when needed: `README.md`, `AGENTS.md`, `80-仓库治理/topic-map.md`, and the target directory README.
2. Decide lifecycle, domain, status, and target path before writing.
3. Use the matching template in `60-方法库/templates/` for new Markdown files.
4. Preserve source traceability with `source_refs`; do not invent sources.
5. Add `未验证事项` when content is based on LLM interpretation, ASR, unrun code, old docs, or unchecked claims.
6. Update nearby README or `80-仓库治理/topic-map.md` only when navigation would otherwise break or a new durable theme appears.
7. In the final response, list created/updated paths, lifecycle classification, verified checks, and remaining unverified items.

## Domain Rules

Use the first-level domains from `80-仓库治理/topic-map.md`: `ai`, `software-engineering`, `product-business`, `learning-research`, `life`, `reading`, `finance`, `health`, and `misc`.

Do not create a new top-level directory for a theme. Create subdirectories under lifecycle directories only when real material needs them.

## Upgrade Rules

- Upgrade `10-来源索引/` to `20-资料笔记/` only after the material has been read, watched, or otherwise understood.
- Upgrade `20-资料笔记/` to `30-稳定知识/` only when the content is stable, reusable, and not just a single-source summary.
- Upgrade `20-资料笔记/` or `30-稳定知识/` to `40-问题研究/` only when there is a clear question being answered.
- Upgrade to `50-实验验证/` only when there is a concrete claim that must be tested by running code or commands.
- After creating `70-输出成品/`, back-write new stable judgments to `30-稳定知识/`, new questions to `40-问题研究/`, reusable procedures to `60-方法库/`, and new evidence to `10-来源索引/`.

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

Top-level lifecycle directory names are fixed Chinese numbered names. Subdirectories and filenames may use concise ASCII slugs or Chinese titles; choose the name that is clearest for long-term navigation.
