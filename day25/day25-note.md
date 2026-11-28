# D025 Git 基础笔记

## 一、三区
工作区 --add--> 暂存区 --commit--> 仓库 --push--> 远端

## 二、status 两列
| 码（左 = 暂存区，右 = 工作区） | 意思 |
| --- | --- |
| ?? | 未跟踪 |
| A  | 新增，已暂存 |
| M  | 已 add 待 commit |
|  M | 改了还没 add |
| D  | 已删除待 commit |
|  D | 删了还没 add |
| UU | 冲突未解决 |

## 三、diff
| 命令 | 比较 |
| --- | --- |
| git diff | 工作区 vs 暂存区 |
| git diff --cached | 暂存区 vs 最新提交（commit 前必看）|
| git diff HEAD | 工作区 vs 最新提交 |
| git diff A B | 比较任意两个提交/分支 |

## 四、我今天制造的冲突
```git switch -c feat-2
echo "feat-2 的版本" > one.txt 
git add -A && git commit -m "feat-2 改 one"

git switch main
echo "main 的版本" > one.txt 
git add -A && git commit -m "main 改 one"

git merge feat-2
git merge --abort
cat one.txt 
```
```切换到一个新分支 'feat-2'
[feat-2 71f7b83] feat-2 改 one
 2 files changed, 2 insertions(+), 2 deletions(-)
 create mode 100644 log.txt
切换到分支 'main'
[main 54aa821] main 改 one
 1 file changed, 1 insertion(+), 2 deletions(-)
自动合并 one.txt
冲突（内容）：合并冲突于 one.txt
自动合并失败，修正冲突然后提交修正的结果。
main 的版本
```

## 五、reset 三档
| 命令 | 意思 |
| --- | --- |
| --soft | 退指针，改动留暂存区 |
| --mixed | 退指针 + 重置暂存区 |
| --hard | 连工作区一起丢（先 stash！） |

## 六、踩到的坑
1. .gitignore 对已跟踪文件无效 → git rm --cached
2. 分支合并冲突 → git merge --abort 放弃合并，返回合并前  
   git diff --name-only --diff-filter=U 哪些文件冲突

## 七、还没弄明白的
1. 撤销某个 git push 怎么使用 git revert
2. remote/push/pull/tag/rebase 的原理