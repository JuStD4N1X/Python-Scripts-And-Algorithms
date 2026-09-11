import random

def fillSets(n):
    columns = 6
    tab = [random.sample(range(1,50), columns)  for _ in range(n)]
    return tab

def showSets(tab):
    for SET in range(len(tab)):
        formatted_numbers = " ".join(map(str, tab[SET]))
        print(f"Losowanie {SET+1}: {formatted_numbers}")

def occurences(tab):
    counters = [0]*50

    for row in tab:
        for num in row:
            counters[num]+=1

    for num in range(1,50):
        print(f"Wystąpienia liczby {num}: {counters[num]}")

if __name__ == '__main__':
    sets_amount = int(input("Ile zestawów wylosować?\n"))
    print("Zestawy wylosowanych liczb: ")
    sets = fillSets(sets_amount)
    showSets(sets)
    occurences(sets)
