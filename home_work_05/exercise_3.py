# Опис завдання
'''
Завдання 3

Порівняйте ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа 
на основі двох текстових файлів (стаття 1, стаття 2). Використовуючи timeit, треба виміряти час виконання 
кожного алгоритму для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого 
(вибір підрядків за вашим бажанням). На основі отриманих даних визначте найшвидший алгоритм для кожного тексту окремо та в цілому.
'''
# Виконання завдання


import timeit
import chardet

# === Алгоритми пошуку ===

def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power = pow(base, n - i - 1, modulus)
        hash_value = (hash_value + ord(char) * power) % modulus
    return hash_value

def rabin_karp_search(text, pattern):
    m, n = len(pattern), len(text)
    base, modulus = 256, 101
    pattern_hash = polynomial_hash(pattern, base, modulus)
    current_hash = polynomial_hash(text[:m], base, modulus)
    h_multiplier = pow(base, m - 1, modulus)

    for i in range(n - m + 1):
        if pattern_hash == current_hash and text[i:i+m] == pattern:
            return i
        if i < n - m:
            current_hash = (current_hash - ord(text[i]) * h_multiplier) % modulus
            current_hash = (current_hash * base + ord(text[i + m])) % modulus
            current_hash = (current_hash + modulus) % modulus
    return -1

def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1

# === Зчитування тексту з визначенням кодування ===

def read_file_detect_encoding(path):
    with open(path, 'rb') as f:
        raw = f.read()
    encoding = chardet.detect(raw)['encoding']
    return raw.decode(encoding)

text1 = read_file_detect_encoding('home_work_05/art_1.txt')
text2 = read_file_detect_encoding('home_work_05/art_2.txt')

# === Підрядки для пошуку ===

patterns = {
    "existing": "алгоритм",
    "non_existing": "реалізаціяметодів"
}

# === Алгоритми ===

algorithms = {
    "Rabin-Karp": rabin_karp_search,
    "Boyer-Moore": boyer_moore_search,
    "KMP": kmp_search
}

# === Вимірювання часу ===

def measure_time(func, text, pattern, repeats=10):
    return timeit.timeit(lambda: func(text, pattern), number=repeats)

# === Основна логіка ===

def main():
    results = []
    for text_id, text in [("Text 1", text1), ("Text 2", text2)]:
        for label, pattern in patterns.items():
            for alg_name, alg_func in algorithms.items():
                exec_time = measure_time(alg_func, text, pattern)
                results.append((text_id, label, alg_name, exec_time))

    print(f"{'Text':<10} {'Pattern':<15} {'Algorithm':<15} {'Time (s)':<10}")
    print("-" * 60)
    for r in results:
        print(f"{r[0]:<10} {r[1]:<15} {r[2]:<15} {r[3]:<10.6f}")

if __name__ == "__main__":
    main()
