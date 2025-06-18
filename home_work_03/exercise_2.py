# Опис завдання
'''
Завдання 2

Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, 
що користувач повинен мати можливість вказати рівень рекурсії.
'''
# Виконання завдання

import turtle

def koch_snowflake(t, order, size):
    """
    Рекурсивна функція малювання сніжинки Коха.
    t — об'єкт turtle
    order — рівень рекурсії
    size — довжина сторони
    """
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_snowflake(t, order - 1, size)
        t.left(60)
        koch_snowflake(t, order - 1, size)
        t.right(120)
        koch_snowflake(t, order - 1, size)
        t.left(60)
        koch_snowflake(t, order - 1, size)

def main():
    try:
        level = int(input("Введіть рівень рекурсії (наприклад: 3): "))
    except ValueError:
        print("Некоректне значення! Буде використано рівень за замовчуванням: 3")
        level = 3

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)  # максимальна швидкість малювання

    # Початкові координати
    t.penup()
    t.goto(-300, 150)
    t.pendown()

    for i in range(3):
        koch_snowflake(t, level, 600)
        t.right(120)

    turtle.done()

if __name__ == "__main__":
    main()
