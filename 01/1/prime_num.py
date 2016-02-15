# coding:utf-8
# 求素数作业
# https://program-think.blogspot.com/2011/12/prime-algorithm-1.html
def prime_num(num):
    for i in range(2,num/2):
        if num % i == 0:
            return False
    return True


print [x for x in range(100) if prime_num(x)]