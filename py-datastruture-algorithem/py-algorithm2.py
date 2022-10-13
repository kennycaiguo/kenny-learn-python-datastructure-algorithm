from timeit import Timer


def timeit_demo1():  # 耗时第三长
    li = []
    for i in range(10000):
        li.append(i)
    return None


def timeit_demo2():  # 耗时第四长
    li = []
    for i in range(10000):
        li += [i]
    return None


def timeit_demo3():  # 耗时第二长
    li = []
    for i in range(10000):
        li.extend([i])
    return None


def timeit_demo4():  # 比较省时间
    li = [i for i in range(10000)]
    return None


def timeit_demo5():  # 最省时间
    li = list(range(10000))
    return None

def timeit_demo6():  # 耗时最长
    li = []
    for i in range(10000):
        # li.insert(0,i)
        li.insert(i,i)


if __name__ == '__main__':
    # 构造运算器
    timer1 = Timer("timeit_demo1()", "from __main__ import timeit_demo1")
    # 运行运算器，返回耗时
    print(timer1.timeit(1000))
    timer2 = Timer("timeit_demo2()", "from __main__ import timeit_demo2")
    # 运行运算器，返回耗时
    print(timer2.timeit(1000))
    timer3 = Timer("timeit_demo3()", "from __main__ import timeit_demo3")
    # 运行运算器，返回耗时
    print(timer3.timeit(1000))
    timer4 = Timer("timeit_demo4()", "from __main__ import timeit_demo4")
    # 运行运算器，返回耗时
    print(timer4.timeit(1000))
    timer5 = Timer("timeit_demo5()", "from __main__ import timeit_demo5")
    # 运行运算器，返回耗时
    print(timer5.timeit(1000))
    timer6 = Timer("timeit_demo6()", "from __main__ import timeit_demo6")
    # 运行运算器，返回耗时
    print(timer6.timeit(1000))
