from abc import ABC,abstractmethod

class Question(ABC):

    def __init__(self,questionContent,fileName):
        self._questionContent = questionContent
        self._fileName = fileName
        self._isAnswerCorrect = False

    @abstractmethod
    def checkAnswer(self, userAnswer:str) -> bool:
        pass

class YesNoQuestion(Question):

    def __init__(self, questionContent, fileName, answerA, answerB, answerC, correctAnswer):
        super().__init__(questionContent, fileName)
        self.__answerA = answerA
        self.__answerB = answerB
        self.__answerC = answerC
        self.__correctAnswer = correctAnswer

    def checkAnswer(self, userAnswer:str) -> bool:
        if userAnswer==self.__correctAnswer:
            self._isAnswerCorrect = True
            return self._isAnswerCorrect
        else:
            self._isAnswerCorrect = False
            return self._isAnswerCorrect

if __name__ == '__main__':
    # obiektTestowy = Pytanie("Kto jest prezydentem polski?","prezydent.jpg")
    question = input("Wpisz pytanie\n")
    file = input("Podaj nazwe pliku graficznego\n")
    answer_a = input("Podaj odp A\n")
    answer_b = input("Podaj odp B\n")
    answer_c = input("Podaj odp C\n")
    correct_answer = input("Podaj poprawną odpowiedź (A, B lub C)\n")

    obj = YesNoQuestion(question, file, answer_a, answer_b, answer_c, correct_answer)

    user_answer = input(f"{question}\nOdp A: {answer_a}\nOdp B: {answer_b}\nOdp C: {answer_c}\n")
    result = obj.checkAnswer(user_answer)
    if result:
        print("Odpowiedź prawidłowa")
    elif not result:
        print("Odpowiedź nieprawidłowa")