# 第5节 循环神经网络—RNN

---

>RNN（Recurrent Neural Network）是一类用于处理序列数据的神经网络。首先我们要明确什么是序列数据，摘取百度百科词条：时间序列数据是指在不同时间点上收集到的数据，这类数据反映了某一事物、现象等随时间的变化状态或程度。这是时间序列数据的定义，当然这里也可以不是时间，比如文字序列，但总归序列数据有一个特点——后面的数据跟前面的数据有关系。

### 语音助手

当你用小米手机呼叫小爱同学，让她帮你设定闹钟的时候，实际发生的事情如下

![1060404-667c04dab1571032](https://md.hass.live/1060404-667c04dab1571032.webp)

步骤：

- 将用户的语音转化为文字
- 分析文字内容，进行填槽（Slot Filling）
- 根据填槽结果，执行命令
- 反馈结果到界面

这里的Slot Filling，中文称为填槽，将句子的内容的文字填写到正确的槽中，这个过程就是循环神经网络实现的。

![1060404-cdd510d5832d89d9](https://md.hass.live/1060404-cdd510d5832d89d9.webp)

### 文字情感分析、关键词提取

![微信截图_20190821155809](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190821155809.png)

![微信截图_20190821155851](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190821155851.png)

### 利用循环神经网络生成古诗词

#### 在线版本

<center><iframe src="http://hass.live:9113" width="800" height="1000" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe></center>

1.打开项目文件夹`learn-ai/codes/chapter1/part5_RNN/PoetAI`

![filestructure](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190821153025.png)

其中，
`poetry.txt`内包含了大量的古诗词
`poet_rnn.py`用来训练模型
`poet_rnn_output`用来生成古诗词

2.打开Anaconda Prompt，执行：

```bash
conda activate learn-ai

//Windows
cd C:\learn-ai\codes\chapter1\part5_RNN\PoetAI
//macOS
cd ~/Desktop/learn-ai/codes/chapter1/part5_RNN/PoetAI

python poet_rnn.py
```

执行后将会开始进行模型训练。

3.待模型训练完毕后，会在当前目录下生成模型文件`poetry.module-49`
使用VS Code编辑器打开`poet_rnn_output.py`，在最后一行：

```bash
print(gen_poetry_with_head_and_type("深度学习", 7))
```

将会生成以`深度学习`四个字开头的七言藏头诗。尝试将文字替换为其他，7可以替换为5，即生成五言诗。保存后执行：

```bash
python poet_rnn_output.py
```

![outputpoet](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190821153928.png)
