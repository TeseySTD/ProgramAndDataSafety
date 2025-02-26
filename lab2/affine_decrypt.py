import sys

def mod_inverse(a, m):
    """
    Обчислює мультиплікативний обернений елемент для a за модулем m.
    Якщо оберненого елемента не існує, повертає None.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(text, a, b):
    """
    Розшифровує текст афінним алгоритмом:
      D(y) = a_inv * (y - b) mod 26
    """
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        print(f"Не існує оберненого елемента для a = {a} за модулем 26!")
        sys.exit(1)
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                offset = ord('A')
            else:
                offset = ord('a')
            y = ord(char) - offset
            decrypted_char = chr((a_inv * (y - b)) % 26 + offset)
            result += decrypted_char
        else:
            result += char
    return result

def build_substitution_table(a, b):
    """
    Будує таблицю заміни для шифрованого алфавіту.
    Для кожної літери обчислюється її відповідність після розшифрування.
    """
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return None
    table = {}
    for i in range(26):
        # Обчислюємо зашифроване значення літери
        cipher_index = (a * i + b) % 26
        cipher_char = chr(cipher_index + ord('A'))
        plain_char = chr(i + ord('A'))
        table[cipher_char] = plain_char
    return table

if __name__ == "__main__":
    filename = input("Введіть ім'я файлу з шифрограмою (наприклад, ciphertext.txt): ")
    try:
        with open(filename, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено!")
        sys.exit(1)

    if not lines:
        print("Файл порожній!")
        sys.exit(1)

    # Зчитуємо ключі з першого рядка файлу
    try:
        key_line = lines[0].strip()
        a_str, b_str = key_line.split()
        a = int(a_str)
        b = int(b_str)
    except Exception as e:
        print("Помилка зчитування ключів:", e)
        sys.exit(1)

    # Об'єднуємо решту рядків у зашифрований текст
    ciphertext = "".join(lines[1:])
    substitution_table = build_substitution_table(a, b)
    if substitution_table is None:
        sys.exit(1)

    print("\n--- Таблиця заміни (шифрована літера -> розшифрована літера) ---")
    for cipher_char in sorted(substitution_table):
        print(f"{cipher_char} -> {substitution_table[cipher_char]}")

    plaintext = affine_decrypt(ciphertext, a, b)
    print("\n--- Розшифрований текст ---")
    print(plaintext)
