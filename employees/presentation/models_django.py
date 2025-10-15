from django.db import models

class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return self.name
