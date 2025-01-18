from django.db import models

class Scenario(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    choices = models.JSONField()  # Stores choices as JSON (e.g., ["Option 1", "Option 2"])
    correct_answers = models.JSONField()  # Stores correct choices

    def __str__(self):
        return self.title

class Player(models.Model):
    username = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    current_level = models.IntegerField(default=1)

    def __str__(self):
        return self.username
