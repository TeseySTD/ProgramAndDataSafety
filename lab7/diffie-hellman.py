import random
import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primitive_root(p):
    if not is_prime(p):
        raise ValueError("p must be a prime number")
    
    # Factorize p-1
    factors = []
    phi = p - 1
    d = 2
    while d * d <= phi:
        if phi % d == 0:
            factors.append(d)
            phi //= d
        else:
            d += 1
    if phi > 1:
        factors.append(phi)
    
    # Find a primitive root
    for a in range(2, p):
        is_primitive_root = True
        for factor in factors:
            if pow(a, (p - 1) // factor, p) == 1:
                is_primitive_root = False
                break
        if is_primitive_root:
            return a
    
    return None

def diffie_hellman_key_exchange(p, a):
    x = random.randint(1, p - 1)  # Private key of A
    y = random.randint(1, p - 1)  # Private key of B
    
    # Calculate public keys
    X = pow(a, x, p)  # Public key of A
    Y = pow(a, y, p)  # Public key of B
    
    # Calculate the shared secret key
    k_a = pow(Y, x, p) 
    k_b = pow(X, y, p)
    
    return x, y, X, Y, k_a, k_b

def main():
    # Choose a prime number p (4-digit)
    p = 7919  # Prime number
    
    # Find a primitive root
    a = find_primitive_root(p)
    
    print(f"Modulus p: {p}")
    print(f"Primitive root a: {a}")
    
    # Perform the key exchange
    x, y, X, Y, k_a, k_b = diffie_hellman_key_exchange(p, a)
    
    print("\nKey exchange results:")
    print(f"Private key of A (x): {x}")
    print(f"Private key of B (y): {y}")
    print(f"Public key of A (X): {X}")
    print(f"Public key of B (Y): {Y}")
    print(f"Key calculated by A (k_a): {k_a}")
    print(f"Key calculated by B (k_b): {k_b}")
    
    # Check if the keys match
    if k_a == k_b:
        print("\nConclusion: Key exchange was successful!")
        print("Both parties obtained the same secret key.")
    else:
        print("\nError: Keys do not match!")

if __name__ == "__main__":
    main()
