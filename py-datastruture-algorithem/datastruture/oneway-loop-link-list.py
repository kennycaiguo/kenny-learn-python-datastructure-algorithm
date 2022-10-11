"""
python实现单向循环链表
"""


# 定义一个链表节点类
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None


# 单向循环链表类的实现
class SingleCycleLinkList(object):
    # 构造函数，注意与单链表的区别
    def __init__(self, node=None):  # 设置默认参数
        self.__head = node  # 创建一个空节点，而且是私有的（以双下划线__开头都是私有变量）
        # 因为是单向循环链表，所以即使只有一个节点也需要指向它自己
        if node:
            node.next = node

    # 判断链表是否为空
    def is_empty(self):
        return self.__head == None

    # 获取链表的长度,注意循环的推出添加
    def length(self):
        # 因为计数器是从1开始，所以需要处理开始时是空链表的情况
        if self.is_empty():
            return 0
        cur = self.__head  # 用来遍历节点的
        count = 1  # 计数器，用来计算节点数,这里不能从0开始
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    # 遍历整个链表
    def travel(self):  # 需要一个游标变量cur
        # 如果是空链表，直接返回
        if self.is_empty():
            return
        cur = self.__head  # 用来遍历节点的
        while cur.next != self.__head:
            print(cur.elem, end=" ")  # print命令不换行的写法
            # print(cur.elem)
            cur = cur.next
        print(cur.elem)  # 输出最后一个的值

    # 在链表的头部添加元素,有2种做法，这里使用第一种
    def add(self, item):
        node = Node(item)
        # 空链表的处理
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            # 通过遍历找出链表的尾节点
            while cur.next != self.__head:
                cur = cur.next
            # 当循环结束，就找到尾节点
            node.next = self.__head
            self.__head = node
            # cur.next = node # 单向循环链表的最后一个节点的next必须指向第一个节点
            cur.next = self.__head  # 单向循环链表的最后一个节点的next必须指向第一个节点

    # 在链表的尾部添加元素
    def append(self, item):  # 注意，这里的item不是一个节点，他是一个数，我们需要用这个数来创建一个节点对象再添加到链表末尾
        node = Node(item)
        # 空链表处理
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:  # 注意这里的条件和遍历，计算链表长度的判断条件有点不一样
                cur = cur.next
            # 方法1
            # cur.next = node
            # node.next = self.__head
            # 方法2
            node.next = cur.next
            cur.next = node

    # 在指定的位置插入元素,不需要改动
    def insert(self, pos, item):  # pos是从0开始的
        node = Node(item)
        # 需要处理特殊情况。如pos<=0,此时我们使用头插法
        if pos <= 0:
            self.add(item)  # 调用头插法
        elif pos > (self.length() - 1):  # 位置比链表的长度还大，使用尾插法
            self.append(item)
        else:
            pre = self.__head  # pre必须指向pos位置的节点的前一个节点否则无法完成操作
            count = 0  # 位置计数器
            while count < pos - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    # 删除节点,需要两个游标，如果使用一个的话比较难理解
    def remove(self, item):
        # 需要处理空链表的情况
        if self.is_empty():
            return
        pre = None  # 当前游标的前一个游标
        cur = self.__head  # 当前游标
        while cur.next != self.__head:
            if cur.elem == item:
                # 先判断是否是头节点,因为是单向循环链表，必须查找尾节点
                if cur == self.__head:  # 是头节点
                    # 需要另外一个游标来从头开始查找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 找到尾节点
                    # rear.next = cur.next
                    self.__head = cur.next
                    rear.next = self.__head

                else:  # 中间节点
                    pre.next = cur.next
                return  # 注意，如果这里使用break会引发异常，注意搞清楚上面时候使用break和上面时候使用return
            else:
                pre = cur  # 注意：一定要先移动pre再移动cur，这样子可以保证pre一直在cur前面
                cur = cur.next
        # 需要在这里处理尾节点的情况
        if cur.elem == item:
            if cur == self.__head:  # 必须处理只有一个节点是情况
                self.__head = None
            else:
                pre.next = cur.next  # 此时pre是None

    # 查找节点
    def search(self, item):
        # 处理空链表
        if self.is_empty():
            return False
        cur = self.__head
        # 先把第一个节点的elem和item进行比较，如果相等，就返回True，否则cur往后移动，重复这个过程，直到找到相等的值返回True
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 当循环退出还没有找到，就返回False,有找到还需要return True
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    sl_list = SingleCycleLinkList()
    print(sl_list.is_empty())
    print(sl_list.length())
    sl_list.append(100)
    print(sl_list.length())
    sl_list.append(200)
    sl_list.append(300)
    # print(sl_list.is_empty())
    # sl_list.travel()
    # print(sl_list.length())
    # sl_list.add(50)
    # sl_list.travel()
    # 测试头插法
    # sl_list.insert(-1,400)
    # sl_list.travel()
    # # 测试尾插法
    # sl_list.insert(3,500)
    # sl_list.travel()
    # 测试正常插法
    # sl_list.insert(2,600)
    # sl_list.travel()
    sl_list.insert(3, 600)
    sl_list.travel()
    print(sl_list.search(600))

    # 删除头
    sl_list.remove(100)
    sl_list.travel()
    # 删除尾
    # sl_list.remove(600)
    # sl_list.travel()
    # 删除中间
    # sl_list.remove(200)
    # sl_list.travel()
