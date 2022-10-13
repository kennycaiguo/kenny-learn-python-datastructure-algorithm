"""
查找算法，就是指在一个序列在查找某一个数是否存在
常见的查找方法：顺序查找，二分法查找，二叉树查找，哈希查找
"""


# 二分法查找，前提是这个列表已经经过排序处理，是一个有序列表，不能用于链表
def binary_search(lst, num):  # 递归版本，不需要游标
    lst.sort()  # 这里先对一个列表进行从小到大的排序，然后才做搜索，这样子就可以在无序的列表在搜索了
    n = len(lst)
    if n > 0:
        mid = n // 2
        if num ==lst[mid]:
            return True
        elif num < lst[mid]:
            # start = mid
            return binary_search(lst[:mid], num)
        else :
            # end = mid
            return binary_search(lst[mid+1:], num)
    return False



def binary_search_no_recursive(lst, num):   # 非递归算法需要两个游标
    lst.sort()  # 先对列表进行升序排序因为这个查找方法需要从小到大排列的列表
    n = len(lst)
    first = 0   # 起点游标
    last = n-1  # 终点游标
    while first <= last:  # 注意如果这里不包含相等的情况，是无法找到元素的
        mid = (first + last) // 2
        if num == lst[mid]:
            return True
        elif num < lst[mid]:
            last = mid-1
        else:
            first = mid+1
    return False


if __name__ == '__main__':
    li = [17, 20, 31, 44, 54, 55, 77, 93, 266]
    l2 = [54, 266, 93, 17, 77, 31, 44, 55, 20]
    # print(binary_search(l2, 31))
    # print(binary_search(l2, 66))
    print(binary_search_no_recursive(l2,66))
    print(binary_search_no_recursive(l2,17))
