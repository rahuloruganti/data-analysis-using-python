from data import question_data
from question_model import question
from quiz_brain import quizbrain
question_bank=[]
for i in question_data:
    q_text=i["text"]
    q_answer=i["answer"]
    new_question=question(q_text,q_answer)
    question_bank.append(new_question)

quiz=quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("you've completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")