---
name: "convert-strategy-to-speaker-script"
description: "V2: Deeply analyze a strategy document and convert it into a downloadable Word speaker script (现场提案口播稿) with main-script-first layout, punchline insights, and consultative sales framework. Supports SPIN, Challenger Sale, value-based selling methodologies."
---

---
name: convert-strategy-to-speaker-script
description: Deeply analyze a strategy, brand, marketing, GTM, business, consulting, or annual-plan document and convert it into a downloadable Word speaker script that follows the source sequence. Use when the user provides DOCX, PDF, PPTX, or long-form proposal content and asks for a 现场提案口播稿、汇报讲稿、跟页讲稿、顾问式销售话术、提案收网、逐页演讲稿，or wants the same analysis-to-Word workflow used on a previous proposal.
---

# Convert Strategy to Speaker Script

Create a read-aloud, source-aligned proposal speaker script. Preserve the source's node order while adding punchline insights, persuasion, interactive questions, transitions, and a consultative sales close.

## Required companion skill

Use the `docx` skill for DOCX creation and render QA. Announce both skills before acting.

## Workflow

1. Read the complete source, including tables, appendices, budgets, KPIs, roadmaps, and notes. Do not draft from headings alone.
2. Extract the source into a searchable text form. Build a heading index and inspect every section.
3. Build a source-aligned node map. Each major source node must map to one script node; merge only repetitive detail and never reorder the strategic argument without stating why.
4. Draft the script with the node structure defined below.
5. Write for speech, not reading comprehension: short paragraphs, controlled rhythm, explicit signposting, and natural Chinese. Do not merely paraphrase the slide.
6. Add the following mandatory end sections:
   - 销售收网：问题选择 → 业务后果 → 不行动代价 → MVP/下一步假设 → 分级承诺
   - 分支追问：品牌、线索、转化、协同数据四类回答
   - 高频异议处理
   - 会前数据与口径核验清单
   - 提案人一页速记
7. Generate a polished DOCX using the `docx` skill's DOCX workflow (npm `docx` library).
8. Render the DOCX to PNGs, visually inspect every page, fix defects, rerender. If the renderer is unavailable or broken, disclose that in the final response.
9. Deliver only the final DOCX unless the user asks for source Markdown or QA artifacts.

## Node structure (V2: Main-script-first + Punchline insight)

Every major slide node must include these elements, in this order:

1. **【对应展示内容】** — What the slide/page shows. Brief reference for presenter alignment.
2. **【可直接朗读的主稿】** — The read-aloud script. Natural spoken Chinese, short paragraphs, explicit signposting. This is the primary content the presenter delivers.
3. **【点睛 Insight】** — A single sharp punchline sentence placed AFTER the main script. It must NOT repeat the main script content. Instead, it adds a deeper angle: a hidden consequence, a reframe, a memorable analogy, a trade-off, or a connection to growth/risk/efficiency. The presenter scans this after finishing the main script and delivers it as a closing punchline — or adapts it into their own words on the fly. Label: `点睛 Insight：` (no emoji prefix).
4. **【❓ 追问】or【顾问式确认】** — Interactive question to draw the client into verbalizing the problem. Calibrate throughout, not only at the end.
5. **【↪ 转场】** — Bridge to the next slide. Natural, never mechanical.
6. **【⚠ 主持提示】** (optional) — When a number, absolute claim, or delivery risk needs caution.

### Why this order matters

The presenter's flow: read the main script → glance at the punchline insight → deliver a sharp closing remark → engage the client with a question → transition. Putting Insight before the main script (old V1 approach) caused confusion — the presenter didn't know whether to read Insight aloud, and the Insight often duplicated the main script. The V2 structure fixes both problems: Insight is a distinct punchline that sharpens what was just said, never repeats it.

## DOCX visual style

### Color scheme

| Element | Background | Left border | Label color |
|---|---|---|---|
| 点睛 Insight | `#E8F0FE` (light blue) | `#C59B3C` (gold, 8px) | `#C59B3C` (gold) |
| ❓ 追问 | `#F3E5F5` (light purple) | `#7B1FA2` (purple, 8px) | `#7B1FA2` (purple) |
| ↪ 转场 | `#FAF3E0` (light warm) | `#E0A800` (amber, 8px) | `#B8860B` (dark amber) |
| 主持提示 | n/a | n/a | `#999999` (gray, italic) |

### Typography & spacing

- Default font: Microsoft YaHei (微软雅黑), 11pt (size 22 half-points)
- Body text line spacing: 1.2× (line: 288 twips)
- Headings: Heading 1 (18pt, dark blue `#1B2A4A`), Heading 2 (15pt), Heading 3 (13pt, `#8B1E1E`)
- Section titles: Heading 1 with bottom gold border
- Indented blocks: 200 twips left indent, 200 twips right indent
- Spacing between body paragraphs: 60 twips before/after

### Document structure

- Cover page: Proposal title + subtitle + English tagline + presenter info + estimated duration
- Usage guide page: How to use the script, node structure explanation
- Main content: Part 0 through Part 10, each node following the V2 structure
- Sales close (销售收网): 6-step commitment ladder
- Branching questions (分支追问): By client concern area
- Objection handling (高频异议处理): Top 5 objections with responses
- Pre-meeting verification checklist (会前数据与口径核验清单)
- Presenter one-page cheat sheet (提案人一页速记)

## Depth and timing

- Default to 80–100 minutes for a full strategic proposal.
- Estimate speaking time from Chinese character count and interaction pauses; do not claim precision.
- If the source is short, reduce length proportionally rather than padding.
- If the user specifies a duration, calibrate the script to that duration.

## Punchline insight standard

Each 点睛 Insight must be a SINGLE sentence that does at least one of the following:

- exposes a hidden business consequence;
- reframes a tactical symptom as a strategic problem;
- creates a memorable analogy that clarifies the mechanism;
- defines a choice or trade-off;
- connects marketing activity to growth, risk, or sales efficiency.

**Critical rule:** The 点睛 Insight must NEVER repeat or paraphrase the main script. It must add sharpness that the main script did not already state. Think of it as the "mic drop" after the main delivery — one sentence that makes the client lean forward.

Avoid slogans that merely repeat the heading. The overall tone is professional and restrained, but the punchline can use sharper language selectively.

## Evidence discipline

- Distinguish source fact, analysis inference, and recommendation.
- Attribute audit numbers to the source and note the measurement date/tool when available.
- Never upgrade "领先" to "第一", "少数" to "唯一", or estimates to official facts.
- Put conflicts, missing sources, inverted baselines, and budget/KPI inconsistencies in the presenter-only verification list.
- Do not silently repair a commercial assumption that materially changes the proposal; flag it.

## Consultative-selling discipline

The default consultative sales framework is a seven-stage proposal path (references/consultative-sales.md). Users may customize this reference file to adopt SPIN, Challenger Sale, value-based selling, or their organization's proprietary sales methodology — all tailored for decision-maker audiences in proposal settings.

- Diagnose before presenting services.
- Ask calibration questions throughout, not only at the end.
- Let the client verbalize the problem and its business consequence.
- Do not jump from strategy to "是否签约". Use a commitment ladder: agree on problem → agree on priority → agree on test → agree on owner/date/input.
- Prefer a bounded MVP when uncertainty is high. Define what it must learn, not only what it must deliver.
- Close with three concrete decisions: scope/market, owner, and next meeting date.

## Output quality gates

Before delivery, verify:

- The script follows the source sequence and covers all major sections.
- Every major node follows the V2 structure: 对应展示内容 → 主稿 → 点睛 Insight → 追问 → 转场.
- Every 点睛 Insight is a single sharp sentence that does NOT repeat the main script.
- The close elicits the client's own growth bottleneck and next-step commitment.
- Numbers and claims are internally consistent or flagged.
- No tool tokens, placeholders, fake citations, or Markdown residue remain.
- Headings, numbered lists, tables, callouts, headers, and footers are native Word structures.
- Visual colors match the scheme defined above (light blue for Insight, light purple for 追问).
- Body text line spacing is 1.2× (line: 288 twips), not the default 1.5×.
- The final file is linked with an absolute `sandbox:` path.
