# 装饰器 ( Decorator ) 的作用在于可以在代码运行期间动态增加功能
# 其本质就是一个返回函数的高阶函数
# 在 Python 中，在被装饰函数名称上部用 @ 添加装饰器
import functools


# 简单写法的装饰器只会被调用一次
def v_function_decorator(func):
    # 函数对象有一个__name__属性，可以拿到函数的名字
    print('v_function_decorator calls %s():' % func.__name__)
    return func


# decorator中使用嵌套函数，在嵌套函数中进行装饰，以保证每次调用函数Function都会调用wrapper函数，起到了装饰器的作用
def log(func):
    @functools.wraps(func)
    def wrapper():
        wrapper.count += 1
        print('log.wrapper calls %s(): Round ' % func.__name__, wrapper.count)
        return func()
    wrapper.count = 0
    return wrapper


# 一个装饰器的唯一需求是它的返回值可以被调用，这味着返回的对象必须实现 _call_ 这个方法
class MyDecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func()


# @MyDecorator
@log
# @v_function_decorator 等价于Function = v_function_decorator(Function),所以v_function_decorator函数本身只会调用一次。
@v_function_decorator
def v_function():
    print('I am the function!!!')


def v_function_caller(vf):
    print('I am caller.')
    vf()


# 函数对象可以被赋值给变量

v_function()
v_function()
v_function_caller(v_function)
v_function_caller(v_function)
print(v_function.__name__)
