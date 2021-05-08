import base64
import hashlib
import time
import random
from ezreal import config
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256


def get_random_string(length=12, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    _random = random.SystemRandom()
    _random.seed(
        hashlib.sha256(
            ('%s%s%s' % (random.getstate(), time.time(), config.SECRET_KEY)).encode()
        ).digest()
    )

    return ''.join(random.choice(allowed_chars) for i in range(length))


class PBKDF2PasswordHasher:
    algorithm = "pbkdf2_sha256"
    iterations = 150000
    digest = hashlib.sha256

    def encode(self, password, salt, iterations=None):
        assert password is not None
        assert salt and '$' not in salt
        iterations = iterations or self.iterations
        _hash = PBKDF2(password, salt, dkLen=32, count=iterations, hmac_hash_module=SHA256)
        _hash = base64.b64encode(_hash).decode('ascii').strip()
        return "%s$%d$%s$%s" % (self.algorithm, iterations, salt, _hash)

    def verify(self, password, encoded):
        if not encoded:
            return False
        algorithm, iterations, salt, _hash = encoded.split('$', 3)
        assert algorithm == self.algorithm
        encoded_2 = self.encode(password, salt, int(iterations))
        return encoded == encoded_2

    def salt(self):
        return get_random_string()


pbkdf2_password_hasher = PBKDF2PasswordHasher()
