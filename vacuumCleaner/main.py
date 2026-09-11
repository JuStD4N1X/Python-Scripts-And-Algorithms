class Devices:
    def showAnnouncement(self, announcement):
        print(announcement)

class WaschingMachine(Devices):
    def __init__(self):
            self.__wash_program_number = 0

    def set_wash_program_number(self, program_number):
        if 1 <= program_number <= 12:
            self.__wash_program_number = program_number
        else:
            self.__wash_program_number = 0
        return self.__wash_program_number
class VacuumCleaner(Devices):
    def __init__(self):
        self.__VCleaner_state = False
    def on(self):
        if not self.__VCleaner_state:
            self.__VCleaner_state = True
            self.showAnnouncement("Odkurzacz włączono")
    def off(self):
        if self.__VCleaner_state:
            self.__VCleaner_state = False
            self.showAnnouncement("Odkurzacz wyłączono")
if __name__ == '__main__':
    wasching_machine = WaschingMachine()

    wash_program_number = int(input("Podaj numer prania 1..12\n"))
    print(wasching_machine.set_wash_program_number(wash_program_number))

    next_wash_number = int(input("a teraz daj nie poprawny\n"))
    print(wasching_machine.set_wash_program_number(next_wash_number))

    vacuum_cleaner = VacuumCleaner()

    vacuum_cleaner.on()
    vacuum_cleaner.on()
    vacuum_cleaner.on()

    vacuum_cleaner.showAnnouncement("Odkurzacz wyładował się")

    vacuum_cleaner.off()




