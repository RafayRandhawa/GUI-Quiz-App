import html


class QuizBrain:
    def __init__(self, question_list):
        self.q_num = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.q_num

    def next_question(self):
        current_question = self.question_list[self.q_num]
        self.q_num += 1
        return html.unescape(f"Q{self.q_num}: "+current_question.text)

    def check_answer(self, user_answer):
        if user_answer.lower() == self.question_list[self.q_num-1].answer.lower():
            self.score += 1
            return True
        else:
            return False

