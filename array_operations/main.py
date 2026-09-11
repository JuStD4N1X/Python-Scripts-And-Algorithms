import random

class ArrayOperations:
    def __init__(self, tab_size):
        self.__elementsAmount = tab_size
        self.__tab = []
        rand = random
        for i in range(self.__elementsAmount):
            self.__tab.append(rand.randint(1,1000))

    def show(self):
        for i in range(len(self.__tab)):
            print(f"indeks nr {i}: {self.__tab[i]}")

    def search(self, value):
        index = -1
        for i in range(len(self.__tab)):
            if self.__tab[i]==value:
                index = i
                break
        return index

    def odd_nums(self):
        odd = []
        for i in range(len(self.__tab)):
            if self.__tab[i]%2!=0:
                odd.append(self.__tab[i])
        return odd

    def getAverage(self):
        nums = 0
        for i in range(len(self.__tab)):
            nums+=self.__tab[i]
        average = nums/self.__elementsAmount
        return average

if __name__ == '__main__':

    obj = ArrayOperations(6)

    print("--- Metoda wyświetl --- ")
    obj.show()

    print("--- Metoda szukająca (liczba 17) ---")
    sought_after = obj.search(17)
    if sought_after != -1:
        print(f"Znaleziono szukaną liczbe na indeksie {sought_after}")

    print("--- Metoda wyświeltająca nieparzyste ---")
    tabOdd = obj.odd_nums()
    for i in range(len(tabOdd)):
        print(tabOdd[i])
    print(f"Razem nieparzystych: {len(tabOdd)}")

    print("--- Metoda licząca średnią ---")
    print(f"Średnia wszystkich elementów: {obj.getAverage()}")



