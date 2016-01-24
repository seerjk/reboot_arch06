# Note 02
## 1.homework


### queue
队列
queue.pop(0)  移动元素

#### 切片法 
```
l = []
front = l[0]
l = l[1:]
return front
```

* 内存空间没有回收
如果用切片是不是可以考虑，无用的空间达到一定的量，重建一个list，把原来的list销毁？


#### 循环队列
头尾指针
队列空间
head
tail
size


转一圈回来的时候，head 是不是也要
h = (h+1) % len(list)

环形，转一圈，元素不会被覆盖么
size可以用来判断queue是否有空间。有空间，再push

循环队列，是不是一开始就要先确定queue的最大长度？
是，一般是定长的。


### wordcount
只包含 字母和数字

每次读出量，不要太小

折行
```
hello wor
ld
```

补基础：

* 站在开发角度分析问题
* Linux 操作系统原理
* 数据库原理


## git
git push origin master:master
master:master
本地branch : 远端branch

git push origin master
git push

origin

[jiangk@node71 homework-arch-6]$ git config -l

remote.origin.url=git@github.com:51reboot/homework-arch-6.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master


提交到多个origin

git remote add reboot git@github.com:seerjk/homework


不要放入大文件到git中
git commit -a  危险
git add -u  只添，之前存在commit的，已经修改的文件

git reset xxxx   未push到远端，可以在本地撤销

## pull： git pull origin master
1. git fetch origin master
从远端拉取
git diff origin/master

隐藏分支
git log origin/master

2. git merge origin/master


两个人操作，测试



## 4. linux 中 Buffer / Cache

Buffer 文件系统的缓存，高速设备和低速设备的缓冲
    内核更新机制，定时刷入磁盘
    Linux为解决 内存和磁盘间速度差异，
    Buffer用于缓冲
    写文件，暂存在内存，定时刷新到磁盘

Cache 缓存
    更多用在读取上

测试数据库性能，要注意之前是否有加载过数据。

可用内存 加上 buffer cache
使用掉的内存 见到 buffer  cache

## 5. 存储金字塔

list
array

代码见：
/home/binggan/reboot/2/cache
arraynode.py listnode.py run.py

## 6. 作业：mysql python
敲教材中的，每个sql的例子


行锁，列锁，表锁都是什么时候发生？
锁是怎么实现的？

## 7. db实现
leveldb   k-v
    单机上的bigtable实现
    快照实现
    实现思想

bigtable 分布式的k-v存储  
    集群实现


快照和锁的区别是什么？
    快照  git commit 提交，基于本地的快照，push的时候才解决冲突。
        db 多版本实现 快照
    锁  svn，提交的时候只能一个人提交，会锁住
如果修改同一行数据的时候，是基于快照，还是有行锁，不让其他人修改？
mvcc 是基于快照，修改的时候不是加锁，而是修改时候的快照

cow copy on write  内存上的快照实现

git的快照    commit id 来实现的多版本



## db  key-value 数据库
write.py k1 v1
write.py k2 v2
read.py k1 k2

持久化，存储在磁盘上。

设计DB面临的问题：
1. 数据怎么存储，怎么读取  --> 字典(json)
    一条记录

2. 数据怎么不丢失 --> 每次写 flush
3. 数据的快速写入 --> log，快速查找 --> 索引



json.dump  --- struct.pack
json.load  --- struct.unpack

struct
In [11]: import struct

In [12]: n=4 

In [13]: struct.pack('<I',n)
Out[13]: '\x04\x00\x00\x00'

In [14]: s=struct.pack('<I',n)

In [15]: len(s)
Out[15]: 4

In [16]: sbig=struct.pack('>I',n)

In [17]: sbig
Out[17]: '\x00\x00\x00\x04'

In [16]: sbig=struct.pack('>I',n)

In [17]: sbig
Out[17]: '\x00\x00\x00\x04'


In [18]: struct.unpack('<I',s)
Out[18]: (4,)

In [19]: a = struct.unpack('<I',s)

In [20]: a
Out[20]: (4,)

In [21]: a[0]
Out[21]: 4



序列化
```
In [22]: m={}

In [23]: m["k"]="v1"

In [24]: m["k1"]="v2"

In [25]: import json

In [27]: json.dumps(m)
Out[27]: '{"k": "v1", "k1": "v2"}'

In [28]: s=json.dumps(m)

In [29]: f=open("m.json", "w") 

In [30]: f.write(s)

In [31]: f.close()

In [32]: cat m.json
{"k": "v1", "k1": "v2"}
```

struct 把int变为二进制方式存储

4Byte  
In [33]: 2**32
Out[33]: 4294967296

全部存为ASCII：
In [34]: print '%010d' %(123)
0000000123

#### 作业：
write append修改了 存为ASCII
要改下 read的   read也要修改下

xdb.py

def append(self, k, v): 
    klen = len(k)
    vlen = len(v)
    #header = struct.pack("<II", klen, vlen)
    header = '%010d%010d'%(klen, vlen)

如何修改：
def read(self, pos):
    self.f.seek(pos)
    s = self.f.read(8)
    #klen, vlen, = struct.unpack("<II", s)

## http tcp udp
应用层 -- (会话 表示 应用) 
    HTTP 特定领域的协议
    ftp
    smtp
    dns 
        udp 
        tcp 数据返回的多，太长的时候



传输层 -- 传输控制，TCP 数据的可靠有序
    udp 之比IP 多了port和简单的校验

网络层 --  完成寻址功能，编号定位，标识设备
    数据不保证安全送达，尽量送达，不是可靠送达
    icmp (ping  echo  reply)
    traceroute  ttl 每过1跳 减1
    mtr 

链路层
    mac地址
    ip -转换- mac   ARP
    ARP欺骗

## socket 编程规范 (要掌握的)
接口层 -- API抽象


## CDN 分享

* CDN架构是什么样的
* 如何尝试去介绍一个架构

CDN -- 运维细节
直播，点播
移动端



### CDN服务构成
* 服务架构
    - 调度层
    - 服务层
    - 支撑系统

* 服务类型
    - 下载
    - 图片
    - 页面
    - 视频 点播类

* 服务规模
    - 超过1000Gbps带宽
    - 服务器近1000台
        * 每天大约1G多，服务器类型：
            - 4 千兆
            - 2 万兆
    - IDC节点 数十个
    - 覆盖 5大运营商，数十个小ISP

看到递归DNS的IP，
    就近访问来实现加速

GSLB 七层
    看到实际用户的出口IP


业务支撑系统

* 服务基层监控
* 可用性监控
    - local dns 模拟各地的访问

看哪些用户服务访问不好，配置错误dns，挖掘
找下专利

* 服务质量监控
* 日志统计

技术与选型：

* 如何选择？
    - 是否很好的满足需求
    - 都有谁在用，别做小白鼠
    - 社区活跃度，文档是否丰富（看中文文档，中国情况不同）
        * 商业版 -- 开源版
    - 在对性能没有机制要求的场景，要追求开发效率
    - 技术只是工具 -- 商业模式，支撑工具
    - 在风险可控的前提下尝鲜

* 开发语言要统一
* 运维工具
    - puppet
    - 任务系统
* 数据存储
    - MySQL
    - MongoDB 大量随机读写，性能差
    - HDFS -- Gluster FS (雪糕视频)
* WebServer AppServer
    - Nginx 本地的cache
    - Passenger
* 消息队列
    - Kestrel 小众，很失败
* 缓存
    - memcached 内部文件缓存

大文件下载的优化：
    sata盘 -- 随机读写太过频繁
    sas盘 -- 性能也不行，带宽占不满
    pcie flash cache ssd -- IO下来，带宽上去
    迅雷盗链  P2SP (server peer)


性能增加4被，节省3台服务器和机架的费用
ssd贵，节约的费用更多
单点故障

flash ssd和sata接口的ssd性能会不会差很多？
intel 商用sata ssd   nvme
三星
镁光
性能抖动


* 如何更好的去讲清楚一个架构，更好的发好架构各组件之间的层次关系？

自顶向下的意识
1.系统是干什么的
2.逻辑功能
3.代码功能

架构的两个维度
横向 几个逻辑子功能
纵向 

如何描述一个系统？

开源生态 + 架构知识在更高层次的抽象
看出不同
更要看出各个系统的相同处
