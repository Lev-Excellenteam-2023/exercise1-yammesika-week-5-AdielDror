"""Extracts the secret messages from the logo file.

This file contains the following functions:

    * is_lowercase - return true if the character is lowercase,
      false otherwise
    * is_exclamation - return true if the character is an exclamation
      mark (!), false otherwise
    * messages - the main function of the script
"""


def messages():
    with open('logo.jpg', 'rb') as f:
        secret = ""
        while True:
            char = f.read(1)
            if not char:
                break
            if is_lowercase(char):
                secret += chr(int(char.hex(), 16))
            elif is_exclamation(char):
                secret += chr(int(char.hex(), 16))

                if len(secret) >= 6:
                    yield secret
                    secret = ""
            else:
                secret = ""


def is_lowercase(char: bytes) -> bool:
    return b'a' <= char <= b'z'


def is_exclamation(char: bytes) -> bool:
    return char == b'!'


if __name__ == '__main__':
    for message in messages():
        print(message)
