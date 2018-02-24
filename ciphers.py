from math import gcd


class Cipher:
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    def coprime(self, a: int, b: int):
        """
        Returns True if 'a' is a coprime of 'b'
        :param a: int
        :param b: int
        :return: Bool
        """
        return gcd(a, b) == 1
