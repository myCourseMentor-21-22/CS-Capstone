from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    publisher = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Student(models.Model):
    stu_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.stu_id) + ', ' + self.name