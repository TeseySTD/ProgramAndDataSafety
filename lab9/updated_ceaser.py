import random

def caesar_cipher(text, shift):
    result = ""
    ukrainian_alphabet = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    for char in text.upper():
        if char in ukrainian_alphabet:
            index = ukrainian_alphabet.index(char)
            new_index = (index + shift) % len(ukrainian_alphabet)
            result += ukrainian_alphabet[new_index]
        else:
            result += char
    return result

def generate_substitution_table():
    ukrainian_alphabet = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    
    shuffled_alphabet = list(ukrainian_alphabet)
    random.shuffle(shuffled_alphabet)
    
    substitution_table = {original: replacement 
                          for original, replacement in zip(ukrainian_alphabet, shuffled_alphabet)}
    
    return substitution_table

def simple_substitution_cipher(text, substitution_table):
    result = ""
    for char in text.upper():
        if char in substitution_table:
            result += substitution_table[char]
        else:
            result += char
    return result

def encrypt_file(input_filename, output_filename, shift):
    try:
        with open(input_filename, "r", encoding="utf-8") as infile:
            text = infile.read().upper()
    except FileNotFoundError:
        print(f"Файл {input_filename} не знайдено!")
        return

    # Перший етап - шифрування Цезаря
    caesar_encrypted = caesar_cipher(text, shift)
    
    # Генерація таблиці простої заміни
    substitution_table = generate_substitution_table()
    
    # Другий етап - проста заміна
    final_encrypted = simple_substitution_cipher(caesar_encrypted, substitution_table)

    # Збереження зашифрованого тексту, зсуву і таблиці заміни
    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write(final_encrypted + "\n\n")
        outfile.write(f"Зсув Цезаря: {shift}\n\n")
        outfile.write("Таблиця замін:\n")
        for original, replacement in substitution_table.items():
            outfile.write(f"{original}: {replacement}\n")

    print(f"Зашифрований файл збережено: {output_filename}")

def decrypt_file(input_filename, shift, substitution_table):
    try:
        with open(input_filename, "r", encoding="utf-8") as infile:
            # Припускаємо, що перші рядки - це зашифрований текст
            lines = infile.readlines()
            encrypted_text = lines[0].strip()
    except FileNotFoundError:
        print(f"Файл {input_filename} не знайдено!")
        return

    # Створення таблиці зворотної заміни
    reverse_substitution_table = {v: k for k, v in substitution_table.items()}
    
    # Перший крок - проста зворотна заміна
    caesar_text = simple_substitution_cipher(encrypted_text, reverse_substitution_table)
    
    # Другий крок - декодування Цезаря
    decrypted_text = caesar_cipher(caesar_text, -shift)

    print("Розшифрований текст:")
    print(decrypted_text)

def main():
    print("Виберіть операцію:")
    print("1. Зашифрувати текст з файлу")
    print("2. Розшифрувати текст з файлу")
    choice = input("Вибір (1/2): ")

    if choice == "1":
        input_filename = input("Введіть назву вхідного файлу (наприклад, input.txt): ")
        output_filename = input("Введіть назву файлу для зашифрованого тексту (наприклад, encrypted.txt): ")
        try:
            shift = int(input("Введіть значення зсуву: "))
        except ValueError:
            print("Зсув має бути цілим числом!")
            return
        encrypt_file(input_filename, output_filename, shift)

    elif choice == "2":
        input_filename = input("Введіть назву файлу з зашифрованим текстом (наприклад, encrypted.txt): ")
        try:
            shift = int(input("Введіть значення зсуву, використане при шифруванні: "))
            
            # Читання таблиці заміни
            substitution_table = {}
            with open(input_filename, "r", encoding="utf-8") as infile:
                infile.readline()
                infile.readline()  
                infile.readline()  
                infile.readline() 
                infile.readline()  
                
                for line in infile:
                    if ':' in line:
                        original, replacement = line.strip().split(': ')
                        substitution_table[original] = replacement
        except Exception as e:
            print(f"Помилка читання таблиці заміни: {e}")
            return

        decrypt_file(input_filename, shift, substitution_table)

    else:
        print("Невірний вибір!")

if __name__ == '__main__':
    main()