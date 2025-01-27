
# 选择排序
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    new_arr = []
    copiedArr = list(arr)  # 修改数组前先复制它
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        new_arr.append(copiedArr.pop(smallest))
    return new_arr

print(selectionSort([5, 2, 3, 1]))