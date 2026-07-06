---
name: convert-strategy-to-speaker-script
description: Deeply analyze a strategy, brand, marketing, GTM, business, consulting, or annual-plan document and convert it into a downloadable Word speaker script that follows the source sequence. Use when the user provides DOCX, PDF, PPTX, or long-form proposal content and asks for a 现场提案口播稿、汇报讲稿、跟页讲稿、顾问式销售话术、提案收网、逐页演讲稿，or wants the same analysis-to-Word workflow used on a previous proposal.
---

# Convert Strategy to Speaker Script

Create a read-aloud, source-aligned proposal script. Preserve the source's node order while adding insight, persuasion, interaction, transitions, and a consultative sales close.

## Required companion skill

Use the `documents` skill for DOCX extraction, creation, and render QA. Announce both skills before acting.

## Workflow

1. Read the complete source, including tables, appendices, budgets, KPIs, roadmaps, and notes. Do not draft from headings alone.
2. Extract the source into a searchable text form. Build a heading index and inspect every section.
3. Read [references/analysis-method.md](references/analysis-method.md). Apply its evidence, contradiction, and storyline analysis.
4. Read [references/consultative-sales.md](references/consultative-sales.md). Use its seven-stage selling path and closing question ladder.
5. Build a source-aligned node map. Each major source node must map to one script node; merge only repetitive detail and never reorder the strategic argument without stating why.
6. Draft the script in the structure defined by [assets/speaker-script-outline.md](assets/speaker-script-outline.md).
7. For every major node, include:
   - 对应展示内容
   - 核心 Insight
   - 可直接朗读的主稿
   - 顾问式追问或确认
   - 承上启下的转场
   - 主持提示 when a number, absolute claim, or delivery risk needs caution
8. Write for speech, not reading comprehension: short paragraphs, controlled rhythm, explicit signposting, and natural Chinese. Do not merely paraphrase the slide.
9. Add the following mandatory end sections:
   - 销售收网：问题选择 → 业务后果 → 不行动代价 → MVP/下一步假设 → 分级承诺
   - 分支追问：品牌、线索、转化、协同数据四类回答
   - 高频异议处理
   - 会前数据与口径核验清单
   - 提案人一页速记
10. Generate a polished DOCX. Use `scripts/build_speaker_docx.py` when its generic layout fits; otherwise use the documents skill's DOCX workflow while preserving the same information hierarchy.
11. Render the DOCX to PNGs, visually inspect every page, fix defects, rerender, and run structural/a11y checks. If the renderer is unavailable or broken, disclose that in the final response.
12. Deliver only the final DOCX unless the user asks for source Markdown or QA artifacts.

## Depth and timing

- Default to 80–100 minutes for a full strategic proposal.
- Estimate speaking time from Chinese character count and interaction pauses; do not claim precision.
- If the source is short, reduce length proportionally rather than padding.
- If the user specifies a duration, calibrate the script to that duration.

## Insight standard

Each section insight must do at least one of the following:

- expose a hidden business consequence;
- reframe a tactical symptom as a strategic problem;
- create a memorable analogy that clarifies the mechanism;
- define a choice or trade-off;
- connect marketing activity to growth, risk, or sales efficiency.

Avoid slogans that merely repeat the heading. Use sharp language selectively; keep the overall tone professional and restrained.

## Evidence discipline

- Distinguish source fact, analysis inference, and recommendation.
- Attribute audit numbers to the source and note the measurement date/tool when available.
- Never upgrade “领先” to “第一”, “少数” to “唯一”, or estimates to official facts.
- Put conflicts, missing sources, inverted baselines, and budget/KPI inconsistencies in the presenter-only verification list.
- Do not silently repair a commercial assumption that materially changes the proposal; flag it.

## Consultative-selling discipline

- Diagnose before presenting services.
- Ask calibration questions throughout, not only at the end.
- Let the client verbalize the problem and its business consequence.
- Do not jump from strategy to “是否签约”. Use a commitment ladder: agree on problem → agree on priority → agree on test → agree on owner/date/input.
- Prefer a bounded MVP when uncertainty is high. Define what it must learn, not only what it must deliver.
- Close with three concrete decisions: scope/market, owner, and next meeting date.

## Output quality gates

Before delivery, verify:

- The script follows the source sequence and covers all major sections.
- Every major node has an insight, read-aloud copy, question, and transition.
- The close elicits the client's own growth bottleneck and next-step commitment.
- Numbers and claims are internally consistent or flagged.
- No tool tokens, placeholders, fake citations, or Markdown residue remain.
- Headings, numbered lists, tables, callouts, headers, and footers are native Word structures.
- The final file is linked with an absolute `sandbox:` path.

