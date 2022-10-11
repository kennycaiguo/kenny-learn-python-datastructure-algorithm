"""
python实现栈数据结构
"""


class Stack(object):
    def __init__(self):
        self.__items = []  # 存储元素的空间是一个顺序表，在python中就是列表，必须是私有的否则用户可以任意修改，失去意义

    # 入栈，添加一个元素到栈顶
    def push(self, item):  # 可以选择将头部作为栈顶或者尾部作为栈顶，但是一旦确定后就只能在这个方向添加，删除数据了
        self.__items.append(item)  # 这里选择将尾部作为栈顶

    # 出栈，从栈顶弹出一个元素
    def pop(self):
        return self.__items.pop()

    # 返回栈顶元素
    def peek(self):
        if self.__items:
            return self.__items[-1]
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


if __name__ == '__main__':
    s = Stack()
    print(s.size())
    print(s.peek())
    s.push(100)
    s.push(200)
    s.push(300)
    # print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.size())
    print(s.is_empty())
    print(s.pop())
    print(s.pop())