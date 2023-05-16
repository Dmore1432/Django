from django.db import models

# Create your models here.
class Teacher(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.Firstname}{self.Lastname}"

class Student(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Firstname}  {self.Lastname}"


class User(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.BigIntegerField()
    Password=models.CharField(max_length=50)


    def __str__(self):
        return self.Firstname


