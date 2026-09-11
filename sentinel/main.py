from random import randint

def tabFiller():
    tab = []

    for i in range(50):
        randomNumber = randint(1, 100)
        tab.append(randomNumber)
    return tab

def search_number(sentinel):
    tab = tabFiller()
    print(tab)
    tab.append(sentinel)

    last_index = len(tab)-1
    found = False

    for letter in range(len(tab)):
        if tab[letter]==sentinel and letter!=last_index:
            print(f"Liczba jest na indeksie {letter}")
            found = True
            break
    if not found:
        print("Liczby nie znaleziono")

if __name__ == '__main__':

    number = int(input("Podaj liczbę do wyszukania\n"))
    search_number(number)
