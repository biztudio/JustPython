from functools import reduce


# Ref: MapReduce: Simplified Data Processing on Large Clusters (by Google)
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# map()函数作为高阶函数，体现的式对运算规则抽象的设计思想
def func(x):
    return x ** 2


print(list(map(func, [1, 2, 3, 4, 5, 6])))


# reduce()函数接收两个参数，一个是函数，一个是Iterable
# reduce()函数作用到序列上，把结果继续作用到下一个元素做积累计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fn(x, y):
    return x * 10 + y


reduce(fn, [1, 3, 5, 7, 9])

# 练习一，把一组大小写不规范的名字转成首字母大写的一组名字
names_list1 = ['sTevEn JOBs',
               'coCo lee',
               'JAck zhaNG',
               'LiSa ChEn',
               'georgE w bUsH',
               'PETER cHeN',
               'brUce Ho',
               'biLL W clinTON'
               ,'ciRAlI Clinton'
               ,'Yang SHEN'
               ,'elSA Y Shen'
               ,'robin zhAng'
               ,'Bruce LEE']


# 一个方法尽量只完成一个工作，便于单元测试的设计
def normalize_name(abnormal_name):
    return reduce(lambda n1, n2: n1+' '+n2, list(map(lambda n: n[0].upper()+n[1:].lower(), abnormal_name.split(' '))))


# 由于设计原因，在python 3 很多场景其实推荐使用直接的推导式替代 map / reduce
def normalize_name_via_loop(abnormal_names):
    return [' '.join([n[0].upper() + n[1:].lower() for n in name.split(' ')]) for name in abnormal_names]

names_list2 = list(map(normalize_name, names_list1))
print(names_list2)
names_list3 = normalize_name_via_loop(names_list1)
print(names_list3)


# 练习二，把练习一中大小写规范好的名字列表姓氏(最后一个词作为姓氏)分组, 组名就是姓氏
# 形如 {'Jobs':['Steven Jobs'], 'Zhang':['Robin Zhang','Jack Zhang'] ... }






# reduce 具有一定的局限性，所以在 python3 中被从内建库取消了 http://www.artima.com/weblogs/viewpost.jsp?thread=98196
# reduce 在python3 中被迁移到 functools
# 其对于 + 或者 * 运算还是十分方便的