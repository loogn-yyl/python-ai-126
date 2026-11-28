# D025 Git 基础笔记

## 一、三区
工作区 --add--> 暂存区 --commit--> 仓库 --push--> 远端

## 二、status 两列
码是两字符，左边是暂存区，右边是工作区。`·` 表示这一位是空的。

| 码 | 意思 |
| --- | --- |
| `??` | 未跟踪 |
| `A·` | 新增，已暂存 |
| `M·` | 已 add 待 commit |
| `·M` | 改了还没 add |
| `D·` | 已删除待 commit |
| `·D` | 删了还没 add |
| `UU` | 冲突未解决 |

## 三、diff
| 命令 | 比较 |
| --- | --- |
| git diff | 工作区 vs 暂存区 |
| git diff --cached | 暂存区 vs 最新提交（commit 前必看）|
| git diff HEAD | 工作区 vs 最新提交 |
| git diff A B | 比较任意两个提交/分支 |

## 四、我今天制造的冲突

### 4.1 真解的那次（README.md，feature2 vs main）

```bash
git merge feature2
git status --short
cat README.md
```

```
UU README.md
```

冲突标记长这样：

```text
项目说明
<<<<<<< HEAD
版本：v2
新增：日志功能
=======
版本：v1
新增：缓存功能
>>>>>>> feature2
```

`<<<<<<< HEAD` 到 `=======` 是我这边，`=======` 到 `>>>>>>> feature2` 是合进来的那边。
两句都要，所以手写成合并版：

```bash
printf '项目说明\n版本：v2\n新增：日志功能\n新增：缓存功能\n' > README.md
git add README.md
git commit -m "合并 feature2：保留日志与缓存两项"
git log --oneline --graph
```

```
[main 0f5bdf5] 合并 feature2：保留日志与缓存两项
```

判断依据只有一条：留下的是「这段代码应该是什么样」，不是「哪个分支赢」。

### 4.2 对照：不想解也可以放弃

```bash
git merge feat-2
git merge --abort
cat one.txt        # main 的版本
```

`--abort` 只是把现场还原，标记会被丢掉。所以主记录是 4.1。

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

## 八、做对了但当时没写下的两件

### 8.1 用 check-ignore 验证规则对谁生效

```bash
echo "x" > log.txt
printf '*.log\n' > .gitignore
git check-ignore -v log.txt     # 无输出，没被忽略（*.log 匹配不到 .txt）
echo "z" > new.log
git check-ignore -v new.log     # .gitignore:1:*.log   new.log
```

`-v` 会说是第几行的哪条规则命中，比反复 commit 试错快。

### 8.2 add -p 逐块暂存

```bash
echo "第二行" >> one.txt
git add -p one.txt
```

```
@@ -1 +1,2 @@
 a
+第二行
(1/1) 暂存该块 [y,n,q,a,d,e,p,P,?]? y
```

`y` 暂存、`n` 跳过、`s` 拆更小、`q` 退出。