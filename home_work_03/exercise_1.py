# Опис завдання
'''
Завдання 1

Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії 
та сортує в піддиректорії, назви яких базуються на розширенні файлів.

Також візьміть до уваги наступні умови:

1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та шлях до 
директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

2. Рекурсивне читання директорій:
Має бути написана функція, яка приймає шлях до директорії як аргумент.
Функція має перебирати всі елементи у директорії.
Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
Якщо елемент є файлом, він має бути доступним для копіювання.

3. Копіювання файлів:
Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
Файл з відповідним типом має бути скопійований у відповідну піддиректорію.

4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.
'''
# Виконання завдання

import argparse
import os
import shutil
from pathlib import Path

def parse_arguments():
    """
    Парсинг аргументів командного рядка.
    Обов'язковий: source_dir
    Необов'язковий: dest_dir (за замовчуванням — 'dist')
    """
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів за розширенням.')
    parser.add_argument('source_dir', help='Шлях до вихідної директорії (наприклад: "C:/Users/Asus/Desktop/Basic Algorithms and Data Structures/home_work_2/test_source")')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням: dist)')
    return parser.parse_args()

def copy_and_sort_files(src_path: Path, dest_path: Path):
    """
    Рекурсивно обходимо всі файли.
    Кожен файл сортується у відповідну папку згідно розширення.
    """
    try:
        for item in src_path.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dest_path)
            elif item.is_file():
                ext = item.suffix.lower().lstrip('.') or 'no_extension'
                target_dir = dest_path / ext
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_dir / item.name)
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    args = parse_arguments()

    source = Path(args.source_dir)
    destination = Path(args.dest_dir)

    if not source.exists() or not source.is_dir():
        print(f"Помилка: директорія {source} не існує або не є директорією.")
        return

    destination.mkdir(parents=True, exist_ok=True)
    copy_and_sort_files(source, destination)
    print("Копіювання та сортування файлів завершено.")

if __name__ == '__main__':
    main()

