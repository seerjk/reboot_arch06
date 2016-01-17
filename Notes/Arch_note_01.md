# Arch_note_01

## 1. 课程介绍
http://www.51reboot.com/course/arch/

一、架构师工作介绍&基础知识
系统架构师日常工作:
BAT架构师日常
架构师课程与师资介绍
Python在Linux系统中的应用和地位
数据结构基础
数组、链表、Hash、二叉树
从Python源代码分析:
Python基础语法实现的机理
Python dict和list、set的性能特质
迭代器原理
Python内置数据结构的实现和特性，如何写出更加高效的程序
课堂练习：
Linux文件系统原理，inode、空洞文件。
Python文件操作，顺序读写，随机读写。

二、计算机体系&数据库
CPU L1、L2 cache介绍以及对性能的影响
Linux Buffer、Cache对性能的影响
HTTP、TCP、IP协议详解
HTTP协议基础，各种常见header的含义
HTTP性能优化：KeepAlive、连接复用
HTTP、TCP、UDP等常见协议的关系
MVC介绍，MVC的演进历史，MVC的思想
课堂练习：
函数的应用，函数的意义，代码复用的意义
Python模块化；Python的面向对象
数据库常见设计规则；数据库原理简介，数据库架构剖析
名企架构剖析
1000G级别CDN系统设计要点

三、初级网络编程&爬虫
Python网络编程：
从urllib、urllib2库到requests
Cookie和Session的原理
同步网络编程&异步网络编程
Python实现网络爬虫
PCRE基础
实战抓取网站资源
怎么抓取异步加载的网页
介绍分布式网络爬虫
Python的reflection
在指导下自主开发监控项
磁盘、网络、CPU、内存
课堂练习：
实战网络爬虫，批量下载用户头像
名企架构剖析
豆瓣架构演进----BeansDB、DoubanFS

四、Python高级编程&MapReduce
Python高阶语法
装饰器原理介绍
通用超时设定装饰器
用Python实现"bash -x"
不定长参数，默认参数
神奇的yield，iter，实现一个自己的xrange
大数据的基石：MapReduce思想介绍
Python实现MapReduce

课堂练习：
    实战多线程网络爬虫
名企架构剖析
    Google 分布式计算集群

五、Linux多进程&多线程
多进程，多线程编程，实现多进程调度框架：
    多进程多线程的产生，在Linux系统中的地位
    多进程和多线程的选用场景
    多进程、多线程基础；为什么不能一味的开线程解决问题
    协程简介
    程序运行时的内存布局
    从系统底层看Python的多进程、多线程实现，分析GIL
    守护进程，用Python实现一个守护进程
课堂练习：
    Python多线程实战，多进程实战
    多线程协同工作实现数据采集&上报
    数据队列和锁的使用
名企架构剖析
    Google分布式文件系统

六、异步网络编程
Python网络编程常用框架：
    Twisted框架
    用Twisted网络框架实现一个RPC调用的Client和Server
    长连接和短连接，推送机制的实现
    通信协议的实现，通信协议的关键点
    深入理解HTTP协议
    为什么HTTP协议是现在这个样子

异步网络编程思想
    为什么Nginx能秒杀Apache

课堂练习：
    不用任何第三方库实现一个简化的HTTP服务器

名企架构剖析
    Facebook 架构探秘----日志、HipHop、BigPipe and more

七、高级网络编程（一） **难度陡增**

屠龙之技：异步非阻塞网络编程实战
    分析memcached并发模型
    比较各类网络编程技法的优劣
    有限状态机实战

Win、Linux、UNIX网络编程现状
    select、poll、epoll、kqueue、IOCP、libevent
    水平触发LT & 边沿触发ET
    用Python实现一个基于memcached思想的网络编程库nbNet

课堂练习：
    nbNet网络库微调
    用nbNet实现Telnet协议

名企架构剖析
    Twitter 架构探秘----Scaling、Cache、Tracing
    对于缓存的利用

八、高级网络编程（二）

屠龙之技：异步非阻塞网络编程深入
    深入剖析异步非阻塞网络编程
    长连接&连接池的应用，智能路由算法的原理与工程实现
    用nbNet实现监控数据持久化模块
    用nbNet实现监控数据中转模块Transfer
    用nbNet实现监控数据报警模块DB-Saver

课堂练习：
    动手实现“连续n次触发阈值报警”,“60s内只报警n次”
    监控系统前后端联调

名企架构剖析
    百亿量级数据库架构----Pinterest
    mysql

九、监控框架

Agent多进程调度框架实战和监控数据缓存、持久化前端数据API封装与实现：
    从头实现一个系统命令RPC调用Server和Client
    综合运用之前的知识实现一个采集服务器状态信息的框架
    运用网络编程技巧，监控框架Debug动手实战
    网络程序性能测试
    代码复用的考虑，如何以不变应万变
名企架构剖析
    360集群控制系统----如何在5s之内控制5w台服务器执行命令

十、集群控制系统

介绍开源集群管理系统：
    深入分析各自利弊和架构
    介绍我们将要开发的系统架构

分布式系统理论介绍
    CAP定理及其推导
    BASE 和 ACID
    一致性算法简介：Paxos、Raft

集群管理系统实战，实现批量命令执行的Client和Server端：
    控制系统简介
    实现能批量分发控制指令的控制系统

名企架构剖析
    Google Chubby分布式锁服务
    Apache ZooKeeper分布式配置管理

十一、综合大实战

综合实战作业（一）
    完成 集监控、控制一体的服务器管理系统
    监控系统整理
    监控系统前后端大联调，监控数据图形化展示
    高可用监控系统的构建：架构&细节
    控制系统代码整理
    监控系统支持自定义监控
    监控脚本的标准&规范
    监控脚本的下发&执行

名企架构剖析
    Google Borg任务调度系统

十二、综合大实战&面试强化培训

综合实战作业（二）
    构建一个规范的上线系统
    面试常见问题解答及剖析
    简历点评、简历润色修改
    BAT专家现场模拟面试

## 2. 系统架构师日常工作

技术才是你的立身之本。


## 3. Python基础语法知识回顾

python的小诗
```
In [1]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit. 简洁 
Simple is better than complex. 模块化 - 简单总比复杂好
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

In [8]: r = urllib2.urlopen('http://www.baidu.com').read()

In [9]: print len(r)
98537

* 大家都在用Python做些什么呢？
    - 服务器日常运维，能完整的替代Bash、Perl。如今几乎所有Linux发行版都携带了Python解释器。
    网页开发：豆瓣、知乎都是纯Python开发的网站。Django、Flask、Web.py
    大数据，数据挖掘，机器学习、自然语言处理
    大型系统开发：OpenStack
    大型游戏开发：
    《文明4》

c++ (对性能要求) 和 python (业务逻辑 Lua)


### python数据类型
* 简单类型
    - 在有限的寄存器单元或者内存存储下
    - int
    - float
    - long 大数 以L结尾
    - str 没有char
```  
In [27]: type(a)
Out[27]: str

In [28]: ord(a[0])
Out[28]: 99

In [29]: char(99)

In [30]: chr(99)
Out[30]: 'c'
```
    - None
```
In [31]: a=None

In [32]: type(a)
Out[32]: NoneType

In [33]: b=""

In [34]: type(b)
Out[34]: str

In [35]: a=[None]

In [36]: a
Out[36]: [None]

In [37]: type(a)
Out[37]: list

In [38]: type(a[0])
Out[38]: NoneType
```
    - bool: True or False
    - 没有枚举类型，用str常量代替
坑
```
In [40]: True+True
Out[40]: 2

In [41]: True*True
Out[41]: 1
```

Erlang 语言： 爱立信的交换机
    函数式语言
    并发
    内存管理
    RabbitMQ 项目

了解一门编译型语言
    c 懂硬件，cache，计算机体系 
        谭浩强 绿皮书
        标准库太少
        还要做内存管理
    cpp

* 复杂类型
    - list 连续内容
    - dict 映射关系
    - 复合类型 class
```
class F:
    pass

int number
char* name

struct Student {
    int number
    char* name
}

Student st[10]

st[0]
```


### list
append(x) 追加到链尾
extend(L) 追加一个列表,等价于+=
insert(i,x) 在位置 i 插入 x
remove(x) 删除第一个值为 x 的元素,如果不存在会抛出异常
reverse() 反转序列
pop([i]) 返回并删除位置为 i 的元素,i 默认为最后一个元素(i 两边的[]表示 i * 为可选 的,
实际不用输入)
index(x) 返回第一个值为 x 的元素,不存在则抛出异常 count(x) 返回 x * 出现的次数
sort() 排序

```
自变量形式
In [45]: l=[]

In [46]: l
Out[46]: []

In [47]: s="hello"

构造函数 list() 可以类型转换
In [48]: l=list()

In [49]: l
Out[49]: []

In [50]: l=list([1,2,3])

In [51]: l
Out[51]: [1, 2, 3]

In [55]: l
Out[55]: [1, 2, 3]

In [56]: l.append(4)

In [57]: l
Out[57]: [1, 2, 3, 4]

In [58]: l.append(4)

In [59]: l
Out[59]: [1, 2, 3, 4, 4]


extend()  +=
In [60]: l1=[5,6,7]

In [61]: l.extend(l1)

In [62]: l
Out[62]: [1, 2, 3, 4, 4, 5, 6, 7]

In [63]: l += l1


In [64]: l
Out[64]: [1, 2, 3, 4, 4, 5, 6, 7, 5, 6, 7]

In [65]: l.insert(2,99)

In [66]: l
Out[66]: [1, 2, 99, 3, 4, 4, 5, 6, 7, 5, 6, 7]


```

list的底层实现  vector


list 函数时间复杂度
append()  空间足够 1  空间不足 O(n)
extend()  空间足够 n2(新list长度n2)  空间不足 O(n)+n2
insert(i,x) 空间足够 n  空间不足 O(n)
remove(x) n
reverse() n
pop([i]) n
index(x) n
sort()  nlog(n)

----
append() 空间足够 1  空间不足 O(n)
extend() 空间足够 n2(新list长度n2) 空间不足 O(n)+n2 ~ O(n)
insert(i,x) 
    平均操作 O(n)
remove(x) O(n)
reverse() 最好情况对调 O(n)  n/2
pop(i) 不加参数 O(1)  加i O(n)
index(x) O(n) 最坏遍历整个列表
sort()  nlog2(n) 内部用快速排序

----
以sort()后的查找
pop() 尽量处理末端的



## 常用函数
eval
    线上不要用
exec 
    执行python脚本，执行一个文件的中所有字符串

作业思考问什么？
In [157]: m={}

In [158]: m=dict()

In [159]: m["a"]=2

In [160]: m["b"]=3

In [161]: m["c"]=4

In [162]: for k in m:
   .....:     print k
   .....:     
a
c
b

In [163]: l=[1,2,3]
n [164]: for k in l:
   .....:     print k
   .....:     
1
2
3
输出结果不一样


## filter
In [165]: l = [x for x in range(9) if x % 3 == 0]

In [166]: a=range(1,5)

In [167]: a
Out[167]: [1, 2, 3, 4]

In [168]: filter(lambda x:x%2, a)
Out[168]: [1, 3]

In [169]: def f(x):
   .....:     return x % 2 != 0
   .....: 

In [170]: filter(f, range(9))
Out[170]: [1, 3, 5, 7]


## map

In [171]: map(f, range(9))
Out[171]: [False, True, False, True, False, True, False, True, False]


## reduce
In [172]: def f(x,y):
   .....:     return x + y

In [173]: reduce(f, range(10))
Out[173]: 45

In [174]: sum(range(10))
Out[174]: 45

In [175]: reduce(f, range(10), 0)
Out[175]: 45

In [176]: reduce(f, range(10), 100)
Out[176]: 145

## reversed()
In [177]: list(reversed(range(9)))
Out[177]: [8, 7, 6, 5, 4, 3, 2, 1, 0]

In [178]: reversed(range(9))
Out[178]: <listreverseiterator at 0x1967290>


https://www.thomas-krenn.com/de/wikiDE/images/b/ba/Linux-storage-stack-diagram_v4.0.png


## python的文件操作

In [1]: f=open('flush1.txt', 'w')  

In [2]: f.write('aa')

In [3]: cat flus
flush       flush1.txt  

In [3]: cat flush1.txt

In [4]: f.flush()

In [5]: cat flush1.txt



In [200]: f=open("flush",'w')

In [201]: bigstr='a' * 1024*1024

In [202]: len
len

In [202]: len(bigstr)
Out[202]: 1048576 

In [203]: f.write(bigstr)

In [204]: 
KeyboardInterrupt

In [204]: f.truncate()


f.flush()
f.truncate()
f.seek()


In [13]: for i in range(9):
   ....:     print i


文件作为迭代器

In [15]: for line in open('a.txt'):
   ....:     print line

In [16]: l=list(open('a.txt'))

In [17]: l
Out[17]: ['hello']

list可以接收一个可迭代对象


b二进制模式
    windows  \r\n

        文本 f.write('hello\n')  -- \r\n
        二进制   写入啥就是啥
    linux 无差别


stdout 重定向

import sys
stdout=sys.stdout

sys.stdout = stdout

饼干老师能讲讲内存缓冲区，文件，磁盘缓冲区，磁盘的关系吗？
内存缓冲区
    - 内核
    - 用户态

## 作业

1. list实现栈和队列
List实现stack和queue的模拟操作
import Queue

2. 筛选素数

3. 作业 运用Python实现一个词频统计脚本

作业要求：
    调用用方方式:wc.py 文文件名 - 例如:wc.py novel.txt
    输出novel.txt中的英文单词的数目
    只用考虑英文情况

需要注意:
    novel.txt会很大大,如50GB,需要注意不能一一次性的读取所有内容。
    请直接修改novel.txt的原文文件不用用生生成文文件副本

    readline() 不好
        - 文件没有换行

    [a-zA-Z]