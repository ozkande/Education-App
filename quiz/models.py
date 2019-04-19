from django.db import models


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name_plural = 'quizzes'


class Question(models.Model):
    question_heading = models.CharField(max_length=250)
    question_text = models.CharField(max_length=500)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_heading


class Answer(models.Model):
    answer_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    right_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text



