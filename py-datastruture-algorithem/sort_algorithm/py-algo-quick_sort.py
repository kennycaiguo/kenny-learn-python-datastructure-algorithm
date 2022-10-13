"""
快速排序法
ctrl+alt+v ---- 提取变量的快捷方式
开始排序使用得多，但是如果需要保序，该方法不能使用
"""


def quick_sort(alist, first, last):
    # 这是一个递归函数，必须设置递归终止条件
    if first >= last:
        return
    # 保存第一个数，作为中间变量
    mid_val = alist[first]
    # 计算列表的长度
    n = len(alist)
    # 需要作用两个游标low，high
    low = first  # 刚开始low是指向第一个元素的
    high = last  # 刚开始high是指向最后一个元素的

    # 先移动右边游标
    while low < high:
        while low < high and alist[high] >= mid_val:  # 控制游标移动的循环,可以在这里处理相等的情况，也可以在下面的循环在处理
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_val:  # 控制游标移动的循环
            low += 1
        alist[high] = alist[low]
    # 当这一层循环退出，low==high
    alist[low] = mid_val
    # 对 左右两边进行递归
    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last)


if __name__ == '__main__':
    li = [54, 266, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
