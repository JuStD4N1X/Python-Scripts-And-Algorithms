class Note:
    __noteCounter = 0

    def __init__(self, noteTitle, noteContent):
        self._noteTitle = noteTitle
        self._noteContent = noteContent
        Note.__noteCounter+=1
        self.__id = Note.__noteCounter

    def showNote(self):
        print(f"Tytuł notatki: {self._noteTitle}\nTreść notatki: {self._noteContent}")

    def diagnoseNote(self):
        print(f"Zawartość wszystkich pól (id;tytuł;treść;licznik): {self.__id};{self._noteTitle};{self._noteContent};{Note.__noteCounter}\n")

if __name__ == '__main__':
    object1 = Note("Koty", "Kocham koty\n")
    object1.showNote()
    object1.diagnoseNote()

    object2 = Note("Psy", "Kocham psy\n")
    object2.showNote()
    object2.diagnoseNote()


