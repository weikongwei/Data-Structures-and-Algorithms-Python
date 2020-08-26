def insertionSort(array):
    lenth = len(array)
    for i in range(1,lenth):
        if array[i] < array[i-1]:
          for j in range(0,i-1):
              if array[j] > array[i]:
                  array.insert(j,array[i])
                  array.pop(i+1)
    return array


array = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertionSort(array))











# def insertionsort(array):
#     length = len(array)
#     i = 1
#     end = array[0]
#     while i < length:
#         if array[i] < end:
#             x = array.pop(i)
#             for j in range(0, i):
#                 if x < array[j]:
#                     array.insert(j, x)
#                     break
#         end = array[i]
#         i += 1
#     return array
#
#
# array = [6, 5, 3, 1, 8, 7, 2, 4]
# print(insertionsort(array))
