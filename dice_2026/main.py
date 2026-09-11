import random

class Dice:
    instances_amount = 0

    def __init__(self, rolled_dice_value=None):
        self.dice_amount = 0
        self.file_names = ["Kosc0.png", "kosc1.png", "kosc2.png", "kosc3.png", "kosc4.png", "kosc5.png", "kosc6.png"]
        self.file_IDs = 0
        self.is_dice_available = True

        if rolled_dice_value is None:
            self.rolled_number = random.randint(1, 6)
            self.dice_amount=self.rolled_number
            self.file_IDs=self.rolled_number
        else:
            if rolled_dice_value in [1, 2, 3, 4, 5, 6]:
                self.dice_amount = rolled_dice_value
                self.file_IDs = rolled_dice_value
            else:
                self.dice_amount = 0
                self.file_IDs = 0

        Dice.instances_amount += 1

    def throwing(self):
        if self.is_dice_available:
            rolled = random.randint(1,6)
            self.dice_amount = rolled
            self.file_IDs = rolled

    def blocking(self):
        self.is_dice_available=False

    def throw_to_text(self):
        match self.dice_amount:
            case 1:
                return "jeden"
            case 2:
                return "dwa"
            case 3:
                return "trzy"
            case 4:
                return "cztery"
            case 5:
                return "pięć"
            case 6:
                return "sześć"
            case _:
                return "zero"

if __name__ == '__main__':

    obj1 = Dice()

    print(f"Liczba instancji {Dice.instances_amount}")
    print(f"Liczba oczek (liczbowo): {obj1.dice_amount}")
    print(f"Liczba oczek (słownie): {obj1.throw_to_text()}")
    print(f"Nazwa pliku graficznego: {obj1.file_names[obj1.file_IDs]}")

    value = int(input("\nPodaj wartość do drugiej kości (1-6)\n"))

    obj2 = Dice(value)
    print(f"Liczba instancji {Dice.instances_amount}")
    print(f"Liczba oczek (liczbowo): {obj2.dice_amount}")
    print(f"Liczba oczek (słownie): {obj2.throw_to_text()}")
    print(f"Nazwa pliku graficznego: {obj2.file_names[obj2.file_IDs]}")


