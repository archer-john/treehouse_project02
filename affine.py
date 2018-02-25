import string

from ciphers import Cipher


# noinspection PyMethodMayBeStatic
class Affine(Cipher):
    """
    Affine cipher is a type of monoalphabetic substitution cipher, wherein each letter
    in an alphabet is mapped to its numeric equivalent.
    Encryption Function: E(x) = (ax + b) % m
    Decryption Function D(x) = a^-1(x - b) % m
        x = character
        a = alpha key (must be coprime with m)
        b = positive int
        m = length of alphabet
    """

    def __init__(self):
        self.letters = list(string.ascii_uppercase)
        self.m = len(self.letters)
        self.alpha = self.get_alpha()
        self.beta = self.get_beta()
        self.alpha_inverse = self.alpha_multiplicative_inverse()

    def get_alpha(self):
        """
        Request user to enter alpha key. The input is validated as an int and that it is
        a coprime of m (self.m)
        :return: int
        """
        m_coprimes = [num for num in range(self.m) if self.coprime(num, self.m)]
        user_input = input(f"Please pick a number from the list to be used as the first\n"
                           f"key: {m_coprimes} ")
        while True:
            if user_input.isdigit():
                if int(user_input) in m_coprimes:
                    return int(user_input)
                else:
                    print(f"You must use a number from the list as your first key. "
                          f"list: {m_coprimes}")
            else:
                print("The key can not contain letters")
            user_input = input("Please pick again: ")

    def get_beta(self):
        """
        Request user to enter beta key. The input is validated as a non-negative int
        :return: int
        """
        user_input = input("Please enter a non-negative integer as your second key: ")
        while True:
            if user_input.isdigit() and int(user_input) > 0:
                return int(user_input)
            else:
                user_input = input("Incorrect value entered. Please pick again: ")

    def alpha_multiplicative_inverse(self):
        """
        Calculates the modular multiplicative inverse of alpha
        :return: int
        """
        inverse = 1
        for i in range(1, self.m):
            if (self.alpha * i) % self.m == 1:
                inverse = i
        return inverse

    def encrypt(self, text: str):
        """
        Iterates over a string applying the Affine Encryption function
        :param text: user entered string
        :return: encrypted string
        """
        result = ''
        for char in text.upper():
            try:
                x = self.letters.index(char)
                cipher_index = (self.alpha * x + self.beta) % self.m
                result += self.letters[cipher_index]
            except ValueError:
                result += char
        return result

    def decrypt(self, text: str):
        """
        Iterates over an encrypted string applying the Affine Decryption function.
        :param text: user entered string
        :return: plain text string
        """
        result = ""
        for char in text.upper():
            try:
                x = self.letters.index(char)
                plain_index = self.alpha_inverse * (x - self.beta) % self.m
                result += self.letters[plain_index]
            except ValueError:
                result += char
        return result
