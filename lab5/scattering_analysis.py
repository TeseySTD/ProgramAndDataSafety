from sdes import *

def count_changed_bits(original, modified):
    return sum(b1 != b2 for b1, b2 in zip(original, modified))

"""Analyze key diffusion"""
def analyze_key_diffusion(plaintext, base_key):
    print("Analyzing key diffusion:")
    original_cipher = sdes_encrypt(plaintext, base_key)
    print(f"Base Key: {base_key} -> Cipher: {original_cipher}")
    
    for i in range(len(base_key)):
        modified_key = list(base_key)
        modified_key[i] = '1' if base_key[i] == '0' else '0'
        modified_key = ''.join(modified_key)
        modified_cipher = sdes_encrypt(plaintext, modified_key)
        changed_bits = count_changed_bits(original_cipher, modified_cipher)
        print(f"Key bit {i+1} flipped: {modified_key} -> Cipher: {modified_cipher}, Changed Bits: {changed_bits}")

# Analyze key diffusion usage:
plaintext = "10101010"
print("---- Analysis for key '0000000000' ----")
analyze_key_diffusion(plaintext, "0000000000")

print("\n---- Analysis for key '1111111111' ----")
analyze_key_diffusion(plaintext, "1111111111")

"""Analyze plaintext diffusion"""
def analyze_plaintext_diffusion(key, base_plaintext):
    print("Analyzing plaintext diffusion:")
    original_cipher = sdes_encrypt(base_plaintext, key)
    print(f"Base Plaintext: {base_plaintext} -> Cipher: {original_cipher}")
    
    for i in range(len(base_plaintext)):
        modified_plaintext = list(base_plaintext)
        modified_plaintext[i] = '1' if base_plaintext[i] == '0' else '0'
        modified_plaintext = ''.join(modified_plaintext)
        modified_cipher = sdes_encrypt(modified_plaintext, key)
        changed_bits = count_changed_bits(original_cipher, modified_cipher)
        print(f"Plaintext bit {i+1} flipped: {modified_plaintext} -> Cipher: {modified_cipher}, Changed Bits: {changed_bits}")

# Analyze plaintext diffusion usage:
print("\n---- Analysis for plaintext '00000000' ----")
analyze_plaintext_diffusion("1010000010", "00000000")

print("\n---- Analysis for plaintext '11111111' ----")
analyze_plaintext_diffusion("1010000010", "11111111")