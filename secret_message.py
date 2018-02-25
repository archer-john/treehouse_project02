from affine import Affine
from atbash import Atbash
from keywords import Keyword


def run():
    """
    Command line interface for encrypting / decrypting messages.
    :return: None
    """
    # dictionary containing implemented ciphers
    cipher_dict = {'affine': Affine, 'atbash': Atbash, 'keyword': Keyword}
    while True:
        print('This is the Secret Messages project for the '
              'Treehouse Techdegree \n')
        print('The following ciphers are available:\n')
        print('1. Affine \n')
        print('2. Atbash \n')
        print('3. Keyword \n')
        print('Enter quit or q to end.')
        print()
        user_input = input("Which cipher would you like to use? ").lower()
        print()
        if user_input == 'q' or user_input == 'quit':
            print('Have a wonderful day!')
            break
        if user_input in cipher_dict:
            message = input("What's the message? ")
            method = input('Do you want to encrypt or decrypt? ')
            while True:
                if method == 'encrypt':
                    cipher = cipher_dict[user_input]()
                    print('Your message has been encrypted:\n')
                    print(cipher.encrypt(message))
                    break
                elif method == 'decrypt':
                    cipher = cipher_dict[user_input]()
                    print('Your message has been decrypted:\n')
                    print(f'*'*4, cipher.decrypt(message), '*'*4)
                    break
                else:
                    print('[!] - Incorrect entry you can only encrypt '
                          'or decrypt')
                    method = input('Please try again would you like to encrypt '
                                   'or decrypt')

            print()
            another = input('Would you like to Encrypt/Decrypt'
                            ' another Y/N: ').lower()
            if another == 'y' or another == 'yes':
                continue
            else:
                break
        else:
            print('[!] -  You can only select from the ciphers listed')


if __name__ == "__main__":
    run()
