# Codex Academic Paper Skills

面向 Codex / Codex CLI 的本科软件工程论文技能包，聚焦“基于真实项目仓库完成论文规划、定稿改写、降查重、降 AIGC、图表恢复、运行截图补充、DOCX 收口”这类高频任务。

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

## 使用示例

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

## 作者

- 记得晚安 JDWA
- 邮箱：1412800823@qq.com

## 许可证

本仓库使用 MIT License。
