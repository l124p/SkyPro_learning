class Question:

    def __init__(self, text, level_question, answer_question):
        self.text = text
        self.level_question = level_question
        self.answer = answer_question
        self.check_question = False
        self.user_answer = None
        self.ball = self.level_question * 10

    def get_points(self):
        """Возвращает количество баллов. Баллы от сложности: за 1 дается 10 балов, за 5 дается 50 балов"""
        return self.ball

    def is_correct(self):
        """Возвращает True если ответ верный"""
        return self.answer == self.user_answer

    def build_question(self):
        """Возвращает вопрос в виде:
        Вопроc: ...?
        Сложность 4/5"""
        return f"Вопрос: {self.text} \nСложность {self.level_question}/5"

    def build_positive_feedback(self):
        """Возвращает:
        Ответ верный, получено __ баллов"""
        return f"Ответ верный, получено {self.ball} балов"

    def build_negative_feedback(self):
        """Возвращает:
        Ответ неверный, верный ответ __"""
        return f"Ответ неверный. Верный ответ - {self.answer}"

    def __repr__(self):
        return f"{self.text} - {self.answer} ({self.level_question}/5)"
