# -*- coding: utf-8 -*-


def bubble_sort(raw_list):
    """
    冒泡排序：
    1. 从数组下标为0的位置开始，比较下标位置为0和1的数据，如果0号位置的大，则交换位置，如果1号位置大，则什么也不做，然后右移一个位置，
    2. 比较1号和2号的数据，和刚才的一样，如果1号的大，则交换位置，
    3. 以此类推直至最后一个位置结束，到此数组中最大的元素就被排到了最后，之后再根据之前的步骤开始排前面的数据，直至全部数据都排序完成。
    """

    _len = len(raw_list)
    for i in range(_len):
        for j in range(_len - 1):
            if raw_list[j] > raw_list[j + 1]:
                raw_list[j], raw_list[j + 1] = raw_list[j + 1], raw_list[j]

    return raw_list  # [1, 2, 3, 4, 8, 9]


def select_sort(raw_list):
    """
    选择排序：
    1. 在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换
    2. 在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
    3. 以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
    """

    _len = len(raw_list)
    for i in range(_len):
        min_index = i
        for j in range(i + 1, _len):
            if raw_list[j] < raw_list[min_index]:
                min_index = j
        raw_list[i], raw_list[min_index] = raw_list[min_index], raw_list[i]

    return raw_list  # [1, 2, 3, 4, 8, 9]


def quick_sort(raw_list):
    """
    快速排序：
    1. 先从数列中取出一个数作为基准数。
    2. 分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
    3. 再对左右区间重复第二步，直到各区间只有一个数。
    """

    if len(raw_list) < 2:
        return raw_list
    else:
        left = [i for i in raw_list[1:] if i < raw_list[0]]
        right = [j for j in raw_list[1:] if j > raw_list[0]]
        return quick_sort(left) + [raw_list[0]] + quick_sort(right)


def insert_sort(raw_list):
    """
    插入排序：
    1. 默认序列中的第0个元素是有序的（因为只有一个元素a[0]嘛，自然是有序的）；
    2. 从下标为1（下标0没啥好插的）的元素开始，取当前下标i位置处的元素a[i]保存到一个临时变量waitInsert里；
    3. waitInsert与对前半部分有序序列的循环遍历比较，直到遇到第一个比waitInsert大的元素（这里默认是从小到大排序），此时的下标为j，然后将其插入到j的位置即可；
    4. 因为前面的插入，导致后面元素向后推移一个位置，没关系，把原来下标i的元素弹出即可；
    5. 重复进行第2步到第4步，直到乱序序列中的元素被全部插入到有序序列中；
    6. 经过以上5个步骤之后，整体序列必然有序，排序完成。

    """

    _len = len(raw_list)
    for i in range(1, _len):
        for j in range(i):
            if raw_list[j] > raw_list[i]:
                raw_list.insert(j, raw_list[i])
                raw_list.pop(i + 1)
                break
    return raw_list


def shell_sort(raw_list):
    """
    希尔排序： [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    1. 设 gap1 = N / 2 = 5，即相隔距离为 5 的元素组成一组，可以分为 5 组。接下来，按照直接插入排序的方法对每个组进行排序。
    2. 把上次的 gap 缩小一半，即 gap2 = gap1 / 2 = 2 (取整数)。这样每相隔距离为 2 的元素组成一组，可以分为 2 组。按照直接插入排序的方法对每个组进行排序。
    3. 再次把 gap 缩小一半，即gap3 = gap2 / 2 = 1。 这样相隔距离为 1 的元素组成一组，即只有一组。按照直接插入排序的方法对每个组进行排序。此时，排序已经结束。
    需要注意一下的是，图中有两个相等数值的元素 5 和 5 。我们可以清楚的看到，在排序过程中，两个元素位置交换了。
    """

    _len = len(raw_list)
    gap = _len / 2
    while gap > 0:
        for i in range(gap, _len):
            tmp = raw_list[i]
            j = i
            while j >= gap and raw_list[j - gap] > tmp:
                raw_list[j] = raw_list[j - gap]
                j -= gap
            raw_list[j] = tmp
        gap = gap / 2
    return raw_list


print bubble_sort([1, 3, 4, 9, 8, 2])
print select_sort([1, 3, 4, 9, 8, 2])
print quick_sort([1, 3, 4, 9, 8, 2])  # [1, 2, 3, 4, 8, 9]
print insert_sort([1, 3, 4, 9, 8, 2])
print shell_sort([1, 3, 4, 9, 8, 2])
