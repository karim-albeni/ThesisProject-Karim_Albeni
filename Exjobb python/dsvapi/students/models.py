from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    program = models.CharField(max_length=50)

    def __str__(self):
        return self.name
