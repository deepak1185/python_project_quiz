from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
#question = Question()

for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

print(question_bank[0].text)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    if quiz.still_has_questions() == False:
        print("You have completed the quiz")
        print(f"Your Total score is {quiz.score}/{quiz.question_number}")

