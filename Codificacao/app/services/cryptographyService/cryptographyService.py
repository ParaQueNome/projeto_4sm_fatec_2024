from app.services.cryptographyService.cryptography import Cryptography

class CryptographyService:

    def __init__(self, crypto : Cryptography) -> None:
        self.crypto = crypto

    def encryptPassword(self, password):
        print(password)
        hashPassword = self.crypto.hashPassword(password)
        key = self.crypto.generateKey()
        encryptedPassword = self.crypto.encryptText(hashPassword, key)
        return encryptedPassword, key