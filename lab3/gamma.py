substitution_table = {
    'А': 0,  'Б': 1,  'В': 2,  'Г': 3,  'Д': 4,  'Е': 5,  'Ж': 6,  'З': 7,
    'И': 8,  'Й': 9,  'К': 10, 'Л': 11, 'М': 12, 'Н': 13, 'О': 14, 'П': 15,
    'Р': 16, 'С': 17, 'Т': 18, 'У': 19, 'Ф': 20, 'Х': 21, 'Ц': 22, 'Ч': 23,
    'Ш': 24, 'Щ': 25, 'Ъ': 26, 'Ы': 27, 'Ь': 28, 'Э': 29, 'Ю': 30, 'Я': 31, ' ': 32
}
len_of_table = len(substitution_table)
inv_substitution = {v: k for k, v in substitution_table.items()}

def read_text_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip()

def write_text_to_file(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def simple_substitution(text):
    codes = []
    for ch in text.upper():
        if ch in substitution_table:
            codes.append(substitution_table[ch])
    return codes

def inverse_substitution(codes):
    chars = []
    for code in codes:
        if code in inv_substitution:
            chars.append(inv_substitution[code])
    return "".join(chars)

def generate_gamma(key, length):
    Y = list(key) 
    while len(Y) < length + 1:
        next_Y = (Y[-1] + Y[-3]) % len_of_table
        Y.append(next_Y)
    gamma = []
    for t in range(length):
        gamma_val = (Y[t] + Y[t+1]) % len_of_table
        gamma.append(gamma_val)
    return gamma

def encrypt(plaintext_codes, gamma):
    ciphertext_codes = []
    for pt, g in zip(plaintext_codes, gamma):
        s = (pt + g) % len_of_table
        ciphertext_codes.append(s)
    return ciphertext_codes

def decrypt(ciphertext_codes, gamma):
    plaintext_codes = []
    for ct, g in zip(ciphertext_codes, gamma):
        t = (ct + (len_of_table - g)) % len_of_table
        plaintext_codes.append(t)
    return plaintext_codes

def codes_to_text(codes):
    text = ""
    for code in codes:
        text += inv_substitution.get(code, "?")
    return text

def main():
    mode = input("Enter the mode (E - encryption, D - decryption): ").strip().upper()
    
    if mode == "E":
        plaintext = read_text_from_file("plaintext.txt")
        print("Plaintext:", plaintext)
        
        plaintext_codes = simple_substitution(plaintext)
        
        key_input = input(F"Enter the session key (three numbers from 0 to {len_of_table - 1}, separated by space): ")
        key = list(map(int, key_input.strip().split()))
        if len(key) != 3:
            print("Error: enter exactly three numbers!")
            return
        
        gamma = generate_gamma(key, len(plaintext_codes))
        
        ciphertext_codes = encrypt(plaintext_codes, gamma)
        ciphertext_str = " ".join(map(str, ciphertext_codes))
        write_text_to_file("ciphertext.txt", ciphertext_str)
        print("Ciphertext saved to file 'ciphertext.txt'")
    
    elif mode == "D":
        ciphertext_str = read_text_from_file("ciphertext.txt")
        ciphertext_codes = list(map(int, ciphertext_str.strip().split()))
        
        key_input = input(F"Enter the session key (three numbers from 0 to {len_of_table - 1}, separated by space): ")
        key = list(map(int, key_input.strip().split()))
        if len(key) != 3:
            print("Error: enter exactly three numbers!")
            return
        
        gamma = generate_gamma(key, len(ciphertext_codes))
        plaintext_codes = decrypt(ciphertext_codes, gamma)
        decrypted_text = codes_to_text(plaintext_codes)
        write_text_to_file("decrypted.txt", decrypted_text)
        print("Decrypted text:", decrypted_text)
        print("Decrypted text saved to file 'decrypted.txt'")
    else:
        print("Invalid mode. Choose E or D.")

if __name__ == "__main__":
    main()