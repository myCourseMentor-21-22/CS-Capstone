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
        
class Credentials(models.Model):
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.email

class Post(models.Model):
    post = models.CharField(max_length=100)

class PredictPrior(models.Model):
    studentId = models.IntegerField()
    cs101 = models.FloatField()
    cs102 = models.FloatField()
    cs140 = models.FloatField()
    mth120 = models.FloatField()

class GradeData(models.Model):
    studentId = models.IntegerField()
    cs101 = models.CharField(max_length=6)
    cs102 = models.CharField(max_length=6)
    cs140 = models.CharField(max_length=6)
    mth120 = models.CharField(max_length=6)
    hw1 = models.CharField(max_length=6)
    test1 = models.CharField(max_length=6)
    hw3 = models.CharField(max_length=6)
    test2 = models.CharField(max_length=6)
    final = models.CharField(max_length=6)