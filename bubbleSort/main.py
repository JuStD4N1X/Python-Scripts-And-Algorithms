import random

def bubbleSort(tab):
    print(f"Nie posortowana {tab}")
    for x in range(len(tab)):
        for j in range(len(tab)-x-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    print(f"tablica posortowana {tab}")
if __name__ == '__main__':
    tab = []
    for i in range(100):
        rand = random.randint(1,100)
        tab.append(rand)
    bubbleSort(tab)

