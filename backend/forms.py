from django import forms
from .models import Edetails
from .models import Todo
from .models import EMS
from .models import Task
from .models import Performance_emp
from .models import MSG
from .models import Training
from .models import Recipe
from .models import JobApplication
from .models import Job

from .models import CareerRegister
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = MSG
        fields = ['content']


class TaskForm2(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description',  'assigned_to']
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Edetails
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['add']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = EMS
        fields = '__all__'


class PerformanceForm(forms.Form):
    rated_user = forms.ModelChoiceField(queryset=User.objects.all(), label='User to rate')
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=5)

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['training_name', 'date', 'time', 'trainer','assignee','assigned_to']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'des', 'image']


class CareerRegisterForm(forms.ModelForm):
    class Meta:
        model = CareerRegister
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'Skills', 'resume']

