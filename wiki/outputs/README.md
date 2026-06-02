# 输出成品

`wiki/outputs/` 是成品层，放最终交付物，例如 PPT、报告、文章、方案、图片成品和可复查的演示文件。

这里不是临时构建目录。临时渲染、批量截图、构建缓存和中间资产默认不进 Git。

## 输出要求

每个新输出目录必须有一个 `manifest.md`，说明：

- 输出目标；
- 目标读者；
- 来源材料；
- 生成过程；
- 最终文件；
- 未验证事项；
- 应该回写到 `wiki/topics/`、`wiki/research/` 或 `schema/methods/` 的新判断。

使用 [output manifest 模板](../../schema/templates/output-manifest.md)。

## 反哺规则

输出不是生命周期终点。输出过程中产生的新判断要回写：

- 稳定知识回写到 `../topics/`；
- 问题研究回写到 `../research/`；
- 可复用流程回写到 `../../schema/methods/`；
- 新来源回写到 `../../raw/sources/`。
