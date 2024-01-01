from question_model import Question
from data import question_data 

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

score = 0

for question in question_bank:
    print(question.text)
    question_answer = input("True or False?")
    if question_answer == question.answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print()