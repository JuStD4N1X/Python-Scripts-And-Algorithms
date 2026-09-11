def encrypt(plain_text: str, raw_key: int):
    if raw_key == 0:
        return plain_text

    key = raw_key % 26
    char_codes = []
    processed_text = ""

    for letter in plain_text:
        if letter == " ":
            char_code = 32
        else:
            char_code = ord(letter) + key
            if char_code < 97:
                char_code += 26
            elif char_code > 122:
                char_code -= 26
        char_codes.append(char_code)

    for i in range(len(char_codes)):
        processed_text += chr(char_codes[i])

    return processed_text


if __name__ == '__main__':
    text = input("Podaj tekst do zaszyfrowania\n")
    key = int(input("Podaj klucz\n"))

    encrypted_text = encrypt(text, key)
    print(encrypted_text)