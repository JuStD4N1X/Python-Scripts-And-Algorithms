def checkSex(pesel):
    peselTab = [int(number) for number in pesel]
    if peselTab[9]%2==0:
        sex = "K"
    else:
        sex = "M"
    return sex

def checkPesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    peselTab = [int(number) for number in pesel]

    S = (peselTab[0]*1 + peselTab[1]*3 + peselTab[2]*7 +
         peselTab[3]*9 + peselTab[4]*1 + peselTab[5]*3 +
         peselTab[6]*7 + peselTab[7]*9 + peselTab[8]*1 +
         peselTab[9]*3)
    M = S%10
    if M==0:
        R=0
    else:
        R=10-M
    if R==peselTab[10]:
        isValid = True
    else:
        isValid = False
    return isValid

if __name__ == '__main__':

    pesel = input("Proszę podać pesel do zweryfikowania ")
    print(pesel)

    checksum = checkPesel(pesel)
    if checksum:
        verified_sex = checkSex(pesel)

        if verified_sex== "K":
            print("Kobieta")
        elif verified_sex== "M":
            print("Mężczyzna")

        print("Suma kontrolna się zgadza, wprowadzony pesel jest poprawny")
    else:
        print("Suma kontrolna się nie zgadza, wprowadzono niepoprawny pesel")

