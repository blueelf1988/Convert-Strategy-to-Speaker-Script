# convert-strategy-to-speaker-script

<p align="center">
  <b>中文</b> | <a href="#english">English</a>
</p>

将战略方案、品牌方案、营销提案或商业计划，深度分析并转化为一份可跟随原方案逐页展示、可直接朗读的顾问式销售 Word 口播稿。

> 核心原则：不是把方案内容重新念一遍，而是帮助提案人把问题讲透、把价值讲清，并推动客户表达真实业务瓶颈与下一步行动意愿。

当前版本：`v2.0.0`

---

<h2 id="english">convert-strategy-to-speaker-script (English)</h2>

Deeply analyze a strategy, brand, marketing, GTM, business, or consulting document and convert it into a downloadable Word speaker script — ready to read aloud slide-by-slide. Preserves source sequence while adding punchline insights, consultative questions, smooth transitions, and a structured consultative sales close.

> Core principle: Don't just read the slides back. Help the presenter make the case sharper, draw the client into the diagnosis, and move toward concrete next-step commitment.

Current version: `v2.0.0`

---

## 1. Skill 简介 / What This Skill Does

`convert-strategy-to-speaker-script` 是一个面向战略咨询、品牌营销、GTM、年度规划和商业提案场景的 Codex Skill。

它能够读取完整方案（含表格、附录、预算、KPI、Roadmap），提炼各章节的核心洞察，识别数据与逻辑风险，并保持原方案展示顺序，将内容转化为：

- 可跟随方案逐页或逐章节朗读的现场口播稿；
- 具有咨询顾问逻辑的结论先行表达；
- 每一页附有 **「Insight」**——一句不重复主稿的犀利金句，供提案人现场画龙点睛；
- 全程穿插 **「追问」**，持续邀请客户参与诊断、表达真实痛点和后果；
- 从问题共识自然推进到 MVP、试点或合作下一步的 **「销售收网」**；
- 完整的 **收网工具包**：分支追问、高频异议处理、会前核验清单、提案人一页速记；
- 经过结构化排版、符合视觉规范、可直接下载和使用的 Word 文档。


默认适用于约 **80–100 分钟**的完整战略提案，也可以根据用户指定时长压缩或扩展。  


---

## 2. V2 核心变更 / What's New in V2

V2 将节点顺序从「Insight 前置」改为「**主稿先行 + 点睛 Insight 后置**」，解决了旧版 Insight 与主稿内容重复、提案人不知道该不该朗读的问题。点睛 Insight 不再做段落式分析，而是改为一句不重复主稿的犀利金句，供提案人在读完主稿后临场画龙点睛。同步调整了视觉配色（点睛 Insight 浅蓝底金框、追问浅紫底紫框）和正文行间距（1.2×）。

---

## 3. 节点结构 / Node Structure (V2)

每个 Slide 节点严格按以下顺序编排：

| # | 元素 | 设计意图 |
|---|---|---|
| 1 | **【对应展示内容】** | PPT 画面参考，提案人确认当前页 |
| 2 | **【可直接朗读的主稿】** | 口播正文，口语化中文，短段落，明确路标 |
| 3 | **【Insight】** | 一句话犀利总结，画龙点睛，不重复、不剧透 |
| 4 | **【追问】** 或 **【顾问式确认】** | 让客户参与诊断，说出自己的痛点和业务后果 |
| 5 | **【转场】** | 自然过渡到下一页，不生硬 |
| 6 | **【⚠主持提示】** (可选) | 数据核实、节奏控制、风险提示——仅提案人看，不朗读 |

### 现场使用流程 / Presenter's Flow

```
看【对应展示内容】确认 PPT 画面
  ↓
朗读【可直接朗读的主稿】
  ↓
扫一眼【点睛 Insight】→ 临场发挥一句收尾（念出来或自己说）
  ↓
抛出【❓ 追问】→ 等待客户回应
  ↓
用【↪ 转场】自然翻到下一页
```

---

## 4. 适用场景 / When to Use

当用户提供以下材料并要求生成讲稿时，调用本 Skill：

- 海外品牌战略或品牌升级方案；
- 数字营销、社媒、内容或媒介推广方案；
- GTM、市场进入与业务增长方案；
- 年度营销规划、IMC 或整合传播方案；
- 咨询项目、董事会汇报或管理层决策方案；
- 招投标提案、客户比稿或商务合作方案；
- 商业计划书、融资方案或战略路线图；
- 需要从「方案解读」升级为「顾问式销售提案」的其他材料。

支持的常见输入格式：

- `.docx`
- `.pdf`
- `.pptx`
- Markdown 或纯文本
- 已粘贴在对话中的长篇方案内容

典型触发表达：

- `/convert-strategy-to-speaker-script 把这份方案生成一份现场提案口播稿`
- “跟随 PPT 顺序，写一份我可以直接读的讲稿”
- “用顾问式销售方法讲这份品牌方案”
- “提炼每个章节的点睛 Insight，并在最后完成销售收网”
- “沿用之前十三行的相同方法，把新方案转成 Word 口播稿”

---

## 5. 核心能力 / Core Capabilities

### 5.1 全文深度分析 / Full-Document Deep Analysis

不会只读取目录或标题，而是检查：

- 战略诊断与核心矛盾；
- 市场、竞品、客户与决策链；
- 品牌定位、USP、价值体系与信息架构；
- 内容、渠道、媒介与执行节奏；
- Roadmap、预算、KPI 与双方协作；
- 表格、附录、备注和隐藏在细节中的商业假设。

### 5.2 证据分层 / Evidence Grading

| 类型 | 定义 | 现场表达方式 |
|---|---|---|
| Fact | 方案明确给出的事实或审计数据 | 保留来源、时间和限定条件 |
| Inference | 从事实中推导出的策略判断 | 使用"这意味着""我们的判断是" |
| Recommendation | 对未来行动的建议 | 使用"建议""优先""可以验证" |
| Assumption | 尚未核实的市场或商业假设 | 放入会前核验，不作为确定事实承诺 |

### 5.3 点睛 Insight 标准 / Punchline Insight Standard

每条「点睛 Insight」必须满足：

- ✅ **一句话**，不写段落
- ✅ **不重复主稿内容**——只加锐度，不加废话
- ✅ 至少做到一项：
  - 暴露隐藏的商业后果
  - 把战术症状重构为战略问题
  - 用类比点明关键机制
  - 明确资源取舍
  - 将营销动作连接到增长、风险或销售效率
- ❌ 不做「标题复读机」
- ❌ 不用 emoji 前缀

示例：

> 主稿说：「十三行不缺货、不缺商户、不缺历史，真正缺的是系统化连接。」
>
> 点睛 Insight：「这六个断层像六根断掉的电线——电流本身是有的，但到不了终端用户。我们的工作不是发电，是接线。」

### 5.4 顾问式销售叙事 / Consultative Selling Narrative

采用七阶段提案路径：

1. 建立共同目标；
2. 重构客户问题；
3. 用证据完成诊断；
4. 放大不行动的代价；
5. 共创增长标准；
6. 用 MVP 或阶段方案降低风险；
7. 引导客户做出下一步行动承诺。

### 5.5 销售收网 / Sales Close

结尾不会直接跳到"是否签约"，而是通过承诺阶梯推进：

1. 让客户用自己的语言确认问题；
2. 确认维持现状的业务代价；
3. 确认优先市场、产品或客户；
4. 确认试点假设与成功标准；
5. 确认客户侧 Owner 与必要输入；
6. 确认下一次工作坊或启动会日期。

### 5.6 跟踪原方案顺序 / Source-Aligned

默认保留原方案章节与节点顺序，不另起一套脱离 PPT 的故事线。如需重新编排战略论点，必须在稿件中明确说明原因。

---

## 6. DOCX 输出规范 / DOCX Output Specification

### 6.1 视觉配色 / Color Scheme

| 元素 | 背景色 | 左边框 | 标签色 |
|---|---|---|---|
| 点睛 Insight | `#E8F0FE` 浅蓝 | `#C59B3C` 金色 8px | `#C59B3C` 金色 |
| ❓ 追问 | `#F3E5F5` 浅紫 | `#7B1FA2` 紫色 8px | `#7B1FA2` 紫色 |
| ↪ 转场 | `#FAF3E0` 浅暖 | `#E0A800` 琥珀色 8px | `#B8860B` 深琥珀 |
| ⚠ 主持提示 | 无 | 无 | `#999999` 灰色斜体 |

### 6.2 排版规范 / Typography

- 默认字体：微软雅黑 (Microsoft YaHei), 11pt (size 22 half-points)
- **正文行间距：1.2×** (line: 288 twips)
- 段落前后间距：60 twips
- H1：18pt 深蓝 `#1B2A4A`，章节标题加金色底线
- H2：15pt 深蓝
- H3：13pt `#8B1E1E`
- 缩进块：左右各 200 twips

### 6.3 输出结构 / Document Structure

```text
一、封面（标题 + 副标题 + 英文 tagline + 提案方 + 预计时长）
二、使用说明（节点结构解释 + 现场使用流程）
三、逐页/逐章节现场提案口播稿（Part 0-10，每个节点按 V2 结构编排）
四、销售收网（6 步承诺阶梯）
五、分支追问（品牌 / 线索 / 转化 / 协同数据四类）
六、高频异议处理
七、会前数据与口径核验清单
八、提案人一页速记
```

---

## 7. 安装与使用 / Installation & Usage

### 7.1 支持的 AI Agent 平台 / Supported AI Agent Platforms

本 Skill 可在以下 AI Agent 平台中安装和使用：

| 平台 / Platform | 安装方式 / Installation |
|---|---|
| **Claude Code** (Anthropic) | 将 Skill 目录复制到 Claude Code Skills 路径。可作为 Slash Command 或自然语言触发。 |
| **Claude Desktop** (Anthropic) | 通过 Claude Desktop 的 Skills 管理面板上传 Skill 目录。触发方式：自然语言（如"把这份方案转成口播稿"）。 |
| **Codex** (OpenAI) | 将 Skill 目录复制到 `${CODEX_HOME:-$HOME/.codex}/skills/`。可通过 `$` 前缀显式调用或自然语言触发。 |
| **Cursor** | 将 SKILL.md 添加到项目 `.cursorrules` 或 Workspace Rules 中；配合 npm `docx` 库即可生成 DOCX。 |

### 7.2 各平台安装步骤 / Platform-Specific Setup

#### Claude Code

```bash
# 从 GitHub 克隆
git clone https://github.com/YOUR_USERNAME/convert-strategy-to-speaker-script.git

# 复制到 Claude Code Skills 目录
cp -R convert-strategy-to-speaker-script \
  ~/.claude/skills/
```

重启 Claude Code 后，Skill 自动被发现。使用方式：

```text
/convert-strategy-to-speaker-script 将附件方案转为现场提案口播稿
```

或直接用自然语言描述需求，Skill 会自动匹配触发。

#### Claude Desktop

1. 打开 Claude Desktop → Settings → Skills
2. 点击「Add Skill」→ 选择 `convert-strategy-to-speaker-script` 目录
3. 确认安装

安装后，在对话中上传方案文件并说"帮我把这份方案转成口播稿"即可触发。

#### Codex (OpenAI)

```bash
git clone https://github.com/YOUR_USERNAME/convert-strategy-to-speaker-script.git

cp -R convert-strategy-to-speaker-script \
  "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重启 Codex 会话后生效。显式调用：

```text
$convert-strategy-to-speaker-script 分析附件，生成现场提案口播 Word 稿
```

#### Cursor

1. 将本仓库克隆到本地
2. 打开项目，在 `.cursorrules` 或 Cursor Settings → Rules for AI 中添加 `SKILL.md` 的内容
3. 安装 DOCX 生成依赖：

```bash
npm install docx
```

使用方式：在 Cursor Chat 中上传方案文件，描述需求即可。

### 7.3 依赖项 / Dependencies

生成 DOCX 需要：

- **Node.js** 18+ 且已安装 `npm install docx`
- PDF 渲染 QA（可选）：LibreOffice (`soffice`) + Poppler (`pdftoppm`)

### 7.2 使用方式 / How to Use

**显式调用（各平台通用）：**

在对话中上传方案文件后输入自然语言指令即可，Skill 自动匹配触发：

```text
/convert-strategy-to-speaker-script 将附件方案转为现场提案口播稿
```

或在对话中说：

```text
使用 convert-strategy-to-speaker-skill，
深度分析这份方案，按照原方案顺序生成一份可直接朗读的
顾问式销售现场口播稿，最终交付可下载的 Word 版本。
```

### 7.3 常用用法示例 / Common Usage Patterns

**指定提案时长：**

```text
将附件转为一份 60 分钟现场提案口播稿。
保留所有关键洞察，但压缩执行细节。
```

**面向高层汇报：**

```text
面向董事长和管理层重写口播稿。
结论先行、逻辑克制，每个 Part 的点睛 Insight 要有决策启发性。
```

**强化收网：**

```text
重点加强最后 15 分钟的顾问式提问、异议处理和销售收网，
推动客户明确业务瓶颈、MVP 范围、项目 Owner 和下一次会议时间。
```

**分批输出确认风格：**

```text
先输出 Part 0–Part 2 的口播稿供我确认风格，
确认后再继续其他部分。
```

---

## 8. 自定义与扩展 / Customization

### 修改分析方法

编辑 `references/analysis-method.md` 可以增加企业内部的诊断模型、行业研究标准或数据分类方法。

### 修改销售方法

编辑 `references/consultative-sales.md` 可以加入 SPIN、Challenger Sale、价值销售等面向决策者听众的提案方法，或企业自有销售框架。

### 修改口播稿骨架

编辑 `assets/speaker-script-outline.md` 可以调整固定章节、提问结构、异议类型和收网动作。

### 修改 Word 视觉规范

在 SKILL.md 中更新「DOCX visual style」部分的配色和排版参数，Skill 会在下次生成时自动应用。

---

## 9. 版本历史 / Version History

| 版本 | 日期 | 变更 |
|---|---|---|
| **v2.0.0** | 2026-07-06 | **主稿先行 + 点睛 Insight 后置**；Insight 改为一句犀利金句不重复主稿；新配色（浅蓝 Insight / 浅紫追问）；1.2× 行间距；去掉 Insight emoji 前缀；更新输出质量检查清单 |
| v1.0.0 | 2026-06 | 初始版本：Insight 前置结构，段落式 Insight，米黄+浅蓝配色，默认行间距 |

---

## 10. Known Limitations / 已知限制

- 输入方案质量会直接影响结论质量；缺少事实或数据时，Skill 只能提出假设与核验问题。
- 无法替代客户内部对技术、案例、预算与商业承诺的最终确认。
- 高客单价 B2B 成交受产品、价格、交付、销售响应和市场周期共同影响，不应承诺无条件成交结果。
- DOCX 渲染结果可能因本机字体和 LibreOffice/Word 版本不同而略有差异。
- 当前主要面向中文提案稿；复杂多语言排版需要进一步适配。

---

## 11. Roadmap

计划中的潜在增强方向：

- [ ] 30 / 60 / 90 分钟自动压缩模式
- [ ] 中英双语口播稿
- [ ] PPT 页码与口播节点自动映射
- [ ] 不同行业的专业提案语料库
- [ ] SPIN / Challenger / MEDDICC 可选销售框架
- [ ] 自动生成提案人 Cue Card
- [ ] 自动计算预计口播时长
- [ ] DOCX 主题色和品牌模板参数化
- [ ] 自动输出"高层精简版 + 完整版"双版本

---

## 12. 贡献指南 / Contributing

欢迎通过 Issue 或 Pull Request 提交：

- 新的分析框架
- 新的顾问式销售问题
- 行业专用版本
- Word 生成与排版改进
- 测试案例与质量评估标准
- Bug 修复和文档优化

提交 Pull Request 时建议说明：

1. 解决了什么问题
2. 修改了哪些文件
3. 是否改变现有输出行为
4. 使用什么方案完成测试
5. 是否生成并检查了 Word 文档

> 不要在公开测试材料中提交客户机密、未公开预算、个人信息或受 NDA 保护的方案。

---

## 13. License

当前仓库在正式公开前应补充 `LICENSE` 文件。如果希望任何人都可以使用、修改与分发，通常可选择 MIT License。

---

## 14. 致谢 / Acknowledgments

本 Skill 面向真实的品牌海外整合营销战略提案现场而设计，强调三项能力：

1. 对方案内容的深度理解；
2. 对管理层决策逻辑的清晰表达；
3. 将策略提案自然转化为顾问式销售对话。

如果这个 Skill 帮助你的方案从"被听完"升级为"被理解、被讨论、被推动"，它就完成了自己的任务。
