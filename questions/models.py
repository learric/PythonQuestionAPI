from django.db import models


class Question(models.Model):
    CATEGORY_CHOICES = (
        ('History', 'History'),
        ('Math', 'Math'),
        ('Geography', 'Geography'),
        ('General', 'General')
    )

    first_line = models.TextField("Main text", max_length=200)
    last_line = models.TextField("Extra text", max_length=200, blank=True, help_text="Use this area for second line")

    first_choice = models.CharField(max_length=200)
    second_choice = models.CharField(max_length=200)
    third_choice = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=200, help_text="This MUST be the correct answer")

    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.first_line
