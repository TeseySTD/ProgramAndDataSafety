import random
import math

class BBSCipher:
    def __init__(self, p, q):
        if not (self.is_prime(p) and self.is_prime(q)):
            raise ValueError("Both p and q must be prime numbers")
        
        if not (p % 4 == 3 and q % 4 == 3):
            raise ValueError("p and q must be congruent to 3 mod 4")
        
        self.n = p * q
        self.p = p
        self.q = q
        
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def generate_seed(self):
        while True:
            x = random.randint(2, self.n - 1)
            # Check coprimality and non-divisibility
            if (math.gcd(x, self.n) == 1 and 
                x % self.p != 0 and 
                x % self.q != 0):
                return x
    
    def generate_bit_stream(self, seed, length):
        bits = []
        x = seed
        
        for _ in range(length):
            # Calculate next x
            x = pow(x, 2, self.n)
            # Extract least significant bit
            bits.append(x % 2)
        
        return bits
    
    def encrypt_decrypt(self, message, seed):
        # Convert message to binary
        binary_message = ''.join(format(ord(char), '08b') for char in message)
        
        # Generate bit stream
        bit_stream = self.generate_bit_stream(seed, len(binary_message))
        
        # XOR message with bit stream
        encrypted_binary = ''.join(str(int(msg_bit) ^ bit) 
                for msg_bit, bit in zip(binary_message, bit_stream))
        
        # Convert binary back to text
        encrypted_message = ''.join(
            chr(int(encrypted_binary[i:i+8], 2)) 
            for i in range(0, len(encrypted_binary), 8)
        )
        
        return encrypted_message

def main():
    p, q = 19, 23
    
    cipher = BBSCipher(p, q)
    
    seed = cipher.generate_seed()
    
    original_message = "Hello, Cryptography!"
    print(f"Original Message: {original_message}")
    
    encrypted_message = cipher.encrypt_decrypt(original_message, seed)
    print(f"Encrypted Message: {encrypted_message}")
    
    decrypted_message = cipher.encrypt_decrypt(encrypted_message, seed)
    print(f"Decrypted Message: {decrypted_message}")
    
    print("\nVerification:")
    print(f"n (modulus): {cipher.n}")
    print(f"p: {cipher.p}")
    print(f"q: {cipher.q}")
    print(f"Seed: {seed}")
    print(f"Encryption/Decryption {'Successful' if original_message == decrypted_message else 'Failed'}")

if __name__ == "__main__":
    main()