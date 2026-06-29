# Codex Academic Paper Skills

面向 Codex / Codex CLI 的本科软件工程论文技能包，聚焦“基于真实项目仓库完成论文规划、定稿改写、降查重、降 AIGC、图表恢复、运行截图补充、DOCX 收口”这类高频任务。

## 来源说明

本仓库在源项目基础上整理、扩展并开源发布，已明确保留来源标记以尊重原创者。

- 源项目：[`lishix520/academic-paper-skills`](https://github.com/lishix520/academic-paper-skills/)
- 当前仓库主要是在实际使用过程中，对学术论文相关 skills、references、prompt 模板、`agents/openai.yaml` 元数据和改稿流程做了补充与适配
- 如果你继续分发或二次修改本仓库，也建议保留这条来源说明

感谢源项目的公开分享与思路贡献。

本仓库当前包含两个可配合使用的 skills：

- `academic-paper-strategist`：负责论文规划、证据映射、keep/rewrite/delete 矩阵、检测报告热点分析、图表与截图规划、composer handoff。
- `academic-paper-composer`：负责在 working draft 上继续改稿、局部替换正文、恢复旧图表与数据库表说明、补真实运行截图、按学校模板整理定稿。

## 适用场景

- 根据真实项目仓库生成本科毕业论文规划
- 在已有初稿/定稿基础上继续改写，而不是整篇重来
- 根据查重报告、AIGC 报告继续迭代降重
- 保留原数据库 E-R 图、每张数据表的字段说明表、旧截图等 legacy assets
- 在论文里补系统真实运行截图
- 按学校模板完成最终 DOCX 收口

## 仓库结构

```text
skills/
  academic-paper-strategist/
  academic-paper-composer/
examples/
scripts/
```

每个 skill 目录内包含：

- `SKILL.md`：主工作流说明
- `agents/openai.yaml`：UI 元数据与默认提示词
- `references/`：细分执行手册、prompt 模板、检测报告重写策略等
- `scripts/`：辅助校验脚本

## 安装方式

将本仓库中的 skill 目录复制到你的 Codex skills 目录中，例如：

```bash
mkdir -p ~/.codex/skills
cp -R skills/academic-paper-strategist ~/.codex/skills/
cp -R skills/academic-paper-composer ~/.codex/skills/
```

如果你希望直接在自己的 skills 仓库中维护，也可以按需合并目录结构。

## 本地校验

维护者可以运行轻量校验脚本，检查 skill 目录、引用文件和 README 证据链接是否完整：

```bash
python3 scripts/validate_repo.py
```

## 使用示例

更完整的可复制示例见：

- [Strategist example](examples/strategist-example.md)
- [Composer example](examples/composer-example.md)

### 1. 先做论文规划

```text
请使用 $academic-paper-strategist 基于当前项目仓库、学校模板和现有论文草稿，先做本科毕业论文定稿规划。要求只保留代码、SQL、配置和文档能证实的内容，输出章节大纲、证据映射、keep/rewrite/delete 矩阵、图表规划和后续给 composer 的 handoff。
```

### 2. 继续在手改稿上改写

```text
请使用 $academic-paper-composer 继续在我当前的 working draft 上改稿。working draft 路径是：[working_draft_path]。请先备份，再按学校模板和项目证据继续修改，不要误改到原始初稿。
```

### 3. 保留数据库图表并继续降重

```text
请使用 $academic-paper-composer 保留并恢复原来的数据库 E-R 图和每张数据表的字段说明表，再根据最新查重报告和 AIGC 报告继续改稿。缺失内容优先从原稿恢复，不要凭空重写旧图表，并在改稿说明里写清楚本轮处理了哪些热点。
```

## 设计原则

- 只围绕真实项目证据写论文，避免脱离代码的虚构表述
- 先规划再改稿，降低整篇返工概率
- 支持 hand-edited draft salvage mode，避免误覆盖用户手工修改
- 优先恢复已有有效图表，再考虑重绘
- 优先重写高收益热点页，而不是整篇盲改
- 在最终定稿阶段显式检查字体、颜色、标题样式、表格字号和目录锚点问题

## 采用证据

本仓库对应的公开分享视频和用户反馈显示，这套工作流已经被真实用户用于本科论文规划和改稿场景。

- 视频播放量约 5.3 万，评论 173 条。
- 数据中心显示播放量在近五稿对比中排名第 1，游客占比约 99.4%。
- 用户反馈集中在 skill 安装、Codex 使用方式、论文规划和 composer/strategist 两个 skill 的下载与复用。

证据截图：

- [视频数据总览](docs/evidence/video-analytics-overview.png)
- [播放来源与稿件对比](docs/evidence/video-traffic-sources.png)
- [视频简介与项目说明](docs/evidence/video-post-summary.png)
- [用户反馈 1](docs/evidence/user-feedback-01.png)
- [用户反馈 2](docs/evidence/user-feedback-02.png)

## Maintenance roadmap（维护路线图）

- Keep validation checks for skill metadata, required references, and script paths.
- Expand runnable examples for both `academic-paper-strategist` and `academic-paper-composer`.
- Use [Release Checklist](RELEASE_CHECKLIST.md) so tagged versions include concise changelogs and installation notes.
- Improve documentation for common user questions, including Codex CLI setup, skill installation, and safe handling of private thesis materials.
- Keep the two-skill boundary clear: strategist for planning and evidence mapping, composer for working-draft revision and final formatting support.

## 作者

- 记得晚安 JDWA
- 邮箱：1412800823@qq.com

## 许可证

本仓库使用 MIT License。
