---
comments: true
icon: simple/git
status: new
title: 快速开始
# subtitle: 算法和数据结构
---

:material-pen-plus: `本文创建于2025-5-16`

[:simple-git: Git官方文档](https://git-scm.com/doc){ .md-button .md-button--primary }
[:simple-github: GitHub官方文档](https://docs.github.com/zh){ .md-button }

## STEP1 在 Git 中设置用户名和邮箱

Git 使用用户名将提交与身份关联。 {==Git 用户名与 GitHub 用户名不同==}, 可以使用任意文本作为 Git 用户名, 此用户名只用来显示 repo 的提交信息.

为每个 repo 设置全局用户名global user.name和全局邮箱global user.email

    $ git config --global user.name "user name"
    $ git config --global user.email "email@example.com"

检查用户名和邮箱是否设置成功

    $ git config --global user.name
    user name
    $ git config --global user.email
    email@example.com

???+ info "单独为某个 repo 设置用户名和邮箱"
    1. 切换目录到本地库
    2. 为这个 repo 专门设置git用户名和邮箱

        ```bash
        $ git config user.name "user name"
        $ git config user.name "email@example.com"
        ```

    3. 检查用户名是否设置成功

        ```bash
        $ git config --user.name
        user name
        $ git config --user.email
        email@example.com
        ```

## STEP2 通过 Git 向 GitHub 进行身份验证

从 Git 连接到 GitHub 仓库时，需要使用 HTTPS 或 SSH 向 GitHub 进行身份验证。

通过HTTPS连接比较简便,推荐使用

