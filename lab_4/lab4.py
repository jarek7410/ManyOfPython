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


def speedTest(n):
    random_list = []
    for i in range(0, n):
        random_list.append(random.randint(0, n * 2))

    random_list1 = random_list.copy()
    random_list2 = random_list.copy()

    print("insert sort starts")
    start_insert = time.time()
    insertSort(random_list1)
    end_insert = time.time()
    print("insert sort time: ", end_insert - start_insert)
    print("marge sort starts")
    start_merge = time.time()
    margeSort(random_list2)
    end_merge = time.time()
    print("marge sort time: ", end_merge - start_merge)
    return [end_insert - start_insert, end_merge - start_merge]


if __name__ == "__main__":
    attempts = int(input("How many times do you want to test? \n"))
    dataSample = int(input("How many data do you want to test? \n"))
    maxTime = [0, 0]
    minTime = [10000, 10000]
    sum=[0,0]
    for i in range(attempts):
        data = speedTest(dataSample)
        if data[0] < minTime[0]:
            minTime[0] = data[0]
        if data[1] < minTime[1]:
            minTime[1] = data[1]
        if data[0] > maxTime[0]:
            maxTime[0] = data[0]
        if data[1] > maxTime[1]:
            maxTime[1] = data[1]
        sum[0]+=data[0]
        sum[1]+=data[1]
        print(f"{i+1}.")
        print(f"\tmin {minTime[0]}\tmax {maxTime[0]}\tavg {sum[0]/(i+1)}")
        print(f"\tmin {minTime[1]}\tmax {maxTime[1]}\tavg {sum[1]/(i+1)}")
