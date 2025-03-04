def permute(bits, permutation):
    return ''.join(bits[i - 1] for i in permutation)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_keys(key):
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8  = [6, 3, 7, 4, 8, 5, 10, 9]
    
    key_p10 = permute(key, p10)
    left = key_p10[:5]
    right = key_p10[5:]
    
    left1 = left_shift(left, 1)
    right1 = left_shift(right, 1)
    k1 = permute(left1 + right1, p8)
    
    left2 = left_shift(left1, 2)
    right2 = left_shift(right1, 2)
    k2 = permute(left2 + right2, p8)
    
    return k1, k2

def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    value = sbox[row][col]
    return format(value, '02b')

def f_function(bits, subkey):
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    expanded_bits = permute(bits, ep)
    
    xor_result = format(int(expanded_bits, 2) ^ int(subkey, 2), '08b')
    left, right = xor_result[:4], xor_result[4:]
    
    s0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]
    s1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
    ]
    s0_out = sbox_lookup(left, s0)
    s1_out = sbox_lookup(right, s1)
    
    combined = s0_out + s1_out
    p4 = [2, 4, 3, 1]
    return permute(combined, p4)

def sdes_encrypt(plaintext, key):
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    
    k1, k2 = generate_keys(key)
    
    temp = permute(plaintext, ip)
    left, right = temp[:4], temp[4:]
    
    temp_f = f_function(right, k1)
    left = format(int(left, 2) ^ int(temp_f, 2), '04b')
    
    left, right = right, left
    
    temp_f = f_function(right, k2)
    left = format(int(left, 2) ^ int(temp_f, 2), '04b')
    
    preoutput = left + right
    ciphertext = permute(preoutput, ip_inv)
    return ciphertext

def sdes_decrypt(ciphertext, key):
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    
    k1, k2 = generate_keys(key)
    
    temp = permute(ciphertext, ip)
    left, right = temp[:4], temp[4:]
    
    temp_f = f_function(right, k2)
    left = format(int(left, 2) ^ int(temp_f, 2), '04b')
    
    left, right = right, left
    
    temp_f = f_function(right, k1)
    left = format(int(left, 2) ^ int(temp_f, 2), '04b')
    
    preoutput = left + right
    plaintext = permute(preoutput, ip_inv)
    return plaintext

def test_sdes():
    plaintext = "10101010"          
    key = "1010000010"              
    encrypted = sdes_encrypt(plaintext, key)
    decrypted = sdes_decrypt(encrypted, key)
    
    print("Test 1:")
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
    print("Result:", plaintext == decrypted, "\n")

test_sdes()

def test_multiple():
    texts = ["11001100", "01110010"]
    keys = ["0010011010", "1110001110"]

    for i, (text, key) in enumerate(zip(texts, keys), start=2):
        encrypted = sdes_encrypt(text, key)
        decrypted = sdes_decrypt(encrypted, key)
        print(f"Test {i}:")
        print("Plaintext:", text)
        print("Key:", key)
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypted)
        print("Result:", text == decrypted, "\n")

test_multiple()
