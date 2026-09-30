# 基于 InterNote 的博客仓库（文章以 GitHub Issue 形式撰写）
# 由 [InterNoteTemplate](https://github.com/interset-wq/InterNoteTemplate) 模板创建。

## 使用方法

1. 点击本仓库的 **Use this template** 创建你的博客仓库（建议命名 `XXX.github.io`，`XXX` 为你的 GitHub 用户名）
2. 编辑 `config.toml`：站点标题、头像、语言、giscus 评论、访问计数等
3. `Settings -> Pages -> Build and deployment -> Source` 选择 `GitHub Actions`
4. 打开 `Actions -> build Internote -> Run workflow`，完成首次全局生成
5. 新建一篇 Issue 并**添加至少一个 Label**，保存后自动构建，稍后即可通过 Pages 地址访问

## 约定

- 文章 = Issue；Label 用于分类，配置在 `config.toml` 的 `single_page` 中的 Label（如 `about`）会生成独立页面
- 生成产物（`dist/`、`sources/`、`internote.json`）由 workflow 自动提交回本仓库，请勿在 `.gitignore` 中忽略
- 首次构建后，本 README 会被自动替换为站点统计（文章数 / 评论数 / 字数 / 构建时间）
- 修改 `config.toml` 或遇到异常时，手动 `Run workflow` 全局重建一次
- 定时任务每天全局重建一次（0 16:00 UTC）

Powered by [Internote](https://github.com/interset-wq/InterNote) • Based on [Gmeek](https://github.com/Meekdai/Gmeek)
