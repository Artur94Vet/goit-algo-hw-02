# Опис завдання
'''
Завдання 1

Додайте метод delete для видалення пар ключ-значення таблиці HashTable , яка реалізована в конспекті.
'''
# Виконання завдання

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True

        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]
        return None
    # Метод для видалення елемента за ключем
    def delete(self, key):
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]
        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return True
        return False

if __name__ == '__main__':
    # Тестуємо  хеш-таблицю:
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)
    H.insert("apple", 50)

    print("apple:", H.get("apple"))     # 50
    print("orange:", H.get("orange"))   # 20
    print("banana:", H.get("banana"))   # 30

    # Видаляємо один елемент і перевіряємо його відсутність
    H.delete("apple")
    print("apple after delete:", H.get("apple"))  # None
    print("table:", H.table)  # Перевірка структури
