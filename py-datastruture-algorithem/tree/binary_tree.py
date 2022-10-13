"""
二叉树
树是一种类似链表的结构,这里是无参构造
如何根据输出的顺序反推一颗二叉树？，注意一定要有中序输出，否则没有办法，可是先序跟中序，也可以是中序跟后序"""


class Node(object):  # 树节点,继承自SingleLinkList
    def __init__(self, elem=-1):
        self.elem = elem
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, item):  # 这里只考虑append的情况
        node = Node(item)
        # 处理根节点为空的情况
        if self.root is None:
            self.root = node
            return  # 处理完了就可以退出
        queue = [self.root]  # 用来处理节点

        # 需要循环处理每一个节点
        while queue:
            cur_node = queue.pop(0)  # 取出节点
            # 如果这个节点的左边孩子是空的，就将新节点添加到左边
            if cur_node.lchild is None:  # 先处理左孩子
                cur_node.lchild = node
                return  # 添加完可以退出
            else:
                queue.append(cur_node.lchild)  # 否则需要添加到队列处理
            if cur_node.rchild is None:  # 再处理右孩子
                cur_node.rchild = node
                return  # 添加完可以退出
            else:
                queue.append(cur_node.rchild)  # 否则需要添加到队列处理

        # 广度优先遍历

    def breadth_travel(self):
        # 处理根节点为空的情况
        if self.root is None:
            return
        queue = [self.root]  # 用来处理节点
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            # 先处理左孩子
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)

            # 再处理右孩子
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    # 深度优先，有三种顺序，先序，中序，后序，注意树的遍历永远都是先左子树，再右子树！！！！
    # 先序,根节点-左子树-右子树
    def pre_order(self, node):
        if node is None:
            return
        print(node.elem)
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    # 中序， 左子树-根节点-右子树
    def mid_order(self, node):
        if node is None:
            return
        self.mid_order(node.lchild)
        print(node.elem)
        self.mid_order(node.rchild)

    # 后序，左子树-右子树-根节点
    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem)


if __name__ == '__main__':
    btree = BinaryTree()
    btree.add(0)
    btree.add(1)
    btree.add(2)
    btree.add(3)
    btree.add(4)
    btree.add(5)
    btree.add(6)
    btree.add(7)
    btree.add(8)
    btree.add(9)

    # btree.breadth_travel()
    # btree.pre_order(btree.root)
    btree.mid_order(btree.root)
    # btree.post_order(btree.root)