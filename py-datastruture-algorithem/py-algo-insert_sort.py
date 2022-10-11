"""
python实现插入排序法
实现思路，将需要排序的数据分为有序和无须两部分，然后不断从无序部分插入数据到有序部分。。。直到完成
时间复杂度是O(n^2) 但是可以优化为O(n)
这个是稳定排序法
"""


def insert_sort(alist):  # 这是经过优化的写法
    for i in range(1, len(alist)):
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            # i -= 1 # 没有else的话,i的减少需要写在这里
            else:  # 这个是优化写法
                break
            i -= 1  # 有else的话,i的减少需要写在这里


def insert_sort2(alist):  # 注意不同循环实现同一操作的不同写法,这个是没有优化的写法,时间复杂度很大
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


if __name__ == '__main__':
    li = [54, 266, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)
