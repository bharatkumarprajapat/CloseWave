from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import random
# Create your models here.
class Rdetails(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password1 = models.IntegerField()
    password12 = models.IntegerField()
    login = models.CharField(max_length=50)


class Edetails(models.Model):
    Emp_id = models.IntegerField()
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Emp_age = models.IntegerField()
    Emp_Role = models.CharField(max_length=50)
    Emp_city = models.CharField(max_length=50)
    Emp_salary = models.IntegerField()

    class Meta:
        db_table = "employee"


class Todo(models.Model):
    add = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    class Meta:
        db_table = "Task"


class EMS(models.Model):
    profile_picture = models.ImageField(upload_to='images/profile')
    summary = models.TextField()
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    twelfth_degree = models.CharField(max_length=100)
    twelfth_passout = models.CharField(max_length=50)
    twelfth_percentage = models.CharField(max_length=10)
    bachelor_degree = models.CharField(max_length=100)
    bachelor_passout = models.CharField(max_length=50)
    bachelor_percentage = models.CharField(max_length=10)
    salary = models.IntegerField()
    joining_date = models.CharField(max_length=50)  # Set default value here
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    bio = models.TextField()

    class Meta:
        db_table = "profile_data"


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Performance_emp(models.Model):
    rater = models.ForeignKey(User, related_name='ratings_given', on_delete=models.CASCADE)
    rated_user = models.ForeignKey(User, related_name='ratings_received', on_delete=models.CASCADE)
    rating = models.IntegerField()

class MSG(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Room(models.Model):
    name = models.CharField(max_length=3000)
class Chat(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=11000)


class Training(models.Model):
    training_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    trainer = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_to')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assignee')

    def __str__(self):
        return self.training_name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Recipe(models.Model):
    title = models.CharField(max_length=80)
    des = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/recipe')

class CareerRegister(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=1000)
    password2 = models.CharField(max_length=1000)


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    created_at = models.DateTimeField(auto_now_add=True)


class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    batch_year = models.IntegerField()

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='images/resume')
    applied_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    Skills = models.CharField(max_length=5000)

