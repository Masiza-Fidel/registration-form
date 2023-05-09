from django.db import models

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100, default='')
    fan_activity = models.CharField(max_length=100)
    free_time_activity = models.CharField(max_length=100)
    crazy_idea = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    goals = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.first_name
