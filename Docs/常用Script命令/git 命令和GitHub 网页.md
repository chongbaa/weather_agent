# 一. git完整流程（命令行方式）

## 0. 前置检查（很重要！）

先在终端（Terminal）检查是否已经安装好 Git：

```bash
git --version
```

看到版本号（如 git version 2.39.x 或更高） → 已经安装好，可以跳到第1步 没看到版本号 → 按以下任一方式安装（推荐 Homebrew 方式）

**Homebrew 安装 Git**（强烈推荐，版本最新、好升级）

```bash
# 如果你还没安装 Homebrew，先安装它（一行命令搞定）
/bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh>)"

/bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh>)"

# 然后安装最新 Git
brew install git

# 再次检查版本
git --version
```

## 1. 全局配置你的用户名和邮箱（只需做一次）

```bash
git config --global user.name "你的名字（中文英文都行）"
git config --global user.email "你的邮箱@qq.com或github注册邮箱"

# 推荐同时设置默认编辑器（可选）
git config --global core.editor "nano"   # 或 vim、code（VSCode）
```

## 2. 两种连接 GitHub 的方式（2025年主流做法）→ 强烈推荐 SSH

|方式|安全性|每次push是否要输入密码|推荐指数|备注|
|---|---|---|---|---|
|HTTPS|一般|是（或用token）|★★☆|简单但麻烦|
|**SSH**|高|不用|★★★★★|目前最推荐（尤其是长期使用）|

**最推荐：配置 SSH（5-8分钟搞定，以后永久舒服）**

```bash
# 1. 生成新的 ssh key（建议用 ed25519 算法，更安全更快）
ssh-keygen -t ed25519 -C "你的邮箱@qq.com"

# 一直按回车（使用默认位置和空密码即可）

# 2. 把公钥加到 ssh-agent（很重要！）
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 3. 复制公钥内容到剪贴板（macOS）
pbcopy < ~/.ssh/id_ed25519.pub

# 4. 打开浏览器 → GitHub → 右上角头像 → Settings → SSH and GPG keys → New SSH key
# 标题随便写 → 把刚刚复制的内容粘贴进去 → Add SSH key

# 5. 测试连接（最关键一步！）
ssh -T git@github.com
```

看到 **Hi xxx! You've successfully authenticated...** 就成功了！

## 3. 把现有项目变成 Git 仓库并上传到 GitHub（最常用流程）

假设你的项目文件夹叫 my-awesome-project

```bash
# 进入项目文件夹
cd ~/Desktop/my-awesome-project
# 或者用拖拽方式：cd + 空格，然后把文件夹拖到终端回车

# 1. 初始化 git（如果之前没用过git）
git init

# 2. 添加 .gitignore（非常重要！！）
# 推荐根据项目类型生成（复制下面命令，根据自己项目选一个）

# Python 项目
curl -o .gitignore <https://www.toptal.com/developers/gitignore/api/python,macos,venv,pycharm> > .gitignore

# Node.js / 前端项目
curl -o .gitignore <https://www.toptal.com/developers/gitignore/api/node,macos,vscode> > .gitignore

# Java / Spring 项目
curl -o .gitignore <https://www.toptal.com/developers/gitignore/api/java,maven,gradle,macos,intellij> > .gitignore

# 或者最简单粗暴（什么都不要提交）
echo ".DS_Store" > .gitignore
echo "node_modules/" >> .gitignore
echo ".idea/" >> .gitignore
echo "build/" >> .gitignore
echo "dist/" >> .gitignore

# 3. 添加所有文件
git add .

# 4. 第一次提交（写个有意义的信息）
git commit -m "初次提交：完成项目基本功能"

# 5. 在 GitHub 网站新建一个空仓库（不要勾选任何初始化选项！）

# 6. 把本地仓库关联到 GitHub（复制你新建仓库的 SSH 地址）
git remote add origin git@github.com:你的用户名/你的仓库名.git

# 7. 推送（main 是目前最主流的主分支名）
git branch -M main          # 如果你本地还是 master 分支，改成 main
git push -u origin main
```

成功后打开浏览器，你的项目就已经在 GitHub 上了！后续操作速查表

```bash
# 日常工作流
git status                      # 查看状态（最常用）
git add .                       # 添加所有改动
git add 文件名                  # 只添加某个文件
git commit -m "修复了登录bug"    # 提交
git push                        # 推送到远程（之后都不用写 origin main 了）

# 回退 / 撤销
git reset --hard HEAD^          # 回退到上一次提交（危险！）
git restore 文件名              # 撤销单个文件的修改
git log --oneline --graph       # 好看的提交记录

# 分支相关
git branch feature/login        # 创建分支
git checkout feature/login      # 切换分支
git checkout -b feature/pay     # 创建并切换（最常用写法）
git merge feature/login         # 把 login 分支合并到当前分支
```

# 二. GitHub 网页和git 命令

|功能 / 操作|GitHub 网页端可以做到？|用 git 命令行可以直接做到？|说明 / 谁更方便 / 推荐方式|
|---|---|---|---|
|创建新仓库|✓|✓|网页更直观（可直接填描述、选开源协议等），命令行要多打几行|
|上传新文件 / 修改已有文件|✓|✓|小改动网页超方便，大量文件/经常改 → 命令行完胜|
|直接在网页编辑代码|✓|✗|网页独有！适合快速修 typo、改配置、写 README|
|上传单个文件（甚至图片）|✓|✓|网页拖拽上传非常爽，命令行要 add → commit → push|
|查看提交历史、对比代码|✓|✓|网页可视化更好看，命令行更精确（git log -p 等）|
|创建/合并 Pull Request|✓|✓（但很麻烦）|几乎所有人都在网页上操作 PR，命令行只用来 git push|
|管理 Issues、项目看板、讨论|✓|✗（基本不行）|网页是唯一方便的地方，命令行基本做不到|
|设置仓库权限、分支保护规则|✓|✗|全部在网页 Settings 里设置|
|添加/管理 SSH / GPG 公钥|✓|✗|只能在网页个人设置里操作|
|管理 GitHub Pages、Actions、Packages|✓|部分可以|几乎全部功能依赖网页界面|
|添加项目协作者、设置仓库可见性|✓|✗|只能网页操作|
|查看仓库 Insights（流量、贡献者等）|✓|✗|纯网页功能|
|Fork 别人的仓库|✓|✗（没有直接命令）|网页一键 Fork，命令行只能 clone|
|Star / Watch / 给别人赞助|✓|✗|社交功能，全部网页操作|
|大量文件批量上传/删除|✗（不方便）|✓|网页一次最多拖 100 个文件，超多文件命令行效率高得多|
|复杂的分支管理、rebase、cherry-pick|✗（很弱）|✓|命令行才是王道，网页基本不支持高级操作|
|本地开发 + 频繁提交|✗|✓|核心开发流程永远是本地 + git 命令|

实际的组合打法

```markdown

1. 本地写代码 → git add/commit/push  ← 命令行完成

2. 需要做下面这些事情时 → 打开浏览器去 GitHub 网页
   - 写/改 README、文档
   - 快速修一个小 bug（直接网页编辑）
   - 创建/回复 Issues
   - 审代码、合并 Pull Request
   - 设置分支保护、权限
   - 查看仓库统计、贡献图
   - 管理 GitHub Pages、Actions 等
```

Git 命令行和 GitHub 网页是**互补**的关系，不是替代关系。你需要两者一起使用才能完整地玩转 GitHub。

# **三. GitHub 的 fork 和 clone 在命令行里有没有对应的 git 命令？**

## **1 . 简单来说：没有纯粹的 git 命令能完全等价于 GitHub 网页上的「Fork」按钮。**

|操作|是否有原生 git 命令？|实际做法（2025-2026 主流方式）|说明|
|---|---|---|---|
|**Fork**|✗ 没有|1. gh repo fork（最推荐）||

2. 网页点 Fork
3. 极少人用 API | Fork 是 **GitHub 服务器端**的操作，原生 git 做不到 | | **Clone** | ✓ 有 | git clone <url> | 这是 git 最基本、最原生的命令，把仓库完整下载到本地 | | **Fork + Clone** | — | gh repo fork xxx/yyy --clone | 一条命令完成 fork + clone，最方便的现代做法 |

## **2. 目前最推荐的命令行完整流程（2025-2026）**

```bash
# 1. 先确保安装了 GitHub CLI（gh）
#    macOS:    brew install gh
#    Windows:  winget install --id GitHub.cli
#    Linux:    看官网 <https://cli.github.com>

# 2. 登录（第一次需要）
gh auth login

# 3. 一步完成 fork + clone（最常用写法）
gh repo fork torvalds/linux --clone

# 等价于做了这两件事：
# 1. 在你的 GitHub 账号下创建了 linux 的 fork
# 2. 自动把你的 fork clone 到本地

# 4. 进入目录并把原仓库加为 upstream（建议做）
cd linux
git remote add upstream <https://github.com/torvalds/linux.git>
git remote -v   # 确认 origin 和 upstream 都对了
```

## **3. 快速对照表（最常用写法）**

```bash
# 只 fork，不 clone
gh repo fork torvalds/linux

# fork 并自动 clone 到当前目录
gh repo fork torvalds/linux --clone

# fork 后自己手动 clone（传统做法）
gh repo fork torvalds/linux
git clone <https://github.com/你的用户名/linux.git>
```

## **4. 一句话总结：**

- git clone → 有原生命令，就是 git clone
- fork → 没有原生 git 命令，只能靠 GitHub API 或工具
- 目前**最方便的做法** → 用 gh repo fork xxx/yyy --clone 一条命令搞定

# 四. git的底层逻辑

## 1. 底层逻辑

|步骤|命令示例|底层在做什么？|为什么要这么做？（核心目的）|不做会怎样？|
|---|---|---|---|---|
|1）检查 Git 是否安装|`git --version`|询问操作系统：你有 Git 这个程序吗？版本是多少？|确认基本工具存在，避免后面全部命令都报「`command not found`」|后面所有 git 命令都会失败|
|2）全局配置用户名 & 邮箱|`git config --global user.name/email`|把你的身份信息永久保存在 `~/.gitconfig` 这个文件里|每次 `commit` 都会自动记录「谁做的改动」，GitHub 显示提交者也是靠这个信息|`commit` 会显示「未知用户」，GitHub 认不出你|
|3）生成 SSH key|`ssh-keygen -t ed25519 -C "邮箱"`|在你电脑上生成一对加密钥匙（私钥+公钥），公钥可以安全给人看，私钥必须自己保密|让 GitHub 以后能「认出」这台电脑是授权的，而不需要每次都输入账号密码|每次 push 都要手动输入密码/令牌，很痛苦|
|4）把公钥加到 GitHub|复制公钥 → GitHub 设置里添加|把你的「公钥」登记到 GitHub 服务器的「已授权钥匙列表」里|建立信任关系：以后这台电脑连上来时，GitHub 会用公钥验证「你就是钥匙的主人」|SSH 认证失败，push/pull 都会被拒绝|
|5）测试 SSH 连接|`ssh -T git@github.com`|真的去敲 GitHub 的门，看看门卫（服务器）会不会放行|验证整个 SSH 信任链路是否打通（最容易出问题的环节）|没打通的话后面 push 会报 Permission denied|
|6）`git init`|在项目文件夹执行|在当前目录创建隐藏的 .git 文件夹，正式把这个目录变成「Git 仓库」|告诉 Git：「从现在开始你要开始跟踪这个文件夹里的文件变化了」|Git 根本不认识这个文件夹，什么都干不了|
|7）创建 `.gitignore`|手动创建或 `curl` 下载|告诉 Git：「这些文件/文件夹永远不要跟踪、不要上传」|防止把垃圾文件（日志、缓存、node_modules、.DS_Store、虚拟环境等）上传到远程，保持仓库干净|仓库会变得巨大、混乱，很多不该传的东西也被传上去|
|8）`git add . / git add` 文件|添加文件到「暂存区」|把你刚刚修改的文件快照先搬到「准备室」（`staging area/index`）|让你有最后一次检查/选择的机会：「我真的要提交这些改动吗？」|直接 commit 会把所有改动（包括没改好的）都打包|
|9）`git commit -m "xxx"`|创建一个提交（`commit`）|把暂存区里的文件快照永久保存成一个「版本」（带 hash 值、作者、时间、说明）|这是 Git 的核心：版本控制的本质就是「保存一个个有意义的快照」|没有 commit → 什么都没保存，后面 push 也没东西可推|
|10）在 GitHub 网站建空仓库|—|在服务器上创建一个空的「远程仓库」|给你的代码找一个「官方备份/展示/协作」的家|没有地方可以 push，代码只能留在你本地|
|11）`git remote add origin URL`|添加远程仓库地址，别名叫 origin|在本地仓库里登记：「以后提到 origin 就代表这个 URL」|避免每次 push 都要写一长串 URL，origin 是业界默认的「主远程仓库」别名|每次 push 都要写完整 URL，很麻烦|
|12）`git branch -M main`|把当前分支改名叫 main|更改本地默认分支名称（Git 从 2020 年后逐渐把默认分支从 master 改成 main）|与 GitHub 现在的默认分支名保持一致，避免后续各种「分支名不匹配」的困惑|可能导致 push 时「找不到对应分支」|
|13）`git push -u origin main`|第一次推送 + 设置上游跟踪|把本地 main 分支的所有 commit 推送到远程 origin 的 main 分支，并建立跟踪关系|1. 把代码真正备份到云端||

2. 建立「本地分支 ↔ 远程分支」的关联，以后可以直接 `git push / git pull` | 代码没备份到远程，等于没上传成功 |

更形象的类比，把整个流程想像成你要搬家：

- 不想带走的东西列清单扔掉（`.gitignore`）
- 把要带的东西打包整理好（`git add`）
- 把打包好的箱子封好并贴标签（`git commit`）
- 在新家（GitHub）先租个空房子（新建空仓库）
- 告诉搬家公司新家的地址，并起个昵称「origin」（`git remote add`）
- 叫搬家公司把所有箱子都运过去（`git push`）
- 以后每次想再送东西过去就不用重新写地址了，直接说「送到 origin 就好」（后续直接 `git push`）

## **2. Fork 和 Clone 的区别（GitHub + Git 命令行完整解析）**

一句话记忆法： Fork = 复制一份仓库到你自己账户 （服务器端，网页/CLI）

Clone = 下载一份仓库到你本地电脑 （纯本地，git命令）

### 1）**视觉对比表**（最直观）

|维度|**Fork** 🌐（服务器复制）|**Clone** 💻（本地下载）|
|---|---|---|
|**操作位置**|GitHub **服务器端**（你的账户下创建新仓库）|**本地电脑**（下载到硬盘）|
|**命令**|`gh repo fork owner/repo`（无纯git命令）|`git clone <https://github.com/owner/repo.git`>|
|**结果**|你的GitHub上多一个**独立仓库**（可改名、加文件）|本地文件夹（.git历史完整，但**不属于你**）|
|**改代码**|可以随意改，**独立存在**，可发PR给原仓库|可以改，但**只是本地副本**，推不上去原仓库|
|**体积**|只复制**仓库结构+代码**（无历史? 有完整历史）|**完整下载**：代码+全部提交历史+分支（大仓库慢）|
|**多人协作**|**你的fork**可分享给别人，他们再clone你的fork|每个人clone一份，各自本地独立|
|**常见场景**|开源贡献（Linux内核fork→改→PR）|日常开发（clone公司仓库→本地写代码→push）|
|**删除后**|GitHub上删fork，本地clone不受影响|本地删clone，GitHub仓库还在|
|**体积影响**|GitHub多存一份（免费无限fork）|本地硬盘占空间（可删.git减小90%体积）|

```markdown
仓库原版：torvalds/linux (10GB历史)
├── Fork → chong/linux (你的GitHub，独立仓库)
│   └── Clone → /Users/chong/linux (本地文件夹)
└── Clone → /Users/chong/linux-readonly (只读本地)
```

### 2）**实际操作演示**（复制粘贴就能跑）

**场景**：贡献 microsoft/vscode（VSCode源码）

```bash
# 【1. Fork 先干这个】（服务器端创建你的仓库）
gh repo fork microsoft/vscode --clone  # 一键：fork + clone到本地
cd vscode
git remote -v
# origin  <https://github.com/chong/vscode.git> (你的fork) ← 能push!
# upstream  <https://github.com/microsoft/vscode.git> (原版) ← 同步更新

# 【2. Clone 只是下载（传统方式）】
git clone <https://github.com/microsoft/vscode.git> vscode-readonly
cd vscode-readonly
git remote -v
# origin  <https://github.com/microsoft/vscode.git> (原版) ← 不能push！
```

**关键差异验证**：

```bash
# Fork后的本地仓库 ✅ 可以推自己的改动
cd vscode          # (fork+clone的目录)
echo "我的修改" >> README.md
git add . && git commit -m "feat: add my feature"
git push origin main  # ✅ 成功推到 chong/vscode

# 纯clone的仓库 ❌ 推不了（无push权限）
cd vscode-readonly
git push origin main  # ✗ ERROR: Permission denied
```

### 3）**内存误区终结者**（90%人踩过的坑）

|❌ **常见误解**|✅ **真相**|
|---|---|
|"Fork就是clone到本地"|Fork是**服务器复制**，clone才下载本地|
|"Clone后就能push原仓库"|**无权限**！clone默认只读，fork后origin才可写|
|"Fork后本地就独立了"|Fork+clone才完整，本地origin指向**你的fork**|
|"大仓库clone很慢"|是的（完整历史），用 git clone --depth=1 只下最新版|
|"Fork删了本地就没了"|**互不影响**，fork是云端，clone是本地|

### 4）**完整工作流**（贡献开源标配，2026版）

```bash
# 1. Fork（服务器创建你的仓库）
gh repo fork owner/repo --clone
cd repo

# 2. 配置upstream（同步原仓库更新）
git remote add upstream <https://github.com/owner/repo.git>

# 3. 开发→提交→推你的fork
git checkout -b my-feature
# ... 写代码 ...
git add . && git commit -m "feat: xxx"
git push origin my-feature  # 推到你的fork

# 4. 网页创建PR（从你的fork → 原仓库）
# GitHub自动提示：<https://github.com/chong/repo/compare/my-feature>

# 5. 同步原仓库最新代码（别人合入了你的PR）
git fetch upstream
git checkout main
git merge upstream/main
git push origin main  # 同步到你的fork
```

### 5）**高级用法**（CLI一键全搞定）

```bash
# 一键fork+clone+upstream（gh 2.40+，2026默认）
gh repo fork microsoft/vscode --clone --remote=origin --upstream

# 批量fork多个仓库
gh repo fork torvalds/linux
gh repo fork python/cpython
gh repo fork --clone --remote-batch  # 批量clone你的forks

# Fork后直接创建PR模板
gh repo fork owner/repo
gh pr create --fill  # 从你的fork创建PR
```

### 6）**体积/性能优化**（大仓库必备）

```bash
# 浅克隆（只下最新代码，省90%空间，10GB→100MB）
git clone --depth=1 <https://github.com/torvalds/linux.git>  # 5秒搞定

# 后续拉完整历史（需要时）
git fetch --unshallow

# 清理无用历史（本地瘦身）
git gc --aggressive --prune=now
```

**🚀 终极记忆口诀**： **F**ork → **F**rom GitHub **服务器** **F**actory（云端造仓库） **C**lone → **C**opy to **本地** **C**omputer（硬盘拷贝）

**99%场景**：**先Fork再Clone**（gh repo fork --clone），一条命令天下我有！