# set_demo.py
集合 无序不重复
In [134]: s=set()

In [135]: s.add(1)

In [136]: s.add(2)

In [137]: s.add(3)

In [138]: s
Out[138]: {1, 2, 3}

In [139]: s.add(3)
去重

In [140]: s
Out[140]: {1, 2, 3}


构造
In [141]: b=set(range(3,9))

In [142]: b
Out[142]: {3, 4, 5, 6, 7, 8}

集合运算
In [142]: b
Out[142]: {3, 4, 5, 6, 7, 8}

In [143]: s
Out[143]: {1, 2, 3}

In [144]: s&b
Out[144]: {3}

In [145]: s|b
Out[145]: {1, 2, 3, 4, 5, 6, 7, 8}

In [146]: s-b
Out[146]: {1, 2}

In [147]: b-s
Out[147]: {4, 5, 6, 7, 8}

查函数
In [148]: dir(s)
查具体内容
In [149]: help(s)
In [150]: help(s.add)