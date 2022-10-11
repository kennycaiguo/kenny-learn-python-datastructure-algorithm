"""
python实现单向链表
"""


# 定义一个链表节点类
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None


# 单向链表类的实现
class SingleLinkList(object):
    # 构造函数
    def __init__(self, node=None):  # 设置默认参数
        self.__head = node  # 创建一个空节点，而且是私有的（以双下划线__开头都是私有变量）

    # 判断链表是否为空
    def is_empty(self):
        return self.__head == None

    # 获取链表的长度
    def length(self):
        cur = self.__head  # 用来遍历节点的
        count = 0  # 计数器，用来计算节点数
        while cur != None:
            count += 1
            cur = cur.next
        return count

    # 遍历整个链表
    def travel(self):  # 需要一个游标变量cur
        cur = self.__head  # 用来遍历节点的
        while cur != None:
            # print(cur.elem,end=" ") # print命令不换行的写法
            print(cur.elem)
            cur = cur.next

    # 在链表的头部添加元素
    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

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

    # 在指定的位置插入元素
    def insert(self, pos, item):  # pos是从0开始的
        node = Node(item)
        # 需要处理特殊情况。如pos<=0,此时我们使用头插法
        if pos <= 0:
            self.add(item)  # 调用头插法
        elif pos > (self.length()-1): # 位置比链表的长度还大，使用尾插法
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
        pre = None  # 当前游标的前一个游标
        cur = self.__head  # 当前游标
        while cur != None:
            if cur.elem == item:
               # 先判断是否是头节点
               if cur == self.__head:  # 是头节点
                  self.__head = cur.next
                  break
               else: #不是头节点
                    pre.next = cur.next
                    break
            else:
                pre = cur  # 注意：一定要先移动pre再移动cur，这样子可以保证pre一直在cur前面
                cur = cur.next

    # 查找节点
    def search(self, item):
        cur = self.__head
        # 先把第一个节点的elem和item进行比较，如果相等，就返回True，否则cur往后移动，重复这个过程，直到找到相等的值返回True
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 当循环退出还没有找到，就返回False
        return False


if __name__ == '__main__':
    sl_list = SingleLinkList()
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
    sl_list.insert(3,600)
    # sl_list.travel()
    # print(sl_list.search(400))

    # 删除头
    # sl_list.remove(100)
    # sl_list.travel()
    #删除尾
    # sl_list.remove(600)
    # sl_list.travel()
    #删除中间
    sl_list.remove(200)
    sl_list.travel()
