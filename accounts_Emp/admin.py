from django.contrib import admin
from .models import Rdetails, Edetails, Todo, EMS, Task, Performance_emp, Room, Chat, Training, Recipe, CareerRegister
from .models import MSG
from .models import Job, MyProfile, JobApplication

# Register your models here.
admin.site.register(Rdetails)
admin.site.register(Edetails)
admin.site.register(Todo)
admin.site.register(EMS)
admin.site.register(Task)
admin.site.register(Performance_emp)
admin.site.register(MSG)
admin.site.register(MyProfile)
admin.site.register(Room)
admin.site.register(Chat)
admin.site.register(Training)
admin.site.register(Recipe)
admin.site.register(CareerRegister)
admin.site.register(Job)
admin.site.register(JobApplication)
