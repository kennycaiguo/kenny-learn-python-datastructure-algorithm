"""
python实现队列数据结构
队列只能从一端存入数据另外一端取出数据
存放数据的一端叫做队尾，取出数据的一端叫做队头
"""


class Queue(object):
    def __init__(self):
        self.__items = []  # 存储元素的空间是一个顺序表，在python中就是列表，必须是私有的否则用户可以任意修改，失去意义


    def enqueue(self, item):  # 入队 采用头插法
        self.__items.insert(0,item)

    # 出栈，从栈顶弹出一个元素
    def dequeue(self):  # 出队 从后面弹出
        return self.__items.pop(-1)



    # 判断栈是否为空
    def is_empty(self):
        return self.__items == []

    # 返回栈元素个数
    def size(self):
        if self.__items:
            return len(self.__items)
        else:
            return 0


if __name__ == '__main__':
    s = Queue()
    print(s.size())
    print(s.is_empty())
    s.enqueue(100)
    s.enqueue(200)
    s.enqueue(300)
    print(s.is_empty())
    print(s.size())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())