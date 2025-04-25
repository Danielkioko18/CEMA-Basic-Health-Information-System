from django.db import models

# Program Table
class HealthProgram(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Client Table
class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=gender_choices)
    contact_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    enrolled_programs = models.ManyToManyField(HealthProgram, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
