from django.db import models


class Question(models.Model):
    CATEGORY_CHOICES = (
        ('History', 'History'),
        ('Math', 'Math'),
        ('Geography', 'Geography'),
        ('General', 'General')
    )
    first_line = models.CharField(max_length=200)
    last_line = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.first_line


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    first_choice = models.CharField(max_length=200)
    second_choice = models.CharField(max_length=200)
    third_choice = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=200)

    def __str__(self):
        return self.first_choice
