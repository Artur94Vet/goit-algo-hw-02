# Опис завдання
'''
Python має дві вбудовані функції сортування: sorted і sort. Функції сортування Python використовують 
Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.

Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. 
Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних. 
Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах. 
Для заміру часу виконання алгоритмів використовуйте модуль timeit.

Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, 
і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки.
'''
# Виконання завдання

import timeit
import random

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Built-in Timsort (via sorted)
def timsort(arr):
    return sorted(arr)

# Вимірювання часу
def measure_time(sort_func, data):
    start = timeit.default_timer()
    sort_func(data[:])
    end = timeit.default_timer()
    return end - start

# Тестування на різних об'ємах
data_sizes = [100, 500, 1000, 5000]
print(f"{'Size':>6} | {'MergeSort':>10} | {'InsertionSort':>13} | {'Timsort':>8}")
print("-" * 45)

for size in data_sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    t_merge = measure_time(merge_sort, data)
    t_insert = measure_time(insertion_sort, data)
    t_timsort = measure_time(timsort, data)
    print(f"{size:>6} | {t_merge:10.6f} | {t_insert:13.6f} | {t_timsort:8.6f}")

# -----------------------
# Необов'язкове завдання
# -----------------------

import heapq

def merge_k_lists(lists):
    return list(heapq.merge(*lists))

# Приклад
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged = merge_k_lists(lists)
print("\nВідсортований список:", merged)
