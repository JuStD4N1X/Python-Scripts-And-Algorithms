class SelectionSort:
    def __init__(self):
        self.tab = [0] * 10

    def __search_maximum(self, start_index):
        maxIndex = start_index

        for i in range(start_index+1,len(self.tab)):
            if self.tab[maxIndex]<self.tab[i]:
                maxIndex=i
        return maxIndex

    def sorting(self):
        for i in range(len(self.tab)-1):
            max_idx = self.__search_maximum(i)
            if max_idx != i:
                self.tab[max_idx],self.tab[i] = self.tab[i],self.tab[max_idx]

        return self.tab

    def load_data(self):
        print("Wprowadź 10 liczb całkowitych do posortowania\n")
        for i in range(10):
            self.tab[i] = int(input(f"Podaj element nr {i+1}\n"))

    def show(self):
        for liczba in self.tab:
            print(liczba, end=" ")


if __name__ == '__main__':

    obiekt = SelectionSort()
    obiekt.load_data()
    obiekt.sorting()
    obiekt.show()

