
class Node(object):  # 双向链表节点,继承自SingleLinkList
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):  # 使用继承
    def __init__(self, node=None):  #单链表和双链表通用的方法可以不写
        self.__head = node

        # 判断链表是否为空

    def is_empty(self):  # 跟单链表一样
        return self.__head is None  # 推荐写法

        # 获取链表的长度

    def length(self):  # 跟单链表一样
        cur = self.__head  # 用来遍历节点的
        count = 0  # 计数器，用来计算节点数
        while cur != None:
            count += 1
            cur = cur.next
        return count

        # 遍历整个链表

    def travel(self):  # 需要一个游标变量cur  # 跟单链表一样
        cur = self.__head  # 用来遍历节点的
        while cur != None:
            print(cur.elem,end=" ") # print命令不换行的写法
            cur = cur.next
        print(" ")
    # 在链表的头部添加元素

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
        if node.next:
            node.next.prev = node

        # 在链表的尾部添加元素

    def append(self, item):  # 注意，这里的item不是一个节点，他是一个数，我们需要用这个数来创建一个节点对象再添加到链表末尾
        node = Node(item)
        # 空链表处理
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:  # 注意这里的条件和遍历，计算链表长度的判断条件有点不一样
                cur = cur.next
            cur.next = node
            node.prev = cur

        # 在指定的位置插入元素

    def insert(self, pos, item):  # pos是从0开始的, 双向链表只需要一个游标
        node = Node(item)
        # 需要处理特殊情况。如pos<=0,此时我们使用头插法
        if pos <= 0:
            self.add(item)  # 调用头插法
        elif pos > (self.length() - 1):  # 位置比链表的长度还大，使用尾插法
            self.append(item)
        else:
            cur = self.__head
            count = 0  # 位置计数器
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

        # 删除节点,需要两个游标，如果使用一个的话比较难理解

    def remove(self, item): # 双链表只需要一个游标

        cur = self.__head  # 当前游标
        while cur != None:
            if cur.elem == item:
                # 先判断是否是头节点
                if cur == self.__head:  # 是头节点
                    self.__head = cur.next
                    if cur.next:  # 当链表的节点多于一个才做下面的操作，否则会引发异常
                        cur.next.prev = None
                    break
                else:  # 不是头节点
                    cur.prev.next = cur.next
                    if cur.next:  # 当链需要删除的节点是表的末尾节点需要做这个判断，否则会引发异常
                        cur.next.prev = cur.prev
                    break
            else:
                cur = cur.next

        # 查找节点

    def search(self, item):
        cur = self.__head
        # 先把第一个节点的elem和item进行比较，如果相等，就返回True，否则cur往后移动，重复这个过程，直到找到相等的值返回True
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 当循环退出还没有找到，就返回False
        return False


if __name__ == '__main__':
    dbl_list = DoubleLinkList()
    # 判断是否是空的
    print(dbl_list.is_empty())
    # 计算长度
    # print(dbl_list.length())
    # 前插入
    dbl_list.add(100)
    print(dbl_list.length())
    dbl_list.append(200)
    dbl_list.travel()
    dbl_list.insert(1,300)
    dbl_list.travel()
    dbl_list.remove(300)
    dbl_list.travel()
    print(dbl_list.length())
    print(dbl_list.is_empty())
    dbl_list.add(400)
    dbl_list.travel()
    print(dbl_list.search(500))
    dbl_list.remove(400)
    dbl_list.travel()
    dbl_list.insert(-1,500)
    dbl_list.travel()
    dbl_list.insert(5,600)
    dbl_list.travel()
