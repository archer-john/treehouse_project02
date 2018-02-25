import string

from ciphers import Cipher


class Atbash(Cipher):
    """
    Atbash is a monoalphabetic substitution cipher originally used to encode
    the Hebre alphabet. The cipher is formed by taking the alphabet and mapping
    it to it's reverse, so that the first letter becomes the last letter, the
    second becomes the second last, and so on.
    """

    def __init__(self):
        self.letters = list(string.ascii_uppercase)
        self.reverse = self.letters[::-1]

    def encrypt(self, text: str):
        """
        Encrypts a message using the Atbash cipher
        :param text: string
        :return: string
        """
        result = ''
        for char in text.upper():
            try:
                result += self.reverse[
                    self.letters.index(char)
                ]
            except ValueError:
                result += char
        return result

    def decrypt(self, text):
        """
        Decrypts an encrypted message using the Atbash cipher
        :param text:
        :return:
        """
        result = ''
        for char in text.upper():
            try:
                result += self.letters[
                    self.reverse.index(char)
                ]
            except ValueError:
                result += char
        return result
