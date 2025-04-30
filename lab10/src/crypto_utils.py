from wincrypto import CryptCreateHash, CryptHashData, CryptDeriveKey, CryptEncrypt, CryptDecrypt
from wincrypto.constants import CALG_SHA1, CALG_RC4

class RC4Cipher:
    def __init__(self, password: str):
        self.hasher = CryptCreateHash(CALG_SHA1)
        CryptHashData(self.hasher, password.encode('utf-8'))
        self.key = CryptDeriveKey(self.hasher, CALG_RC4)

    def encrypt(self, plaintext: str) -> bytes:
        return CryptEncrypt(self.key, plaintext.encode('utf-8'))

    def decrypt(self, ciphertext: bytes) -> str:
        return CryptDecrypt(self.key, ciphertext).decode('utf-8')

