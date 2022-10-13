'''
python实现选择排序法，这是一个不稳定排序，不是一个好方法
'''


def selective_sort(alist):
    sorted_l = []
    while len(alist) > 0:
        min = alist[0]
        for i in range(len(alist)):
            if min < alist[i]:
                min = alist[i]
        # sorted_l.append(min)
        sorted_l.insert(0, min)
        alist.remove(min)
        # print(sorted_l)
    return sorted_l


def selective_sort2(alist):
    n = len(alist)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1,n):
            if alist[min_index] > alist[j]:
                min_index = j  # 不要在这里交换值，需要在这里更新最小值下标，需要在内层循环的外面交换值
        alist[i], alist[min_index] = alist[min_index], alist[i]


if __name__ == '__main__':
    li = [54, 266, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    # li = selective_sort(li)
    selective_sort2(li)
    print(li)
