from django.db import models

# Create your models here.

class Guardian(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    dob = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    rwp = models.CharField(max_length=50)
    
class Category(models.Model):
    category = models.CharField(max_length=30, default=None)

class Patient(models.Model):
    guardian = models.ForeignKey(Guardian, null=True, unique=False, default=None, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    address = models.TextField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=100, null=True)
    category=models.ForeignKey(Category, null=True, default=None, on_delete=models.CASCADE)

class Question(models.Model):
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.CASCADE)
    question = models.TextField()

    def __init__(self, question):
        self.question = question

class Answer(models.Model):
    guardian = models.ForeignKey(Guardian, null=True, default=None, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=True, default=None, on_delete=models.CASCADE)
    answer = models.IntegerField(null=True, default=None)

class Result(models.Model):
    guardian = models.ForeignKey(Guardian, null=True, default=None, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, null=True, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(null=True)
    asd_status = models.IntegerField(null=False)

















