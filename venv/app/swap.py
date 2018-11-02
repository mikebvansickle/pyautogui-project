import math

def sort(list):
    lowest = [list[0], 0]
    for i in range(0, len(list)):
        if list[i] < lowest[0]:
            lowest = [list[i], i]
    return lowest

def swapSort(list):
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if list[j] < list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

array = [25, 12, 250, 600, 34, 4, 12, 15]
print(array)
print(sort(array))

array = [25, 12, 250, 600, 34, 4, 12, 15]
print(array)
print(swapSort(array))
