# Gitbook 简单使用方法

## 文件结构

`_book`： 为编译好的静态站点

`content`：课程文件目录

`node_moudles`：gitbook 插件等文件

`book.json`：配置文件，主要用于添加插件和插件配置信息

`SUMMARY.md`：gitbook 目录和文档架构，在 `content` 中更改文件名称或增加减少文件需要在`SUMMARY.md`中同步改动

## 安装和初始化

1. 安装 [node.js](<https://nodejs.org/en/>)

2. 安装 gitbook

   ```bash
   npm install gitbook-cli -g
   ```
   
3. 切换 terminal 路径到 `gitbook静态站点` 文件夹

4. 安装插件

   ```bash
   gitbook install
   ```

5. 本地预览

   ```bash
   gitbook serve
   ```

## 如何安装插件

1. 在 `book.json` 的 `"plugins"` 字段中添加需要安装的差价名称；
2. 打开 terminal 切换到 gitbook 项目路径；
3. 运行命令 `gitbook install`，程序会自动按照 `book.json` 中的配置安装插件。

## 其他命令

### init——初始化一本书

```bash
gitbook init
```

在使用 `gitbook init` 之后本地会生成两个文件 `README.md` 和 `SUMMARY.md` ，这两个文件都是必须的，一个为介绍，一个为目录结构。

### build——发布电子书

```bash
gitbook build
```

该命令会在当前文件夹中生成 `_book` 文件夹，这个文件夹中的内容就是静态网页版电子书。

在使用 `serve` 命令的同时一会调用 `build` 命令。