---
comments: true
icon: simple/git
status: new
title: First Contributions
subtitle: Git协作
---

:material-pen-plus: `本文创建于2025-5-16`

[:simple-github: First Contributions](https://github.com/firstcontributions/first-contributions){ .md-button }

## STEP1 Fork other's repo 

Fork repo [first-contributions](https://github.com/firstcontributions/first-contributions)

## STEP2 Clone my repo forked from others

```bash
$ git clone https://github.com/interset-wq/first-contributions.git
```

???+ note
    此处使用的是HTTPS,也可以使用SSH

## STEP3 创建一个新分支

1. 切换目录到 clone 到本地的 repo 的目录中
2. 使用 `git switch` 命令新建一个代码分支

    ```bash
    $ git switch -c <新分支的名称>
    ```

    此处创建一个add-myname分支:

    ```bash
    $ git switch -c add-interset-wq
    ```

## STEP4 修改代码, Commint 修改

1. 修改 `Contributors.md` 中的内容
2. 检查状态(可选, 输出信息中,被修改的文件的文件名会被标红)

    ```bash
    $ git status
    ```

3. 添加改动

    ```bash
    $ git add Contributors.md
    ```

4. 检查状态(可选,输出信息中,刚才标红的文件名现在标绿)
5. 提交修改

    ```bash
    $ git commit -m "Add interset-wq to Contributors list"
    ```

6. Push 到 GitHub repo

    ```bash
    $ git push origin <分支的名称>
    ```

    此处推送的分支为前面新建的分支add-interset-wq
    ```bash
    $ git push origin add-interset-wq
    ```

## STEP5 Pull Request(PR)

1. 刚刚从别人那里fork的repo上方出现 `Compare & pull request` 的按钮,点击此按钮
2. 点击 `Create pull request` 按钮，正式提交 pull request
