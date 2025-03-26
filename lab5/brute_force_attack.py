import time
from sdes import *
def brute_force_attack(plaintext, target_cipher):
    start_time = time.time()
    total_keys = 0
    for key in range(1024):
        key_str = format(key, '010b')
        total_keys += 1
        if sdes_encrypt(plaintext, key_str) == target_cipher:
            elapsed = time.time() - start_time
            print(f"Key found: {key_str}")
            print(f"Total keys tested: {total_keys}")
            print(f"Time elapsed: {elapsed:.4f} seconds")
            return key_str, total_keys, elapsed
    print("Key not found")
    return None

# Example usage:
plaintext = "10101010"
key = "1010000010"
target_cipher = sdes_encrypt(plaintext, key)
print("\n---- Brute force attack ----")
brute_force_attack(plaintext, target_cipher)
