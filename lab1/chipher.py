def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def encrypt_file(input_filename, output_filename, shift):
    try:
        with open(input_filename, "r", encoding="utf-8") as infile:
            text = infile.read()
    except FileNotFoundError:
        print(f"File {input_filename} not found!")
        return

    encrypted_text = caesar_cipher(text, shift)
    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write(encrypted_text)
    print(f"Encrypted file saved: {output_filename}")

def decrypt_file(input_filename, shift):
    try:
        with open(input_filename, "r", encoding="utf-8") as infile:
            encrypted_text = infile.read()
    except FileNotFoundError:
        print(f"File {input_filename} not found!")
        return

    decrypted_text = caesar_cipher(encrypted_text, -shift)
    print("Decrypted text:")
    print(decrypted_text)

def main():
    print("Choose operation:")
    print("1. Encrypt the text from the file")
    print("2. Decrypt the text from the file")
    choice = input("Choice (1/2): ")

    if choice == "1":
        input_filename = input("Enter the incoming file name (eg input.txt): ")
        output_filename = input("Enter the file name for encrypted text (eg encrypted.txt): ")
        try:
            shift = int(input("Enter shift number: "))
        except ValueError:
            print("Shift must be an integer!")
            return
        encrypt_file(input_filename, output_filename, shift)
    elif choice == "2":
        input_filename = input("Enter a file name with encrypted text (eg encrypted.txt): ")
        try:
            shift = int(input("Enter the shift value used to encrypt: "))
        except ValueError:
            print("Shift must be an inte!")
            return
        decrypt_file(input_filename, shift)
    else:
        print("Uncorrected choice!")

if __name__ == '__main__':
    main()
