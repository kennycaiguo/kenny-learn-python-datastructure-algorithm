"""
python实现队双向列数据结构
双向列数据结构可以从两个方向存取数据
"""


class Deque(object):
    def __init__(self):
        self.__items = []  # 存储元素的空间是一个顺序表，在python中就是列表，必须是私有的否则用户可以任意修改，失去意义

    # 从头部添加一个元素
    def add_front(self, item):
        self.__items.insert(0, item)

    # 从尾部添加一个元素
    def add_rear(self, item):
        self.__items.append(item)

    # 从头部删除一个元素
    def pop_front(self):
        if self.__items:
            return self.__items.pop(0)
        else:
            return None

    # 从尾部删除一个元素
    def pop_rear(self):
        if self.__items:
            return self.__items.pop()
        else:
            return None

    # 判断栈是否为空
    def is_empty(self):
        return self.__items == []

    # 返回栈元素个数
    def size(self):
        if self.__items:
            return len(self.__items)
        else:
            return 0


def test_dome1():
    s = Deque()
    print(s.size())
    print(s.is_empty())
    s.add_front(100)
    # print(s.size())
    s.add_rear(200)
    # print(s.pop_front())
    print(s.size())
    print(s.pop_rear())
    print(s.size())


def test_dome2():
    s = Deque()
    s.add_front(100)
    s.add_front(200)
    s.add_front(300)
    # print(s.pop_rear())
    # print(s.pop_rear())
    # print(s.pop_rear())
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())

def test_demo3():
    d = Deque()
    d.add_rear(100)
    d.add_rear(200)
    d.add_rear(300)
    # print(d.pop_rear())
    # print(d.pop_rear())
    # print(d.pop_rear())
    print(d.pop_front())
    print(d.pop_front())
    print(d.pop_front())
    print(d.pop_front())
if __name__ == '__main__':
    # test_dome1()
    # test_dome2()
    test_demo3()
