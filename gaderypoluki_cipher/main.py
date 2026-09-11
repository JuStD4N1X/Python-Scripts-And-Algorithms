def encrypt(user_text):
    cipher = {
        "G": "A",
        "A": "G",
        "D": "E",
        "E": "D",
        "R": "Y",
        "Y": "R",
        "P": "O",
        "O": "P",
        "L": "U",
        "U": "L",
        "K": "I",
        "I": "K"
    }
    encrypted_text = ""
    for item in user_text:
        if item in cipher:
            encrypted_text += cipher[item]
        else:
            encrypted_text += item
    return encrypted_text

if __name__ == '__main__':

   text = input("podaj tekst do zaszyfrowania\n")
   print(encrypt(text))

