import random

class Game:
    def __init__(self):
        self.tab = []
        self.rolls_amount = 0
        self.sum = 0

    def roll(self, rolls_amount):
        self.rolls_amount = rolls_amount
        for i in range(self.rolls_amount):
            randomNumber = random.randint(1,6)
            self.tab.append(randomNumber)
            print(f"Kostka {i+1}: {randomNumber}")

    def count_points(self):
        self.tab.sort()
        counter = 1
        for i in range(1, len(self.tab)):
            if self.tab[i]==self.tab[i-1]:
                counter +=1
            else:
                if counter > 1:
                    self.sum += counter * self.tab[i - 1]
                counter = 1
        if counter > 1:
            self.sum += counter * self.tab[-1]
        print(f"Liczba uzyskanych punktów: {self.sum}")

if __name__ == '__main__':
    repeat = True
    while repeat:
        currentGame = Game()
        diceAmount = int(input("Ile kostek chcesz rzucić?(3 - 10)\n"))
        if 3 <= diceAmount <= 10:
            repeat = False
            currentGame.roll(diceAmount)
            currentGame.count_points()
            repeatOn = input("Jeszcze raz? (t/n)\n")
            if repeatOn=="t":
                repeat = True
            elif repeatOn=="n":
                repeat = False

