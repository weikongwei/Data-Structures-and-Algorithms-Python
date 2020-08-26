def selectionSort(array):
    for i in range(len(array)):
        minNum = array[i]
        for j in range(i + 1, len(array)):
            if array[j] < minNum:
                minNum = array[j]
                index = j
        array[i], array[index] = array[index], array[i]
    return array

array = [8, 6, 5, 0, 4, 3, 2]
print(selectionSort(array))

# def selectionsort(array):
#     i = 0
#     while i < len(array):
#         min = array[i]
#         index = i
#         for j in range(i + 1, len(array)):
#             if array[j] < min:
#                 index = j
#                 min = array[j]
#         array[i], array[index] = array[index], array[i]
#         i += 1
#
# #     return array
#
#
# array = [8, 6, 5, 0, 4, 3, 2]
# print(selectionsort(array))
