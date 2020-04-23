# 第6节 人工智能与游戏—DQN

---

>DeepMind《Playing Atari with Deep Reinforcement Learning》提出了**强化学习算法（DQN）**，DQN使用卷积神经网络作为价值函数来拟合Q-learning中的动作价值，这是第一个直接从原始像素中成功学习到控制策略的深度强化学习算法。DQN 模型的核心就是卷积神经网络，使用Q-learning 来训练，其输入为原始像素，输出为价值函数。在不改变模型的架构和参数的情况下，DQN在七个Atari2600游戏上，击败了之前所有的算法，并在其中三个游戏上，击败了人类最佳水平。

![atari](https://md.hass.live/640.webp)

### Flappy Bird

![fbird](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190821174302.png)

1.打开项目文件夹`learn-ai/codes/chapter1/part6_DQN/DeepLearningFlappyBird`

2.打开Anaconda Prompt，进行训练：

```bash
conda activate myenv

//Windows
cd C:\\learn-ai\\codes\\chapter1\\part6_DQN\\DeepLearningFlappyBird

//macOS
cd ~/Desktop/learn-ai/codes/chapter1/part6_DQN/DeepLearningFlappyBird

python deep_q_network.py
```

3.预先训练好的模型：

```bash
python deep_q_network_trained.py
```

### 进化算法超级马里奥

>这种学习方式称之为神经网络进化拓扑结构（NeuroEvolution of Augmenting Topologies，简称NEAT）

实际进化过程中，超级马里奥并不会进行预测以改变其行动。通过进行不同的尝试，而不是做其“应该”做的事情，这样每次都会产生新的点子。当一个点子成功后，就会被记住，反之则被作废。就这样，超级马里奥在经历了34尝试后，完全通关了！当然，如果重新运行的话，这套AI机会肯定可以找到一条不同但不会更加成功的线路。

1.打开项目文件夹`learn-ai/codes/chapter1/part6_DQN/SuperMario`

2.双击打开`EmuHawk.exe`

3.**载入游戏文件** 点击左上角的`File`——`Open ROM`，然后选择项目目录下的`Super Mario World(USA).sfc`

![微信图片_20190822102248](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190822102248.png)

![微信图片_20190822102329](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190822102329.png)

4.**载入游戏存档文件** 点击左上角的`File`——`Load State`——`Load Named State`，然后选择Lua目录下的`DP1.State`

![1](https://md.hass.live/1.png)

![2](https://md.hass.live/2.png)

5.**载入算法文件** 点击左上角的`Tool`——`Tool Box`，选择Lua Console。在新窗口中点击`Script`——`Open Script`，选择项目目录下的`neatevolve.lua`

![3](https://md.hass.live/3.png)

![4](https://md.hass.live/4.png)

![5](https://md.hass.live/5.png)

![6](https://md.hass.live/6.png)

6.**观察游戏的自我进化过程** 思考游戏进化的过程和生物进化的异同

![微信截图_20190822102857](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190822102857.png)
