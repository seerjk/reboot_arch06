# struct_class.py
# coding:utf-8

class F:
    pass

# tuple

std_id = [10, 11, 23]
name = ["student1", "st2", "st3"]
teacher = ["pc", "pc", "binggan"]

# def print_name(std_id, name):
#     # 10:"student1"
#     print "%d:%s" % (std_id, name)


# print_name(std_id[0], name[0])

def print_name(std_id, name, teacher):
    # 10:"student1"
    print "%d:%s:%s" % (std_id, name, teacher)

print_name(std_id[0], name[0], teacher[0])

# 具体一个事物的属性
# print_name(student[0])

