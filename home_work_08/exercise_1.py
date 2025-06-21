# Опис завдання
'''
Опис домашнього завдання



Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.

Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, 
у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, 
а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

'''
# Виконання завдання

import heapq

def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths:
        return 0

    heapq.heapify(cable_lengths)
    total_cost = 0

    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        cost = first + second
        total_cost += cost
        heapq.heappush(cable_lengths, cost)

    return total_cost

if __name__ == '__main__':
    cable_lengths = [1, 1, 9, 2, 1, 2]
    print("Вихідний список:", sorted(cable_lengths))
    print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))