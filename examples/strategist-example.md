# Strategist Example

Use this prompt when you want a grounded thesis plan from a real repository.

```text
请使用 $academic-paper-strategist 基于当前仓库和我提供的学校模板，先做本科毕业论文定稿规划。
要求只保留代码、SQL、配置、文档、截图这些能被项目证据证实的内容。
请输出：
1. 章节大纲
2. 每章证据映射
3. keep/rewrite/delete 矩阵
4. 图表规划
5. 需要补充的运行截图
6. 给 composer 的 handoff brief

约束：
- 不要编造功能、数据量、部署规模或测试结果。
- 如果项目里没有某个证据，就不要写进正文。
- 如果我已经手改过初稿，请把手改部分当作保护区。
```

## Expected output

- A chapter plan grounded in repo evidence.
- A figure plan limited to engineering-style diagrams and real screenshots.
- A short handoff note for `academic-paper-composer`.
