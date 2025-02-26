import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def affine_encrypt(text, a, b):
    """
      E(x) = (a * x + b) mod 26
    """
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                offset = ord('A')
            else:
                offset = ord('a')
            x = ord(char) - offset
            encrypted_char = chr((a * x + b) % 26 + offset)
            result += encrypted_char
        else:
            result += char
    return result

def main():
    input_filename = input("Enter the name of the input file with plaintext (e.g., plaintext.txt): ")
    output_filename = input("Enter the name of the file to save the ciphertext (e.g., ciphertext.txt): ")

    try:
        with open(input_filename, "r", encoding="utf-8") as infile:
            plaintext = infile.read()
    except FileNotFoundError:
        print(f"File {input_filename} not found!")
        sys.exit(1)

    try:
        a = int(input("Enter the value of coefficient a (must be coprime with 26): "))
        b = int(input("Enter the value of shift b: "))
    except ValueError:
        print("Error: coefficients must be integers!")
        sys.exit(1)

    if gcd(a, 26) != 1:
        print(f"Error: {a} is not coprime with 26. Please choose another value.")
        sys.exit(1)

    ciphertext = affine_encrypt(plaintext, a, b)
    try:
        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.write(f"{a} {b}\n")
            outfile.write(ciphertext)
        print(f"Encrypted text saved in file {output_filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == '__main__':
    main()

