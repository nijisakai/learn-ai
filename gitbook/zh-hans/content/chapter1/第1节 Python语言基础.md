# 第1节 Python语言基础

---

## Python简介

Python是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。

Python的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

Python是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。

Python是交互式语言： 这意味着，您可以在一个Python提示符 >>> 后直接执行代码。

Python是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。

Python是初学者的语言：Python对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到浏览器再到游戏。

<center><iframe src="http://hass.live:8000/user/yuanzhuo/notebooks/L01_PMC%20-%20Intro%20to%20Python%20and%20Turtle.ipynb" width="100%" height="1000" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe></center>

### 1.Python发展历史

Python是由Guido van Rossum在八十年代末和九十年代初，在荷兰国家数学和计算机科学研究所设计出来的。

Python本身也是由诸多其他语言发展而来的,这包括ABC、Modula-3、C、C++、Algol-68、SmallTalk、Unix shell和其他的脚本语言等等。

像Perl语言一样，Python源代码同样遵循GPL(GNU General Public License)协议。

现在Python是由一个核心开发团队在维护，Guido van Rossum仍然占据着至关重要的作用，指导其进展。

Python 2.7被确定为最后一个Python 2.x版本，它除了支持 Python 2.x语法外，还支持部分Python 3.1语法。

### 2.Python特点

1).易于学习：Python有相对较少的关键字，结构简单，和一个明确定义的语法，学习起来更加简单。

2).易于阅读：Python代码定义的更清晰。

3).易于维护：Python的成功在于它的源代码是相当容易维护的。

4).一个广泛的标准库：Python的最大的优势之一是丰富的库，跨平台的，在UNIX，Windows和macOS兼容很好。

5).互动模式：互动模式的支持，您可以从终端输入执行代码并获得结果的语言，互动的测试和调试代码片断。

6).可移植：基于其开放源代码的特性，Python已经被移植（也就是使其工作）到许多平台。

7).可扩展：如果你需要一段运行很快的关键代码，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。

8).数据库：Python提供所有主要的商业数据库的接口。

9).GUI编程：Python支持GUI可以创建和移植到许多系统调用。

10).可嵌入: 你可以将Python嵌入到C/C++程序，让你的程序的用户获得"脚本化"的能力。

### 3.Python版本说明(以树莓派已安装版本为例)

|版本|说明|备注|
:-:|:-:|:-:
|Python|Python2.7|属于Python早期版本，官方逐渐放弃维护该版本|
|Python3|Pyhton3.7|Python3是较新的版本，Python2.7语法与Python3不兼容，其程序代码无法使用Python3的解释器运行|

树莓派上运行python2环境，如下图：

树莓派上运行python3环境，如下图：

### 4.Python文件的执行

我们一般在终端里，通过`python test.py`的方式来运行Python文件。

### 5.Python包管理工具—pip

pip是一个现代的，通用的Python包管理工具,提供了对Python包的查找，下载，安装，卸载的功能。  
PIP的使用方法:  
【注】：由于Python2与Python3的语法不兼容，故pip为Python2的包管理工具，Python3的包管理工具为**pip3**。
|pip命令|功能|备注
:-:|:-:|:-:
|install|安装软件包|pip install [package name]|
|download|下载软件包||
|uninstall|卸载软件包|pip uninstall [package name]|
|list|列表列出已安装的软件包|pip list|
|show|显示已安装软件包的信息|pip show [package name]|
|check|检查已安装的软件包是否具有兼容的依赖项||
|search|搜索PyPI查找软件包||
|help|显示帮助命令||

## Python基本语法

![20180823164259854](https://md.hass.live/20180823164259854.png)

> [!NOTE]
> 测试

<!--sec data-title="Introduction" data-id="intro" ces-->
This page is implemented using the two plugins developed by me: ```gitbook-plugin-mcqx``` and ```gitbook-plugin-sectionx```. You can use the two plugins separately, but they can also be integrated for more interactivity.

Please check the [Github repo](https://github.com/ymcatar/gitbook-plugin-mcqx) for the syntax, changelog of the plugin ```gitbook-plugin-mcqx```. Syntax too complicated? Use the code generator in the [plugin homepage](http://ymcatar.github.io/gitbook-plugin-mcqx/).

The source code for this page is available [here](https://raw.githubusercontent.com/ymcatar/gitbook-test/master/testing_mcqx.md) for your reference.
<!--endsec-->

<!--sec data-title="Example" data-id="q2" data-show=true ces-->

Question attempted will be disabled, however, you can open a new tab in Incognto Mode (Chrome), Private Window (Firefox), or clear your cookies if you want to try to answer this question again.

The ```random``` option is enabled for the question, you might find the order of the questions to be different when you refresh the page.

{%mcq ans="o4", random=true%}
{%title%}
Which of the following is not a planet in the Solar System?
{%o1%} Jupiter
{%o2%} Earth
{%o3%} Mars
{%o4%} Pluto
{%hint%} Poor Pluto ...
{%endmcq%}

The ```random``` option is disabled for the question.

{%mcq ans="o3"%}
{%title%} Just click option C to continue.
{%o1%} Don't click me. I'm A.
{%o2%} Don't click me. I'm B.
{%o3%} Click me.
{%o4%} Don't click me. I'm C.
{%hint%} It is so hard to come up with placeholder question ...
{%endmcq%}

You can use ```count``` to only displayed a certain number of options. You can try to see all the options by refreshing the page, or if you are smart, just take a look of the source code of this page.

{%mcq ans="o4", count=7%}
{%title%} Just find the number "42" and click it.
{%o1%} ```689```
{%o2%} 30626700^23
{%o3%} 30624770
{%o4%} 42
{%o5%} 1234
{%o6%} 99999
{%o7%} 1
{%o8%} -3
{%hint%} It is so hard to come up with placeholder question ...
{%endmcq%}

You can add a ```{%message%}``` sub-block. The message will be displayed only after the user has answered the question correctly, useful for outputing answer explanation.

{%mcq ans="o4", random=true%}
{%title%} Just find the number ```42``` and click it.
{%o1%} 31
{%o2%} 13
{%o3%} 689
{%o4%} 42
{%message%} This message is only visible to those who answered this question correctly ...
{%endmcq%}

<!--endsec-->

{%mcq ans="o1", count=2%}
{%title%} This is a question?
{%o1%} First option
{%o2%} Second option
{%o3%} Third option
{%o4%} Fourth option
{%o5%} Fourth option
{%o6%} Fourth option
{%o7%} Fourth option
{%o8%} Fourth option
{%endmcq%}

<!--sec data-title="Introduction" data-id="introabc" data-nopdf="true" ces-->
This page is implemented using the two plugins developed by me: ```gitbook-plugin-sectionx```, please check the [Github repo](https://github.com/ymcatar/gitbook-plugin-sectionx) for the plugin.

The source code for this page is available [here](https://raw.githubusercontent.com/ymcatar/gitbook-test/master/testing_sectionx.md).
<!--endsec-->

<!--sec data-title="Example 1" data-id="section1" ces-->
This is a section that is by default visible. You can toggle this with the button in the title. The next section is hidden by default, you can add a custom button to toggle it (see GitHub for the syntax).

<button class="section" target="section3" show="Show the next section" hide="Hide the next section"></button>
<!--endsec-->

<!--sec data-title="Example 2" data-id="section2" data-collapse=true ces-->
This is a section that is by default closed but visible (with ```data-collapse=true```)
<!--endsec-->

<!--sec data-title="Hidden 3" data-id="section3" data-show=false ces-->
This section can only be opened with that button.
<!--endsec-->

This is a spoiler: {%s%}Hello World.{%ends%}

{%youtube%}JIB3JbIIbPU{%endyoutube%}

```eval-python
print [x + 1 for x in range(10)]
```

```eval-python
import turtle

def hilbert2(step, rule, angle, depth, t):
   if depth > 0:
      a = lambda: hilbert2(step, "a", angle, depth - 1, t)
      b = lambda: hilbert2(step, "b", angle, depth - 1, t)
      left = lambda: t.left(angle)
      right = lambda: t.right(angle)
      forward = lambda: t.forward(step)
      if rule == "a":
        left(); b(); forward(); right(); a(); forward(); a(); right(); forward(); b(); left();
      if rule == "b":
        right(); a(); forward(); left(); b(); forward(); b(); left(); forward(); a(); right();
myTurtle = turtle.Turtle()
myTurtle.speed(0)
hilbert2(5, "a", 90, 5, myTurtle)
```

<center><iframe src="http://hass.live:9019" width="100%" height="1400" scrolling="yes" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe></center>

### 1.Python语言源程序模块的初识

一个Python程序可能由一个或多个模块组成。模块是程序的功能单元。Python模块的典型结构由:**模块文档、模块导入、变量定义、类定义语句、函数定义语句、主程序**等组成。

**模块文档**：模块文档使用三引号注释的形式，简要的介绍模块的功能以及重要全局变量的含义。

**模块导入**：导入需要调用的其他模块。模块只能被导入一次，被导入模块中的函数代码并不会被自动执行，只能被当前模块主动（显式）调用。

#### 2.基本词法单位、标识符/常量/运算符等构成规则与关键字

**基本词法单位**：常量、变量、关键字、运算符、表达式、函数、语句、类等。 常量：是指初始化（第一次赋予值）后保持固定不变的值。例如：1，3.14，'Hello!',False,这是4个不同类型的常量。在Python中没有命名常量，通常用一个不改变值的变量代替。比如：PI=3.14 通常用于定义圆周率常量PI。

**标识符**：用于不同的的词法单位，通俗的讲就是名字。标识符可以作为变量、函数、类的名字。合法的标识符必须遵守以下规则：

- 由一串字符组成，字符可以是任意字母、数字、下划线、汉字，但这些字符中的开头不能是数字。
- 不能与关键字同名。关键字也成为保留字，是被语言保护起来具有特殊含义的词，不能用于起名字。查看Python的语言的所有关键字（用Python自带的IDLE执行下面两句代码）

``` python
import keyword
keyword.kwlist
```

![1728484-db2bf141eb715a73](https://md.hass.live/1728484-db2bf141eb715a73.webp)

- 标识符中唯一能够使用的标点符号是下划线，不能含有其他标点符号（包含：空格、括号、引号、逗号、斜线、反斜线、冒号、句号、问号等）。

> **正确的标识符**：X、varl、FirstName、stu_score、平均分2等
**错误的标识符**：stu-score、First Name、2平均分
**变量**：是指在运行的过程中值可以被修改的量。变量的名称除了必须符合标识符的构成规则外，要尽量遵循一些约定俗成的规范。以下划线开头的变量在Python中有特殊的含义，所以自定义名称时，一般不用下划线作为开头字符。此外，Python是严格区分大小写字母的。也就是说，Score和score会被认为是两个不同的名字。
**运算符**：指常量/变量之间进行何种运算。
**表达式**：由常量、变量加运算符构成。一个表达式可能包含多次多种运算，与数学表达式在形式上很接近。例如：1+2、2*(x+y)、0<=a<=10等。
**函数**：是相对独立的功能单位，可执行一定的任务。
**语句**：是由函数、表达式调用组成的。另外，各种控制结构也属于语句，例如： if语句、for语句。
**类**：是同一类事物的抽象。我们处理的数据都可以看做数据对象。Python是面向对象的程序设计语言，它是一个事物的静态特征（属性）和动态行为（方法）封装在一个结构里，称之为对象。

### 3.程序的书写格式与基本规则

**缩进**：使用缩进来区分代码块的级别。Python语言中没有采用花括号或begin...end等来分隔代码块，而是使用冒号和代码缩进来区分代码之间的层次。代码缩进是一种语法规则，错误的缩进可能导致代码的含义完全不同。如下2个代码块
![1728484-77bb1c5e0daf3c45](https://md.hass.live/1728484-77bb1c5e0daf3c45.webp)
建议使用在缩进代码前输入4个空格来表示代码缩进，不推荐其他数量的空格或使用制表符的方式来完成缩进。

**分号**：Python允许在行尾加分号，但不建议加分号，也不要用分号将两条命令放在同一行中。建议每一条命令单独一行。

**长语句行**：除非遇到长的导入模块语句或者注释里的URL，建议不宜超过80个字符。对于超长语句，允许但不提倡使用反斜杠连接行，建议在需要的地方使用圆括号来连接行。例如：

- 不推荐写法

``` python
 year1 = 2016
 if year1 % 4 == 0 and year1 % 100 != 0 or \
    year1 % 400 == 0:
     print(year1,"是闰年！")
 else:
     print(year1,"不是闰年！")
```

- 推荐写法

``` python
year2 = 2018
if (year2 % 4 == 0 and year2 % 100 != 0 or
      year2 % 400 == 0):
     print(year2,"是闰年！")
else:
     print(year2,"不是闰年！")
```

**括号**：不建议使用不必要的括号，除非用于实现行连，否则不要在返回语句或者条件语句中使用括号，例如：

``` python
if (x):         # x两侧的括号多余
   foo()

if not (x):     # x两侧的括号多余
   foo()

return (x)      # x两侧的括号多余
```

**空行**：变量定义、类定义以及函数定义之间可以空两行。类内部的方法定义之间，类定义与第一个方法之间，建议一行。函数或方法中，如果有必要，可以空一行。

**空格**：对于赋值(=)、比较（==,<,>,!=,<>,<=,>=,in,not in,is,is not）、布尔（and,or,not）等运算符，在运算符两边各加一个空格，可以使代码更清晰。而对于算数运算符，可以按照自己的习惯决定，但建议运算符两侧保持一致。例如：

- 不推荐写法

``` python
x==1
```

- 推荐写法

``` python
x == 1
```

**注释**：注释通常以#开始直到行尾结束。行内注释：和语句在同一行中的注释。行内注释应该以#和单个空格开始，应该至少用两个空格和前面的语句分开。注释块后面通常跟着代码，且注释块应该与相关代码的缩进一致。注释块中的每行以#和一个空格开始，注释块内段落以仅含单个#的行分割。注释块上下方最好各空一行。例如：

- 建议的写法

``` python
# 这个函数用于计算班级所有学生的平均分
#
# 例子： Avg(score,100)

def Avg(Score,Num):
      pass
```

**文档字符串**：是Python 语言独特的注释方式。文档字符串是包、模块、类或函数中的第一条语句。文档字符串可以通过对象__doc__成员被自动提取。我们书写文档字符串的时候，在其前、后使用三重双引号 """ 或三重单引号 '''。一个规范的文档字符串应该首先是一行概述，接着是一个空行，然后是文档字符串剩下的部分，并且应该与文档字符串的第一行的第一个引号对齐。例如：

``` python
def Avg(Score, Num=100):
      """ 计算班级的平均分

      从Score中读取所有学生的成绩，逐一加求总分，然后把总分除以人数Num,结果就是平均分，返回该结果

      参数
          Score: 记录所有学生的成绩列表
          Num:班级总人数，默认值是100

      返回值
          float类型的平均分
      """
    pass
```

文档字符串可以通过__doc__成员进行查看，也可以在help()函数的结果里

``` python
>>> print(Avg.__doc__)
```

文档字符串通常用于提供在线帮助信息。
