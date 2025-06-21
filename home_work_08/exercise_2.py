# Опис завдання
'''

Необов'язкове завдання

Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. 
Тепер при виконанні завдання ви повинні використати мінімальну купу для ефективного злиття кількох відсортованих списків в один відсортований список. 
Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків та повертає відсортований список.

Приклад очікуваного результату:

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

Виведення:

Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
'''
# Виконання завдання

import heapq

def merge_k_lists(lists):
    min_heap = []
    result = []

    # Додаємо перші елементи з кожного списку до купи
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента в списку)

    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)

        # Якщо у цьому списку ще є елементи — додаємо наступний
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)

    return result

if __name__ == '__main__':
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)