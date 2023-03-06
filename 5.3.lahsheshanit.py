# The function extracts the secret messages from the logo file
def messages():
    with open('C:/Users/Adiel/PycharmProjects/excellentTeam/logo.jpg', 'rb') as f:  # opening a binary file
        secret = ""
        while True:
            char = f.read(1)  # Read from the file character by character
            if not char:  # If we have reached the end of the file
                break
            char_in_hex = char.hex()
            an_integer = int(char_in_hex, 16)

            if 0x61 <= an_integer <= 0x7A:  # Checking if the character is lowercase
                secret += chr(an_integer)

            elif an_integer == 0x21:  # Checking if the character is an exclamation mark (!)
                secret += chr(an_integer)
                # Checking if the length of the string is greater than 6 characters, including the exclamation mark
                if len(secret) >= 6:
                    yield secret
                    secret = ""

            else:
                secret = ""

    f.close()  # Close the file


for message in messages():
    print(message)
