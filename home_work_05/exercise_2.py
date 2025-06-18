# Опис завдання
'''
Завдання 2

Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами. 
Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. 
Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.
'''
# Виконання завдання

def binary_search_with_upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            # Якщо точно знайдено
            return (iterations, arr[mid])

    # Якщо точно не знайдено — верхня межа це перший елемент ≥ target
    if low < len(arr):
        upper_bound = arr[low]
    return (iterations, upper_bound)


if __name__ == '__main__':
    # Вхідний масив має бути відсортований
    arr = [1.1, 1.3, 2.5, 3.8, 4.6]
    
    print("target=3.5  =>", binary_search_with_upper_bound(arr, 3.5))   # (ітерації, 3.8)
    print("target=4    =>", binary_search_with_upper_bound(arr, 4))     # (ітерації, 4.6)
    print("target=6.0  =>", binary_search_with_upper_bound(arr, 6.0))   # (ітерації, None)
    print("target=2.5  =>", binary_search_with_upper_bound(arr, 2.5))   # (ітерації, 2.5)
    print("target=0    =>", binary_search_with_upper_bound(arr, 0))     # (ітерації, 1.1)
