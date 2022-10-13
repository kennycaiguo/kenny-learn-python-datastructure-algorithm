"""
归并排序法,又是一个递归算法
思想：将需要排序的列表拆分为两个部分，然后这两个部分的每个部分有拆分成两个部分，如此一直进行，直到最后分成的所有部分都只有一个元素
然后每两个部分进行合并排序，一直进行直到所有的部分都合并了，排序完成
这个排序用的不多
"""


def merge_sort(alist):  # 这个方法不改变原来的列表，必须接收方法返回值来获取排好序的列表
    n = len(alist)
    # 递归退出条件
    if n <= 1:
        return alist
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])  # 注意：如果这里的开始位置改为mid+1，最终得到的列表注意原来列表的一半元素！！！！

    left_p, right_p = 0, 0  # 需要两个游标，默认分别指向左右两部分的第一个元素
    result = []
    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            result.append(left[left_p])
            left_p += 1
        else:
            result.append(right[right_p])
            right_p += 1
    # 循环退出后一定有一边还有剩余的数，我们就把剩余的添加到result中，因为不能够确定是哪边先移动完成，所有采用下面的写法
    result += left[left_p:]  # 使用切片是比较保险的
    result += right[right_p:]
    return result


def merge_sort2(alist):  # 功能相同但是可以在源列表排序，也就是就地排序
    n = len(alist)
    # 递归退出条件
    if n <= 1:
        return alist
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])  # 注意：如果这里的开始位置改为mid+1，最终得到的列表注意原来列表的一半元素！！！！

    left_p, right_p = 0, 0  # 需要两个游标，默认分别指向左右两部分的第一个元素
    result = []
    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            result.append(left[left_p])
            left_p += 1
        else:
            result.append(right[right_p])
            right_p += 1
    # 循环退出后一定有一边还有剩余的数，我们就把剩余的添加到result中，因为不能够确定是哪边先移动完成，所有采用下面的写法
    result += left[left_p:]  # 使用切片是比较保险的
    result += right[right_p:]
    # alist=[]
    for i in range(len(result)):
        alist[i] = result[i]  # 注意如果这里使用append就不能达到排序的目的，因为这里是alist是一个副本，必须使用地址


# def merge(left, right):
#     left_p, right_p = 0, 0  # 需要两个游标，默认分别指向左右两部分的第一个元素
#     result = []
#     while left_p < len(left) and right_p < len(right):
#         if left[left_p] < right[right_p]:
#             result.append(left[left_p])
#             left_p += 1
#         else:
#             result.append(right[right_p])
#             right_p += 1
#     # 循环退出后一定有一边还有剩余的数，我们就把剩余的添加到result中，因为不能够确定是哪边先移动完成，所有采用下面的写法
#     result += left[left_p:]  # 使用切片是比较保险的
#     result += right[right_p:]
#     return result


if __name__ == '__main__':
    l1 = [54, 266, 93, 17, 77, 31, 44, 55, 20]
    print(l1)
    # l1 = merge_sort(l1)
    # print(l1)
    merge_sort2(l1)
    print(l1)
