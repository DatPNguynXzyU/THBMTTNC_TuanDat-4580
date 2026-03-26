import rsa

class RSACipher:
    def __init__(self):
        # Update these two lines to include the folder path
        self.public_key_file = 'cipher/rsa/keys/public_key.pem'
        self.private_key_file = 'cipher/rsa/keys/private_key.pem'

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)
        with open(self.public_key_file, 'wb') as p_file:
            p_file.write(public_key.save_pkcs1('PEM'))
        with open(self.private_key_file, 'wb') as p_file:
            p_file.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        with open(self.public_key_file, 'rb') as p_file:
            public_key = rsa.PublicKey.load_pkcs1(p_file.read())
        with open(self.private_key_file, 'rb') as p_file:
            private_key = rsa.PrivateKey.load_pkcs1(p_file.read())
        return private_key, public_key 

    def encrypt(self, message, key):
        # Return raw bytes directly
        return rsa.encrypt(message.encode('utf-8'), key)

    def decrypt(self, ciphertext, key):
        # Expect raw bytes and decode the result
        decrypted_data = rsa.decrypt(ciphertext, key)
        return decrypted_data.decode('utf-8')
        
    def sign(self, message, key):
        # Return raw bytes directly
        return rsa.sign(message.encode('utf-8'), key, 'SHA-256')
        
    def verify(self, message, signature, key):
        # Expect raw bytes
        try:
            rsa.verify(message.encode('utf-8'), signature, key)
            return True
        except rsa.VerificationError:
            return False