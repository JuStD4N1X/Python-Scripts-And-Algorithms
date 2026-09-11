class stringHandler:
    @staticmethod
    def counter(word: str):
        vowelsAmount = 0
        vowels = ["a","ą","e","ę","i","o","u","ó","y","A","Ą","E","Ę","I","O","U","Ó","Y"]
        if word=="" or word is None:
            return vowelsAmount
        else:
            for letter in word:
                if letter in vowels:
                    vowelsAmount+=1
            return vowelsAmount

    @staticmethod
    def repeatRemover(messyWord: str):
        if messyWord=="" or messyWord is None:
            return ""
        else:
            cleanWord = ""
            for i in range(len(messyWord)-1):
                if messyWord[i]!=messyWord[i+1]:
                    cleanWord+=messyWord[i]
            cleanWord+=messyWord[-1]
            return cleanWord

if __name__ == '__main__':
    print(stringHandler.counter("chocolate"))
    print(stringHandler.repeatRemover("ccccchocollllatttteee"))

