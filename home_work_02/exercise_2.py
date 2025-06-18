# Опис завдання
'''Завдання 2

Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
а також бути нечутливою до регістру та пробілів.
'''
# Виконання завдання

from collections import deque

def is_palindrome(s) -> bool:
    # Попередня обробка рядка: видаляємо пробіли, пунктуацію і переводимо в нижній регістр
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    
    deq = deque(cleaned_s)
    
    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False
    return True

# Тести

def test_true_polindorms():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("Madam In Eden, I’m Adam") is True, "Провалено: 'Madam In Eden, I’m Adam'"
    assert is_palindrome("A Santa at NASA") is True, "Провалено: 'A Santa at NASA'"

def test_not_polindroms():
    assert is_palindrome("Python") is False, "Провалено: 'Python'"
    assert is_palindrome("OpenAI") is False, "Провалено: 'OpenAI'"

def test_true_polindroms_with_punctuation():
    assert is_palindrome("Was it a car or a cat I saw?") is True, "Провалено: 'Was it a car or a cat I saw?'"
    assert is_palindrome("No 'x' in Nixon") is True, "Провалено: 'No 'x' in Nixon'"

def test_short_polidroms():
    assert is_palindrome("a") is True, "Провалено: 'a'"
    assert is_palindrome("ab") is False, "Провалено: 'ab'"
    assert is_palindrome("") is True, "Провалено: пустий рядок"

def test_mixed_upper_lower():
    assert is_palindrome("Eva, Can I Stab Bats In A Cave?") is True, "Провалено: 'Eva, Can I Stab Bats In A Cave?'"
    assert is_palindrome("Mr. Owl Ate My Metal Worm") is True, "Провалено: 'Mr. Owl Ate My Metal Worm'"

# Запуск всіх тестів вручну
if __name__ == "__main__":
    test_true_polindorms()
    test_not_polindroms()
    test_true_polindroms_with_punctuation()
    test_short_polidroms()
    test_mixed_upper_lower()
    print("Усі тести пройшли успішно!")
