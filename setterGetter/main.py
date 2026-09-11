class Film:
    def __init__(self):
        self._title = ""
        self._rentalsAmount = 0

    def setter(self, newTitle):
        self._title = newTitle[:20]

    def getter(self):
        return self._title

    def getterIncrementation(self):
        return self._rentalsAmount

    def increment(self):
        self._rentalsAmount+=1
if __name__ == '__main__':
    object1 = Film()
    print(f"Stan poczatkowy - Tytuł: {object1.getter()}\nLiczba Wypożyczeń: {object1.getterIncrementation()}\n")

    object1.setter("Ciekawy film")
    result = object1.getter()
    print(result)

    preIncrementResult = object1.getterIncrementation()
    print(f"Przed inkrementacją: {preIncrementResult}")
    object1.increment()
    postIncrementResult = object1.getterIncrementation()
    print(f"po inkrementacji: {postIncrementResult}")

