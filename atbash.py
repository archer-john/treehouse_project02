import string

from ciphers import Cipher


class Atbash(Cipher):
    """
    Atbash is a monoalphabetic substitution cipher originally used to encode the Hebre
    alphabet. The cipher is formed by taking the alphabet and mapping it to it's reverse,
    so that the first letter becomes the last letter, the second becomes the second last,
    and so on.
    """

    def __init__(self):
        self.letters = [s for s in string.ascii_uppercase]
        self.reverse = self.letters[::-1]

    def encrypt(self, text: str):
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
        result = ''
        for char in text.upper():
            try:
                result += self.letters[
                    self.reverse.index(char)
                ]
            except ValueError:
                result += char
        return result


if __name__ == '__main__':
    atbash = Atbash()
    plain_text = 'irk low hob hold holy horn glow'
    encrypted = 'RIP OLD SLY SLOW SLOB SLIM TOLD'
    print("Testing Atbash cipher")
    assert encrypted == atbash.encrypt(plain_text)
    assert plain_text == atbash.decrypt(encrypted).lower()
    print('Cipher passed')
