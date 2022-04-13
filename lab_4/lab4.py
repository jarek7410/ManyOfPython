import math
import time
import random


def insertSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def margeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        margeSort(left)
        margeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

random_list = []
n=int(input("Enter the number of elements: "))
for i in range(0, n):
    random_list.append(random.randint(0, n*2))
print("The random list is: ", random_list)

random_list1=random_list.copy()
random_list2=random_list.copy()

print("insert sort starts")
startInser=time.time()
insertSort(random_list1)
endInser=time.time()
print("marge sort starts")
startmerge=time.time()
margeSort(random_list2)
endmerge=time.time()
print("insert sort time: ", endInser-startInser)
print("marge sort time: ", endmerge-startmerge)
print("insert sort: \t", random_list1)
print("marge sort: \t", random_list2)

