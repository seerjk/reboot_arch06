# list_demo.py
base
len
cap

切片有拷贝

In [90]: x=1000

In [91]: l=range(x)

In [92]: m=2

In [93]: n=10

In [94]: l[m:n]
Out[94]: [2, 3, 4, 5, 6, 7, 8, 9]


切片时间复杂度 n-m，与切片的长度有关



In [95]: id(l[m])
Out[95]: 13847632

In [96]: l1=l[m:n]


In [98]: id(l1[0])
Out[98]: 13847632

整数同一个，只是整数是同一个位置（对整数的引用）

python有对小整数进行缓存 -10~200多，预先生成这些整数对象
小整数的缓存造成的 两个值一样

解释器的语言

In [99]: n=10

In [100]: nn=10

In [101]: id(n)
Out[101]: 13847440

In [102]: id(nn)
Out[102]: 13847440


In [103]: a=1000

In [104]: aa=1000

In [105]: id(a)
Out[105]: 27679184

In [106]: id(aa)
Out[106]: 27679160


----
In [107]: l=range(9)

In [108]: l1=[]

In [110]: for i in l:      
    l1.append(i*2)
   .....:     

In [111]: l1
Out[111]: [0, 2, 4, 6, 8, 10, 12, 14, 16]

列表推到式

In [113]: l=range(9)

In [114]: l
Out[114]: [0, 1, 2, 3, 4, 5, 6, 7, 8]

In [115]: l2=[x*2 for x in l]

In [116]: l2
Out[116]: [0, 2, 4, 6, 8, 10, 12, 14, 16]

In [117]: l3=[x*2 for x in l if x % 3 == 0]

In [118]: l3
Out[118]: [0, 6, 12]


----
In [151]: l=range(9)

In [152]: l
Out[152]: [0, 1, 2, 3, 4, 5, 6, 7, 8]

In [153]: 6 in l
Out[153]: True

练习
列表推到式 求100以内的质数
