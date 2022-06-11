from Cryptodome.Cipher import AES
from hashlib import sha3_256


def encode(x): return bytes(x, encoding='utf-8')
def decode(x): return x.decode()


def sha(x: str | bytes) -> bytes:
    if isinstance(x, str):
        return sha3_256(encode(x)).digest()
    else:
        return sha3_256(x).digest()


# 訊息加密
class AesCrypt:
    def __init__(self, key: str | bytes, for_text=False):
        '''Initialize the AES cryptor'''
        if isinstance(key, str):
            key = encode(key)
        key = sha(key)
        self.cipher = AES.new(key, AES.MODE_ECB)
        self.for_text = for_text

    @staticmethod
    def pad(text: bytes) -> bytes:
        t_len = len(text).to_bytes(16, 'big')
        text = t_len+text
        text += b' '*(16-len(text) % 16)
        return text

    def encrypt(self, text: str | bytes, hex=False) -> str | bytes:
        if self.for_text:
            text = encode(text)

        text = AesCrypt.pad(text)
        ciphertext = self.cipher.encrypt(text)

        if hex:
            return ciphertext.hex()
        else:
            return ciphertext

    def decrypt(self, ciphertext: str | bytes) -> str | bytes:
        if isinstance(ciphertext, str):
            ciphertext = bytes.fromhex(ciphertext)

        text = self.cipher.decrypt(ciphertext)
        t_len = int.from_bytes(text[:16], 'big')
        text = text[16:t_len+16]

        if self.for_text:
            return decode(text)
        else:
            return text
