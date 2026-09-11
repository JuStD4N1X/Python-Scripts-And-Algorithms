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

    object1 = Person()

    UserID = int(input("Podaj swoje ID\n"))
    UserName = input("Podaj swoje imię\n")

    object2 = Person(UserID, UserName)

    object3 = Person()
    object3.copy(object2)

    object1.printOut("Jan")
    object2.printOut("Jan")
    object3.printOut("Jan")

    print(f"Liczba zarejestrowanych osób to {Person.instancesAmount}")


