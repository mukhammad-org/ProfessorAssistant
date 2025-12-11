import uploadfile
import random
def pick_random_questions(QuestionsBank, num):
    return random.sample(QuestionsBank, num) 

questions = uploadfile.load_questions()
selected = pick_random_questions(questions, 5)
print(selected)