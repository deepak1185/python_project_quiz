#asking user for next question
#

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # length = len(self.question_list)
        # if self.question_number < length:
        #     return True
        # else:
        #     return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number} : {current_question.text}: True/False? ")
        self.check_answer(user_answer, current_question.answer)



    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("You got it")
        else:
            print("Thats incorrect")
        print(f"The correct answer is {current_answer} ")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")






