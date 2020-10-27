# 第2节 Linux基本操作

---

>树莓派运行的`Raspberry Pi OS`操作系统是一个Linux的发行版本，我们需要了解Linux的基本概念和操作。

---

### 内容提要

- 了解Linux终端
- 体验Linux终端的基本操作
- 学会Linux终端下的文件的基本操作
- 学会Linux终端下Nano编辑器

### 背景知识

#### 终端

终端（Terminal）也称终端设备，是计算机网络中处于网络最外围的设备，主要用于用户信息的输入以及处理结果的输出。在此处为Linux操作系统用于用户输入信息和输出信息的窗口，也是人机交流的窗口。

![neofetch-raspbian-buster-raspberry-pi-4](https://md.hass.live/neofetch-raspbian-buster-raspberry-pi-4.png)

#### Shell

Shell 是一个程序，同时它又是一种程序设计语言。作为命令语言，它交互式解释和执行用户输入的命令或者自动地解释和执行预先设定好的一连串的命令；作为程序设计语言，它定义了各种变量和参数，并提供了许多在高级语言中才具有的控制结构，包括循环和分支。

在后边的学习中我们只会用到Shell命令，并且通过这些命令与Linux内核沟通，让树莓派执行我们想要的操作。

#### Linux目录结构

![linux-filesystem](https://md.hass.live/linux-filesystem.png)

在Linux系统中，目录被组织成一个单根倒置树结构，文件系统从根目录开始，用`/`来表示。路径用`/`来进行分割（windows中使用`\`来分割）。

目录名称 | 功能
:-: | :-:
/| 根目录，位于Linux文件系统目录结构的顶层，一般根目录下只存放目录，不要存放文件
/bin|提供用户使用的基本命令， 存放二进制命令，不允许关联到独立分区
/boot|用于存放引导文件,内核文件,引导加载器
/sbin|管理类的基本命令，不能关联到独立分区，OS启动时会用到的程序
/lib|存放系统在启动时依赖的基本共享库文件以及内核模块文件
/lib64|存放64位系统上的辅助共享库文件
/etc|系统配置文件存放的目录，该目录存放系统的大部分配置文件和子目录，不建议在此目录下存放可执行文件
/home|普通用户主目录，当新建账户时，都会分配在此，建议单独分区，并分配额外空间用于存储数据
/root|系统管理员root的宿主目录
/media|便携式移动设备挂载点目录
/mnt|临时文件系统挂载点
/dev|设备（device）文件目录，存放linux系统下的设备文件，访问该目录下某个文件，相当于访问某个设备，存放连接到计算机上的设备
/opt|第三方应用程序的安装位置
/srv|服务启动之后需要访问的数据目录，存放系统上运行的服务用到的数据
/tmp|存储临时文件， 任何人都可以访问,重要数据一定不要放在此目录下
/usr|应用程序存放目录，/usr/bin 存放保证系统拥有完整功能而提供的应用程序， /usr/share 存放共享数据，/usr/lib 存放不能直接运行的，却是许多程序运行所必需的一些函数库文件，/usr/local 存放软件升级包，第三方应用程序。
/var|放置系统中经常要发生变化的文件，如日志文件
/proc|用于输出内核与进程信息相关的虚拟文件系统，目录中的数据都在内存中
/sys|用于输出当前系统上硬件设备相关的虚拟文件系统
/selinux|存放selinux相关的信息安全策略等信息

#### 常用的Linux命令

> 可以使用`[命令] --help`获得详细使用说明。如`ls --help`

##### 基本文件操作

命令 | 操作 | 举例
:-: | :-: | :-:
ls|显示文件和目录列表(list)|`ls -a` 显示隐藏文件
pwd|显示当前工作目录(print working directory)
touch|创建空文件|`touch test.bin`
mkdir|创建目录|`mkdir testfolder`
cp|复制文件或目录|`cp test.bin testfolder/test.bin.copy`
mv|移动文件或目录或改名|`mv testfolder /usr/foldertest`
rm|删除文件或目录|`rm -r /usr/folder`
cat|显示文件内容|`cat test.bin`
tar|打包或解压文件或目录|`tar -cf test.tar.gz test.bin`  压缩<br>`tar -xf test.tar.gz`解压

##### 树莓派上的软件管理工具`apt`

命令 | 操作
:-: | :-:
apt update| 更新软件源
apt upgrade |更新已安装的软件版本
apt dist-upgrade|更新系统
apt install [软件名]|安装软件
apt remove [软件名]|移除软件而保留配置
apt purge [软件名]|彻底移除软件
apt autoremove|自动卸载不需要的软件包
apt-cache search [软件名]|搜索指定名称的软件包
apt-cache show [软件名]|获取包的相关信息，如说明、大小、版本
apt source [软件名]|下载软件包的源代码
apt clean|清理无用软件包
apt autoclean|清理无用软件包

##### 使用文本编辑器`nano`编辑文件

命令 | 操作
:-: | :-:
nano -c test.bin|打开文件并显示行号
sudo nano test.bin|使用管理员权限打开文件
Ctrl + O|保存
Ctrl + X|退出

##### 其他常见命令

命令 | 操作
:-: | :-:
Alt + Tab键|切换活动窗口|
Tab键|自动补齐|
man [命令]|查看命令使用手册|
ifconfig|查看当前网路连接状态以及IP地址|
ping [IP地址]/[URL]|检测与某个IP地址是否连通|
sudo raspi-config|打开树莓派配置界面|只针对树莓派系统
date|查看当前系统时间|
ps -ax|显示当前运行的进程|
kill -9 [进程号]|关闭某个进程|
top|实时显示各个进程对资源的占用情况|
passwd|设置用户密码|
groups|显示当前用户所属组|
clear|清空终端屏幕|
uname -m|显示机器的处理器架构|
which [命令]|在系统中搜索命令以确定该命令是否存在|
shutdown -r now|重启系统
shutdown -h now|关机

#### 练习：文件操作

> 尝试完成下面的题目。在下面的交互终端中进行练习。相关命令的说明见下表。

- 切换目录到`/usr`，新建一个名为`hello_linux.bin`的新文件，和一个名为`linux_Home`的文件夹
- 将`hello_linux.bin`的文件复制一份到`linux_Home`文件夹中，并把文件改名为`.hello_linux.bin.back`
- 用文字编辑器打开`.hello_linux.bin.back`，输入一段话*The Raspberry Pi is a tiny and affordable computer that you can use to learn programming through fun, practical projects.*
- 压缩`linux_Home`文件夹为`linux.tar.gz`，并将其移动到用户目录下

<center><iframe src="http://hass.live:8082" width="100%" height="600" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe></center>
