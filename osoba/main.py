class Person:
    instancesAmount = 0

    def __init__(self, personID = 0, personName = ""):
        self.__personID = personID
        self.__personName = personName
        Person.instancesAmount+=1

    def copy(self, otherPerson):
        self.__personID = otherPerson.__personID
        self.__personName = otherPerson.__personName
        Person.instancesAmount+=1

    def printOut(self, otherName):
        if self.__personName == "":
            print("Brak danych")
        else:
            print(f"Cześć {otherName}, mam na imię {self.__personName}")

if __name__ == '__main__':

    print(f"Liczba zarejestrowanych osób to {Person.instancesAmount}")

    obiekt1 = Person()

    idUsera = int(input("Podaj swoje ID\n"))
    imieUsera = input("Podaj swoje imię\n")

    obiekt2 = Person(idUsera, imieUsera)

    obiekt3 = Person()
    obiekt3.copy(obiekt2)

    obiekt1.printOut("Jan")
    obiekt2.printOut("Jan")
    obiekt3.printOut("Jan")

    print(f"Liczba zarejestrowanych osób to {Person.instancesAmount}")


