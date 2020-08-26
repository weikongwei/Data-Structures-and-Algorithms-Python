# By following the explanation in the video

def quickSort(array,l,r):
    if l > r:   # due to the input values p-1, p+1 below on line 10 & 11, when there is only one element,
                # l will be larger then r
        return
    else:
        p = partition(array,l,r)

    quickSort(array,l,p-1)
    quickSort(array,p+1,r)
    return array


def partition(array,l,r):
    pivotindex = r
    pivotvalue = array[r]
    while l < pivotindex:
        if array[l] > pivotvalue:
            shift(array, l, r)
            pivotindex -= 1
            l -= 1
        l += 1
    return pivotindex

def shift(array, index, pivotindex):
    temp = array[index]
    for i in range(index,pivotindex):
        array[i] = array[i+1]
    array[pivotindex] = temp


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Select first and last index as 2nd and 3rd parameters
print(quickSort(array, 0, len(array) - 1))







# Solution # Not following the way explained in the video, not intuitive to understand
# def quicksort(array, left, right):
#     ln = len(array)
#     if left < right:
#         pivot = right
#         partitionindex = partition(array, pivot, left, right)
#
#         quicksort(array, left, partitionindex - 1)
#         quicksort(array, partitionindex + 1, right)
#     return array
#
#
# def partition(array, pivot, left, right):
#     pivotvalue = array[pivot]
#     partitionindex = left
#
#     for i in range(left, right):  # scaning for element smaller than pivotvalue, and place them to the 0 then 1,2,3
#         if array[i] < pivotvalue:
#             swap(array, i, partitionindex)
#             partitionindex += 1
#
#     swap(array, right, partitionindex)
#     return partitionindex
#
#
# def swap(array, firstindex, secondindex):
#     temp = array[firstindex]
#     array[firstindex] = array[secondindex]
#     array[secondindex] = temp
#
#
# numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
#
# # Select first and last index as 2nd and 3rd parameters
# print(quicksort(numbers, 0, len(numbers) - 1))
