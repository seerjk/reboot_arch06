git_pull的一个坑.md

## 1. 问题描述
在本地`reboot06_arch`文件夹下初始化，本地当前是有文件的。

```
cd reboot06_arch/
git init
git add .
```

* 本地没有git commit

添加远程仓库(远程是空仓库)
```
$ git remote add origin git@github.com:seerjk/reboot06_arch.git

$ git pull origin master

$ git lg
* 5149ea3 - (HEAD, origin/master, master) Initial commit (34 minutes ago)
```

至此本地文件夹中的所有文件丢失

## 2. 不完美的恢复方法
`git fsck --lost-found`可以找回丢失的文件，找回的文件存储在`.git/lost-found/other/`文件夹中。只是文件名全部丢失。

```
$ git fsck --lost-found
Checking object directories: 100% (256/256), done.
dangling blob 0a8549d34027d27ac0f6869ca3a7a2c06895e0ab
dangling blob 4ae651337ffb4922e29c7c93dfc2f56f12144094
dangling blob 2ca9d88c8a5e166afbfe6e60722859c4fbe13f75
dangling blob 4db3d124be16662fa2d489be3727d845f3ab04ff
dangling blob f1775338386c590714c48b9627db7de64ca2987e
dangling blob f144be14cd90eb298a09eb6bfb0b3fcf223f532d
dangling blob 14ec337dbe48b270e0c84a87c401f69f505c5542
dangling blob 15fe91ad238cb977b60c209c8e8e079e7eaedb26
dangling blob 7741be54f242a6426a797d0144df3e7d6b5d2d97
dangling blob 7cec2afbefa0aa9ba269a1f592abaa3de7dcb0f7
dangling blob 3e306fa58acf4e87e0385202160f8ac4b70ad0e4

$ ls .git/lost-found/other/
0a8549d34027d27ac0f6869ca3a7a2c06895e0ab
14ec337dbe48b270e0c84a87c401f69f505c5542
15fe91ad238cb977b60c209c8e8e079e7eaedb26
2ca9d88c8a5e166afbfe6e60722859c4fbe13f75
3e306fa58acf4e87e0385202160f8ac4b70ad0e4
4ae651337ffb4922e29c7c93dfc2f56f12144094
4db3d124be16662fa2d489be3727d845f3ab04ff
7741be54f242a6426a797d0144df3e7d6b5d2d97
7cec2afbefa0aa9ba269a1f592abaa3de7dcb0f7
f144be14cd90eb298a09eb6bfb0b3fcf223f532d
f1775338386c590714c48b9627db7de64ca2987e
```


问题解决参考
http://www.eoeandroid.com/blog-2-38362.html?_dsign=d21d9860