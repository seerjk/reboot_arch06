# tuple_demo.py

只读list

In [119]: t=(2,3,5)

In [120]: t[0]=34
---------------------------------------------------------------------------
TypeError 


拆包
In [122]: st=(100, 'aa', 'pc')

In [123]: id, name, teacher = st

In [124]: id
Out[124]: 100

In [125]: name
Out[125]: 'aa'

In [126]: teacher
Out[126]: 'pc'



* zip() 打包 用于tuple

In [127]: l=range(20, 30)

In [128]: l
Out[128]: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

In [129]: zip(range(len(l)), l)
Out[129]: 
[(0, 20),
 (1, 21),
 (2, 22),
 (3, 23),
 (4, 24),
 (5, 25),
 (6, 26),
 (7, 27),
 (8, 28),
 (9, 29)]

 In [130]: zip([2,3,4], [10,20,30])
Out[130]: [(2, 10), (3, 20), (4, 30)]

In [131]: for m, n in zip([2,3,4], [10,20,30]):
   .....:     print m, n
   .....:     
2 10
3 20
4 30

In [133]: for n,m,q in [(1,2,3)]:
   .....:     print n,m,q
   .....:     
1 2 3