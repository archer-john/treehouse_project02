import string

from ciphers import Cipher


# noinspection PyMethodMayBeStatic
class Keyword(Cipher):
    """
    A keyword cipher is a form of monoalphabetic substitution. A keyword is used as the
    key.
    """
    def __init__(self):
        self.alphabet = list(string.ascii_uppercase)
        self.keyword = self.get_keyword()

    def get_keyword(self):
        """
        Ask user for a keyword the input is validated as a string that only contains
        letters and one word.
        :return: string
        """
        user_input = input("Please enter a keyword that only contains characters: ")
        while True:
            if user_input.isalpha() and len(user_input.split()) == 1:
                return user_input.upper()
            else:
                user_input = input("You entered non-alpha character or more than "
                                   "one word please try again: ")

    def generate_cipher_alphabet(self):
        """
        generates a cipher alphabet from the keyword
        :return: list
        """
        cipher_alphabet = list(string.ascii_uppercase)
        for index in range(len(self.keyword)):
            cipher_alphabet.remove(self.keyword[::-1][index])
            cipher_alphabet.insert(0, self.keyword[::-1][index])
        return cipher_alphabet

    def encrypt(self, text: str):
        """
        Encrypts a message using the keyword cipher.
        :param text: string
        :return: string
        """
        result = ''
        cipher_alphabet = self.generate_cipher_alphabet()
        for char in text.upper():
            try:
                result += cipher_alphabet[self.alphabet.index(char)]
            except ValueError:
                result += char
        return result

    def decrypt(self, text: str):
        """
        Decrypts am encrypted message using the keyword cipher
        :param text: string
        :return: string
        """
        result = ''
        cipher_alphabet = self.generate_cipher_alphabet()
        for char in text.upper():
            try:
                result += self.alphabet[cipher_alphabet.index(char)]
            except ValueError:
                result += char
        return result
