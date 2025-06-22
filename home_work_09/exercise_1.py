# Опис завдання
'''
У конспекті ми розглянули приклад про розбиття суми на монети. Маємо набір монет [50, 25, 10, 5, 2, 1]. 
Уявіть, що ви розробляєте систему для касового апарату, яка повинна визначити оптимальний спосіб видачі решти покупцеві.

Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:

Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму, яку потрібно видати покупцеві, 
і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. Наприклад, 
для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, тобто спочатку вибирати 
найбільш доступні номінали монет.
Функція динамічного програмування find_min_coins. Ця функція також повинна приймати суму для видачі решти, але 
використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для формування 
цієї суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми 
найефективнішим способом. Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}
Порівняйте ефективність жадібного алгоритму та алгоритму динамічного програмування, базуючись на часі їх 
виконання або О великому та звертаючи увагу на їхню продуктивність при великих сумах. Висвітліть, як вони 
справляються з великими сумами та чому один алгоритм може бути більш ефективним за інший у певних ситуаціях. 
Свої висновки додайте у файл readme.md домашнього завдання.
'''
# Виконання завдання

import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    min_coins = [0] + [float('inf')] * amount
    used_coins = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                used_coins[i] = coin

    result = {}
    current = amount
    while current > 0:
        coin = used_coins[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin
    return result

if __name__ == "__main__":
    amount = 113

    start = time.perf_counter()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.perf_counter() - start

    start = time.perf_counter()
    dp_result = find_min_coins(amount)
    dp_time = time.perf_counter() - start

    print(f"Greedy result: {greedy_result}")
    print(f"Time taken (Greedy): {greedy_time:.8f} seconds")

    print(f"DP result: {dp_result}")
    print(f"Time taken (DP): {dp_time:.8f} seconds")
