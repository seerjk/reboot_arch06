# arch_share_01_redis.py

redis cluster 特性
redis cluster 高可用
redis cluster 使用和部署
redis cluster 选举算法Raft


## 1.redis cluster 特性

* 高性能
    - 最大集群规模 1000
* 一致性
    - 强一致性
    - 只有master提供服务
    - slave只是备份用，不提供读和写服务
    - 数据在多个master分布用Hash，可以人工干预的hash
* 可用性
    - 容忍多数网络分区
    - HA
* 数据丢失
    - Redis 只是一个缓存，不是数据库
    - 少数情况下可能 Best Effort

### 1.1 高性能

![redis_clients_topology](redis_clients_topology.png)

* 最多1000个节点
    - 因为所有节点两两相连
    - C(1000,2)=1000*999/2 ~ 500000

* 所有节点两两相连
* TCP端口，服务端口+4000，6379:10379
    - redis: 6379  gossip+4000: 10379

* Gossip 二进制协议，为带宽和速度优化
    - Gossip 一群节点在底下窃窃私语

* Client 和 Server用ASCII协议通信
* 很低的Overhead

* 节点不代理任何请求
    - 减少每个请求的环节

### 1.2 Gossip通信协议
![](redis_ping-pong.png)

* ping-pong协议

idle 忙音，没有回应
超过1000个节点，大量小包，会有网络风暴


### 1.3 Hash

* 最多1000个节点
    - Gossip协议
    - 用户只能操作自己有权限的树节点
* 4096个哈希槽
    - slot = crc16("key") mod 4096

redis内存配置：
redis 保守配置不超过 机器内存的50% (70% ~ 80%)
dump rdb -- 进程会fork一个兄弟进程 (kernel cow 特性，无变化不完全拷贝)
如果同时有大写入，会把所有内存都copy一遍，用满内存(oom -- out of memory)随机杀死进程。
awwwapp.com

redis单线程
    * 几个core开几个redis
    * 单线程占用大量资源 -- 关闭 超线程 (HT技术)

## 2. redis cluster 使用

图
![](redis_HA_topology.png)

### 2.1 高可用
一主n从 (replicas-per-hashslot)

* 最多可以容忍n节点宕机

最坏情况下同一个分片出现多个宕机，如果继续在使用本分片宕机，就不能再保证高可用了。

* 任何情况下每个分片
*

### 2.2 数据丢失
* case1
    - 网络分割，master 在 grace time(优雅时间)中master恢复，变成slave
* case2
    - 

* 人祸 -- 群集中机器挂了一大片，分片全部挂完

### 2.3 两种请求模式
* 粗暴版
    1. client => A: GET foo
    2. A+> client:

* 智能版


### 2.4 使用注意
* NO LVS and haproxy
    - 不知道请求落到谁上
    - Redis Cluster 自带完善的高可用解决方案，不需要任何的“proxy”
* 优先使用智能版
    - client操作效率高2倍
* 长连接
    - “智能版”Client为了提升效率会尽量多的和Server保持长连接。
    - 所以，Redis Client代码的实例尽量复用
* 管理域配置
    - redis-trib客户端进行各种配置
* re-sharding
    - redis-trib
* 选举算法
    - Raft ~ Paxos选举 + Slave冷跟随
        * Paxos: google论文, zookeeper

## 3. redis cluster 选举算法Raft
### 3.1 Paxos & Raft
* Paxos
https://zh.wikipedia.org/wiki/Paxos%E7%AE%97%E6%B3%95

投票选举，在有争议的情况下设置规则，防止决定摇摆

P1 P2 要都过半数，一定至少有一个A是重合的，
    - 重合的A是决定的关键


分布式系统中的节点通信存在两种模型：
共享内存（Shared memory）
消息传递（Messages passing）

算法的提出与证明

首先将议员的角色分为proposers，acceptors，和learners（允许身兼数职）。proposers提出提案，提案信息包括提案编号和提议的value；acceptor收到提案后可以接受（accept）提案，若提案获得多数acceptors的接受，则称该提案被批准（chosen）；learners只能“学习”被批准的提案。划分角色后，就可以更精确的定义问题：

决议（value）只有在被proposers提出后才能被批准（未经批准的决议称为“提案（proposal）”）；
在一次Paxos算法的执行实例中，只批准（chosen）一个value；
learners只能获得被批准（chosen）的value。


P1：一个acceptor必须接受（accept）第一次收到的提案。

P2：一旦一个具有value v的提案被批准（chosen），那么之后批准（chosen）的提案必须具有value v。
    P2a：一旦一个具有value v的提案被批准（chosen），那么之后任何acceptor再次接受（accept）的提案必须具有value v。
    P2b：一旦一个具有value v的提案被批准（chosen），那么以后任何proposer提出的提案必须具有value v。

paxos 每次写入都要选举
奇数  5 (3,2)
偶数个 -- 6 (4,2) 设置每个机器的权重

* Raft
https://raft.github.io/
https://en.wikipedia.org/wiki/Raft_(computer_science)

改进效率：
只在选举老大master的时候使用paxos投票，后面写入的时候全都听master的





# 运维职业规划

* 运维基础 (基础运维)
    - linux
    - yum
    - lamp
    - 运维基本概念
* 工具语言 (掌握运维)
    - shell (面向过程)
    - 业务运维
    - 理解工具 cacti zabbix等工具
* 开发思维 (开发的初级阶段 -- python写小工具)
    - 语言研究者
    - 优化与挑毛病 (业务部署，性能等)
    - 设计与逻辑思维 (数据结构和算法)
* 架构和平台思维 (转到业务)
    - 工具 --> 平台(支撑多问题的解决)
    - 架构研究者 (zabbix架构，why cs，通信，数据存储)
    - 知识的迁移 (zabbix 对比 cacti，写平台的时候借鉴)
* 体系 开源生态 (运维总监，运开总监，业务leader)
    - 知识体系化 (cache, mongo, hdfs等选型)
    - 深度拥抱开源
    - 技术方向感

开发思维解决运维问题


## 学习的境界

* 独上西楼
    - 认识到要转型
* 衣带渐宽终不悔
    - 学习转型付出的代价(真正学习东西)
* 蓦然回首
    - 根据要求做，去问问题


## 语言的学习

词汇和语法不是全部内容
开发只是思维
语言只是工具

* 词汇
* 语法
* 听力
* 口语
* 写作

## 计算机的学习
语法也不是计算机语言的全部

* 词汇
* 语法
* 数据结构
* 算法
* 架构

## 解决问题的过程

提出问题
分析问题
设计算法
编写程序
调试程序
得到结果

### 算法
数据结构 (c语言版) 清华 -- 看到排序

### 实践动手能力

### 技术选型和架构能力
T字型的人才
 —— 横  知识面 开源的
 |  竖  深度

