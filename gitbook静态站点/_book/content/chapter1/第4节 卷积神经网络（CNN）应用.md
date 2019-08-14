# 第4节 卷积神经网络（CNN）应用

## 4.1 Tensorflow训练自定义图片分类器

    简单的项目描述

### 硬件准备

### 程序及操作

## 4.2 图像风格迁移

<center>

![Neural Style 图像风格迁移](http://psqevyxc3.bkt.clouddn.com/neuralstyle.jpg)
</center>

在神经网络之前，图像风格迁移的程序有一个共同的思路：分析某一种风格的图像，给那一种风格建立一个数学或者统计模型，再改变要做迁移的图像让它能更好的符合建立的模型。这样做出来效果还是不错的，但一个很大的缺点：**一个程序基本只能做某一种风格或者某一个场景**。因此基于传统风格迁移研究的实际应用非常有限。
而 Neural Style 程序通过输入一张代表内容的图片和一张代表风格的图片，使用深度学习网络输出一张融合了这个风格和内容的新作品。

### 环境准备

#### VGG 网络

[训练好的 VGG 19 网络](http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat)，下载到项目文件夹“Neural Style 图像风格迁移”的中，或在运行时使用参数 `--network` 指定其位置。

#### 软件准备

除了在本课程最开始已经在 Anaconda 的 learn-ai 环境中安装好的 `TensorFlow` 外，还需安装 `Pillow` 软件包。

1.macOS 用户打开终端，Windows用户打开 Anaconda Prompt；
2.输入下面的命令来进入 learn-ai 环境；

```bash
conda activate learn-ai
```

3.安装 `Pillow` 软件包；

```bash
conda install pillow
```

4.切换工作路径到项目文件夹；

```bash
cd 项目文件夹的路径
```

### 程序及操作

```bash
python neural_style.py --content <输入图片> --styles <风格图片> --output <输出文件名> -- --iterations <迭代次数>
```

我们使用 examples 文件夹中的 1-content.jpg 和 2-style1.jpg 来举例，把上面命令中：
<输入图片> 替换为 `examples/1-content.jpg`
<风格图片> 替换为 `examples/2-style1.jpg`
<输出文件名> 替换为 `examples/output.jpg`，当然也可以不叫output，使用你自己喜欢的名字；
<迭代次数> 替换为 `100`
替换后的命令为：

```bash
python neural_style.py --content examples/1-content.jpg --styles examples/2-style1.jpg --output examples/output.jpg -- --iterations 100
```

> [!NOTE]
> <输入图片>不建议使用过大的图片，这会明显的增加机器的负担，特别是对于性能差或者没有独立显卡的机器，可能需要数个小时来生成新的图片。
> <迭代次数>在课程中使用的是 100 次迭代，可以初步看出机器风格迁移的效果。一般来说 1000 次迭代可以获得不错的图像质量，但会花费更多的时间。

<center>

![完成]( http://psqevyxc3.bkt.clouddn.com/finishProcess.jpg)
</center>

当窗口中的迭代次数变为 “100/100” 时就完成了整个图片的处理过程，打开 examples 文件夹中的图片就可以开到结果。
