'''
python实现冒泡排序法，是一个稳定排序
普通的冒泡排序法有一个缺点，即使你输入一个已经排好序的列表，它仍然需要进行一样的操作，这样子非常浪费时间
我们有一个优化的办法，就是在外层循环用一个遍量来聚类内层循环的次数，如果每一次count但是0，什么不需要排序，直接推出
'''


def bubble_sort(alist):
    for i in range(0, len(alist)):
        for j in range(0, len(alist)):
            if alist[i] < alist[j]:
                alist[j], alist[i] = alist[i], alist[j]
            else:
                continue


def bubble_sort2(alist):  # 这种写法比较好理解
    n = len(alist)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


def bubble_sort3(alist):  # 这种写法比较难理解
    n = len(alist)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


# 冒泡排序法的改进：记录每一趟的交换次数
def bubble_sort2_enhanced(alist):  # 这种写法比较好理解
    n = len(alist)
    for i in range(0, n - 1):
        count = 0
        for j in range(0, n - 1 - i):

            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        if count == 0:  # count == 0 表明这个列表是有序的，根本就不需要排序
            break


if __name__ == '__main__':
    l = [2, 4, 78, 12, 1, 3, 56]
    # l2 = [300, 100, 50, 500, 10, 600]
    # # bubble_sort(l2)
    # bubble_sort2(l)
    # print(l)
    l_good = [1, 2, 3, 4, 12, 56, 78]
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort2_enhanced(l_good)
    print(l_good)
