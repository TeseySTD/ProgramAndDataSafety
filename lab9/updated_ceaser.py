import random

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def generate_substitution_table():
    alphabet = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    
    substitution_table = {original: replacement 
                          for original, replacement in zip(alphabet, shuffled_alphabet)}
    
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
        print(f"File {input_filename} not found!")
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
        outfile.write(f"Ceasar shift: {shift}\n\n")
        outfile.write("Table of replacements:\n")
        for original, replacement in substitution_table.items():
            outfile.write(f"{original}: {replacement}\n")

    print(f"Encrypted file saved: {output_filename}")



def main():
    print("Choose operation:")
    print("1. Encrypt text from file")
    print("2. Decrypt text from file")
    choice = input("Choice (1/2): ")

    if choice == "1":
        input_filename = input("Enter the name of the input file (e.g. input.txt): ")
        output_filename = input("Enter the name of the file for the encrypted text (e.g. encrypted.txt): ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Shift must be an integer!")
            return
        encrypt_file(input_filename, output_filename, shift)

    elif choice == "2":
        input_filename = input("Enter the name of the file with the encrypted text (e.g. encrypted.txt): ")
        try:
            shift = int(input("Enter the shift value used for encryption: "))
            
            # Read the substitution table
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
            print(f"Error reading the substitution table: {e}")
            return

        decrypt_file(input_filename, shift, substitution_table)

    else:
        print("Incorrect choice!")

if __name__ == '__main__':
    main()