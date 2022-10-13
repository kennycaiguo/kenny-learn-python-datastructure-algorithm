"""
希尔排序法
将一个无序列表看成是几个无序列表,然后分别使用插入排序法
这里有一个gap就是间隔
是一种不稳定排序
"""


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:  # 需要3层循环
        for j in range(gap,n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:  # 这个是优化写法
                    break
        gap //= 2



if __name__ == '__main__':
    li = [54, 266, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(li)
    print(li)
