from itertools import permutations
from sdes import sdes_encrypt

def compare_sbox_effect(plaintext, key):
    original_encrypted = sdes_encrypt(plaintext, key)

    s0_original = [
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

    results = []

    for i in range(len(s0_original)):
        for new_row in permutations(s0_original[i]):
            modified_s0 = [row[:] for row in s0_original]
            modified_s0[i] = list(new_row) 

            modified_encrypted = sdes_encrypt(plaintext, key, modified_s0, s1)

            diff = sum(1 for a, b in zip(original_encrypted, modified_encrypted) if a != b)
            results.append((i, new_row, modified_encrypted, diff))

            print(f"Row {i}: original: {s0_original[i]}, new row: {new_row} -> {modified_encrypted} ({diff} bits changed)")

    max_change = max(results, key=lambda x: x[3])
    min_change = min(results, key=lambda x: x[3])

    print(f"Original Encrypted: {original_encrypted}\n")
    
    print("Most Impactful Change:")
    print(f"Modified row index: {max_change[0]}")
    print(f"New row: {max_change[1]}")
    print(f"Modified Encrypted: {max_change[2]}")
    print(f"Bits changed: {max_change[3]}\n")

    print("Least Impactful Change:")
    print(f"Modified row index: {min_change[0]}")
    print(f"New row: {min_change[1]}")
    print(f"Modified Encrypted: {min_change[2]}")
    print(f"Bits changed: {min_change[3]}")

plaintext = "10101010"
key = "1010000010"
compare_sbox_effect(plaintext, key)
