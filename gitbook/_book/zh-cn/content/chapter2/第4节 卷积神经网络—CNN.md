# 第4节 卷积神经网络—CNN

---

>卷积神经网络（Convolutional Neural Networks, CNN）是一类包含卷积计算且具有深度结构的前馈神经网络（Feedforward Neural Networks），是深度学习（deep learning）的代表算法之一。卷积神经网络具有表征学习（representation learning）能力，能够按其阶层结构对输入信息进行平移不变分类（shift-invariant classification），因此也被称为“平移不变人工神经网络（Shift-Invariant Artificial Neural Networks, SIANN）

### 在线体验

在左上角方框中写数字来进行可视化CNN体验

<center><iframe src="http://hass.live:9024/" width="800" height="600" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe></center>

<!-- ![微信截图_20200313131651](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200313131651.png)

![微信截图_20200313131713](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200313131713.png) -->

### Tensorflow训练自定义图片分类器

使用Tensorflow深度学习框架按类别训练图像。我们将使用狗狗的图片进行模型训练，测试图片分类器对狗的品种的识别。

<center><iframe src="https://teachablemachine.withgoogle.com/train" width="800" height="600" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe></center>
#### 环境准备

1.在资源管理器中打开`learn-ai\codes\chapter1\part4_CNN\DogsBreedClassification`。下载数据库和模型文件，解压到项目文件夹中。

2.Windows用户打开Anaconda Prompt，macOS用户打开终端

3.输入下面的命令来进入learn-ai环境

```bash
conda activate learn-ai
```

4.安装额外的软件包

```bash
conda install bleach
conda install html5lib
conda install pandas
conda install python-dateutil
```

5.切换工作路径到项目文件夹

```bash
//Windows
cd C:\learn-ai\codes\chapter1\part4_CNN\DogsBreedClassification
//macOS
cd ~/Desktop/learn-ai/codes/chapter1/part4_CNN/DogsBreedClassification
```

#### 程序及操作

1.整理训练数据文件夹
运行数据处理程序`data_processing.py`来通过狗品种名称重新排列文件夹

![整理好的文件](http://pic-learn-ai.oss-cn-beijing.aliyuncs.com/classification.png)

```bash
python data_processing.py <项目文件夹的路径>
```

2.使用处理好数据训练模型
运行以下命令以使用 CNN 架构训练模型。
默认情况下，脚本下方将下载 Google 的初始架构 -'inception-2015-12-05.tgz'

```bash
python retrain.py — image_dir=dataset/ — bottleneck_dir=bottleneck/ — how_many_training_steps=500 — output_graph=trained_model/retrained_graph.pb — output_labels=trained_model/retrained_labels.txt — summaries_dir=summaries
```

以下是程序的输出

![训练程序输出](http://pic-learn-ai.oss-cn-beijing.aliyuncs.com/classification_output.png)

上述训练模型的 Tensorboard 精度图

![训练精度](http://pic-learn-ai.oss-cn-beijing.aliyuncs.com/classification_acc.png)

要运行 TensorBoard，请运行此命令

```bash
User:/dogs_breed_classification$ tensorboard — logdir summaries/ — host=0.0.0.0 — port=8888

TensorBoard 1.7.0 at http://0.0.0.0:8888 (Press CTRL+C to quit)#
```

3.测试模型

运行下面的 python 脚本，根据我们预先训练的模型对测试图像进行分类。

```bash
python classify.py
```

![测试输出](http://pic-learn-ai.oss-cn-beijing.aliyuncs.com/classification_testOutput.png)

> 你可以跳过上面教程中的第2步，直接使用提供的预训练模型（trained_model /retrained_graph.pb）来测试模型。

### 图像风格迁移

![Neural Style 图像风格迁移](http://pic-learn-ai.oss-cn-beijing.aliyuncs.com/neuralstyle.jpg)

在神经网络之前，图像风格迁移的程序有一个共同的思路：分析某一种风格的图像，给那一种风格建立一个数学或者统计模型，再改变要做迁移的图像让它能更好的符合建立的模型。这样做出来效果还是不错的，但一个很大的缺点：**一个程序基本只能做某一种风格或者某一个场景**。因此基于传统风格迁移研究的实际应用非常有限。
而 Neural Style 程序通过输入一张代表内容的图片和一张代表风格的图片，使用深度学习网络输出一张融合了这个风格和内容的新作品。

#### 环境准备

1.VGG网络

[训练好的 VGG 19 网络](http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat)，下载到项目文件夹“Neural Style 图像风格迁移”的中，或在运行时使用参数 `--network` 指定其位置。

2.Pillow

```bash
conda activate learn-ai
conda install pillow
```

#### 程序及操作

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

> <输入图片>不建议使用过大的图片，这会明显的增加机器的负担，特别是对于性能差或者没有独立显卡的机器，可能需要数个小时来生成新的图片。
> <迭代次数>在课程中使用的是 100 次迭代，可以初步看出机器风格迁移的效果。一般来说 1000 次迭代可以获得不错的图像质量，但会花费更多的时间。

![完成](http://pic-learn-ai.oss-cn-beijing.aliyuncs.com/finishProcess.jpg)

当窗口中的迭代次数变为 “100/100” 时就完成了整个图片的处理过程，打开examples文件夹中的图片就可以开到结果。
