def mod_pow(base, power, mod):
    result = 1
    base = base % mod
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % mod
        power = power >> 1
        base = (base * base) % mod
    return result

def calculate_hash(message):
    char_table = {
        'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ж': 6, 'З': 7,
        'И': 8, 'Й': 9, 'К': 10, 'Л': 11, 'М': 12, 'Н': 13, 'О': 14, 'П': 15,
        'Р': 16, 'С': 17, 'Т': 18, 'У': 19, 'Ф': 20, 'Х': 21, 'Ц': 22, 'Ч': 23,
        'Ш': 24, 'Щ': 25, 'Ъ': 26, 'Ы': 27, 'Ь': 28, 'Э': 29, 'Ю': 30, 'Я': 31,
        ' ': 32
    }
    
    total = 0
    for char in message.upper():
        if char in char_table:
            total += char_table[char]
    
    return total % 33

def sign_message(message, e, n):
    hash_value = calculate_hash(message)
    signature = mod_pow(hash_value, e, n)
    return signature

def encrypt_message(message, e, n):
    char_table = {
        'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ж': 6, 'З': 7,
        'И': 8, 'Й': 9, 'К': 10, 'Л': 11, 'М': 12, 'Н': 13, 'О': 14, 'П': 15,
        'Р': 16, 'С': 17, 'Т': 18, 'У': 19, 'Ф': 20, 'Х': 21, 'Ц': 22, 'Ч': 23,
        'Ш': 24, 'Щ': 25, 'Ъ': 26, 'Ы': 27, 'Ь': 28, 'Э': 29, 'Ю': 30, 'Я': 31,
        ' ': 32
    }
    
    encrypted = []
    for char in message.upper():
        if char in char_table:
            value = char_table[char]
            encrypted_value = mod_pow(value, e, n)
            encrypted.append(str(encrypted_value))
    
    return ' '.join(encrypted)

def main():
    p, q = 3, 11
    n = p * q
    e = 7
    
    try:
        with open("message.txt", "r", encoding="utf-8") as file:
            message = file.read().strip()
    except FileNotFoundError:
        print("Файл message.txt не знайдено. Створюю тестове повідомлення.")
        message = "Лол кек чебурек"
        with open("message.txt", "w", encoding="utf-8") as file:
            file.write(message)
    
    encrypted_message = encrypt_message(message, e, n)
    
    hash_value = calculate_hash(message)
    digital_signature = sign_message(message, e, n)
    
    with open("encrypted.txt", "w", encoding="utf-8") as file:
        file.write(encrypted_message + "\n")
        file.write(str(digital_signature))
    
    print(f"Оригінальне повідомлення: {message}")
    print(f"Зашифроване повідомлення: {encrypted_message}")
    print(f"Хеш-функція повідомлення: {hash_value}")
    print(f"Цифровий підпис: {digital_signature}")
    print("Зашифроване повідомлення та цифровий підпис збережено у файлі encrypted.txt")

if __name__ == "__main__":
    main()