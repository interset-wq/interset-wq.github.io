[:simple-git: Git官方文档](https://git-scm.com/doc){ .md-button .md-button--primary }
[:simple-github: GitHub文档](https://docs.github.com/zh){ .md-button }

[GitCode文档](https://docs.gitcode.com/){ .md-button .md-button--primary }
[:simple-gitee: Gitee文档](https://gitee.com/all-about-git){ .md-button }

???+ warning
    创建 repo 时,一定要创建 `README.md` `.gitignore` 和 `LICENSE` 文件,减少不必要的麻烦

`git init` 初始化一个全新的 Git 存储库并开始跟踪现有目录。 它在现有目录中添加一个隐藏的子文件夹，该子文件夹包含版本控制所需的内部数据结构。

`git clone HTTPS/SSH` 通过HTTPS或SSH创建远程已存在的项目的本地副本。 克隆包括项目的所有文件、历史记录和分支。

`git add .或文件名` 暂存更改。 Git 跟踪对开发人员代码库的更改，但有必要暂存更改并拍摄更改的快照，以将其包含在项目的历史记录中。 此命令执行暂存，即该两步过程的第一部分。 暂存的任何更改都将成为下一个快照的一部分，并成为项目历史记录的一部分。 通过单独暂存和提交，开发人员可以完全控制其项目的历史记录，而无需更改其编码和工作方式。

`git commit -m "备注信息"` 将快照保存到项目历史记录中并完成更改跟踪过程。 简言之，提交就像拍照一样。 任何使用 git add 暂存的内容都将成为使用 git commit 的快照的一部分。

`git status` 将更改的状态显示为未跟踪、已修改或已暂存。

`git branch` 显示正在本地处理的分支。

`git merge` 将开发线合并在一起。 此命令通常用于合并在两个不同分支上所做的更改。 例如，当开发人员想要将功能分支中的更改合并到主分支以进行部署时，他们会合并。

`git pull` 使用远程对应项的更新来更新本地开发线。 如果队友已向远程上的分支进行了提交，并且他们希望将这些更改反映到其本地环境中，则开发人员将使用此命令。

`git push` 使用本地对分支所做的任何提交来更新远程存储库。

???+ tip "创建本地repo,并发布到GitHub"

    ```bash
    # 初始化本地repo
    git init my-repo

    # 切换到本地repo目录
    cd my-repo

    # 创建本项目第一个文件README.md
    touch README.md

    # 暂存更改
    git add README.md

    # 提交修改 
    git commit -m "add README to initial commit"

    # 通过SSH连接远程repo
    git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git

    # 推送到 github
    git push --set-upstream origin main
    ```

???+ tip "对远程repo修改"

    ```bash
    # 切换到已和远程repo关联的本地repo目录
    cd repo

    # 拉取远程repo,更新本地repo
    git pull

    # 切换到现有分支 `feature-a`
    git checkout feature-a

    # 做出修改

    # 暂存被修改的文件
    git add file1.md

    # 提交修改
    git commit -m "edit file1"

    # 推送到 github
    git push
    ```

