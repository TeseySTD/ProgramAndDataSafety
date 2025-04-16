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

def decrypt_message(encrypted_message, d, n):
    number_table = {
        0: 'А', 1: 'Б', 2: 'В', 3: 'Г', 4: 'Д', 5: 'Е', 6: 'Ж', 7: 'З',
        8: 'И', 9: 'Й', 10: 'К', 11: 'Л', 12: 'М', 13: 'Н', 14: 'О', 15: 'П',
        16: 'Р', 17: 'С', 18: 'Т', 19: 'У', 20: 'Ф', 21: 'Х', 22: 'Ц', 23: 'Ч',
        24: 'Ш', 25: 'Щ', 26: 'Ъ', 27: 'Ы', 28: 'Ь', 29: 'Э', 30: 'Ю', 31: 'Я',
        32: ' '
    }
    
    encrypted_values = encrypted_message.split()
    
    decrypted = ""
    for value in encrypted_values:
        decrypted_value = mod_pow(int(value), d, n)
        if decrypted_value in number_table:
            decrypted += number_table[decrypted_value]
        else:
            decrypted += '?'  # Символ, якого немає в таблиці
    
    return decrypted

def verify_signature(message, signature, d, n):
    decrypted_signature = mod_pow(signature, d, n)
    
    hash_value = calculate_hash(message)
    
    return decrypted_signature == hash_value

def main():
    # За завданням: p=3, q=11, n=3x11=33, E=7, D=3
    n = 33
    d = 3
    
    try:
        with open("encrypted.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                encrypted_message = lines[0].strip()
                digital_signature = int(lines[1].strip())
            else:
                print("Помилка: файл encrypted.txt має неправильний формат")
                return
    except FileNotFoundError:
        print("Файл encrypted.txt не знайдено.")
        return
    
    decrypted_message = decrypt_message(encrypted_message, d, n)
    
    hash_value = calculate_hash(decrypted_message)
    
    decrypted_signature = mod_pow(digital_signature, d, n)
    
    is_valid = verify_signature(decrypted_message, digital_signature, d, n)
    
    print(f"Зашифроване повідомлення: {encrypted_message}")
    print(f"Розшифроване повідомлення: {decrypted_message}")
    print(f"Обчислена хеш-функція повідомлення: {hash_value}")
    print(f"Розшифрований цифровий підпис: {decrypted_signature}")
    
    if is_valid:
        print("Цифровий підпис ВІРНИЙ. Повідомлення не було модифіковано.")
    else:
        print("Цифровий підпис НЕВІРНИЙ! Повідомлення могло бути модифіковано.")

if __name__ == "__main__":
    main()