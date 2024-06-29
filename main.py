from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for x in question_data:
    question = Question(x['question'], x['correct_answer'])
    question_bank.append(question)

Quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(Quiz)
