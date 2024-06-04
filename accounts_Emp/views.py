from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password
from django.conf import settings
from .forms import EmployeeForm, TaskForm, ProfileForm, TaskForm2
from .models import Edetails
from .models import EMS
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .models import Task
from .models import Todo
from .models import Performance_emp
from .forms import PerformanceForm
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import MSG
from .forms import TrainingSessionForm
from .models import Training
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from .models import Message
from .models import Recipe
from .forms import RecipeForm

from .models import CareerRegister
from .forms import LoginForm
from .forms import CareerRegisterForm
from .models import Job, JobApplication
from .forms import JobForm, JobApplicationForm


def CloseWave(request):
    return render(request, 'Closewave.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        code = request.POST['code']  # New code field

        # Check if the code matches
        if code != "EMS24":
            error_message = 'Invalid code.'
            return render(request, 'register.html', {'error_message': error_message})

        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists.'
            return render(request, 'register.html', {'error_message': error_message})
        elif User.objects.filter(email=email).exists():
            error_message = 'Email already exists.'
            return render(request, 'register.html', {'error_message': error_message})
        elif password1 != password2:
            error_message = 'Passwords do not match.'
            return render(request, 'register.html', {'error_message': error_message})
        else:
            # Create the user with a hashed password
            password = make_password(password1)
            user = User.objects.create(username=username, email=email, password=password)
            user.save()

            # Send welcome email
            subject = 'Welcome to CloseWave Tech'
            message = f'Hello {username},\n\nWelcome to CloseWave Tech! Thank you for joining us.'
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            send_mail(subject, message, from_email, to_email, fail_silently=True)

            return redirect('login')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('EMS_page')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def manage(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'filldetails.html', {'form': form})


def show(request):
    employees = Edetails.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Edetails.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Edetails.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Edetails.objects.get(id=id)
    employee.delete()
    return redirect("show")


def product(request):
    return render(request, 'products.html')


# -------------------------------------------------------------------
# ---------------------------------TO DO -----------------------------
# -----------------------------------------------------------------------
# to do
def todo(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("todo")
            except:
                pass
    else:
        form = TaskForm()
    Tasks = Todo.objects.all()
    return render(request, 'Todo.html', {'form': form, 'Tasks': Tasks})


def editTodo(request, id):
    task = Todo.objects.get(id=id)
    return render(request, 'editTodo.html', {'task': task})


def updateTodo(request, id):
    task = Todo.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("todo")
    else:
        form = TaskForm(instance=task)
    return render(request, 'updateTodo.html', {'form': form, 'task': task})


def destroyTodo(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect("todo")


def checkpoint(request, id):
    task = Todo.objects.get(id=id)
    task.status = True
    task.save()
    return redirect('todo')


# -----------------------------------------------------------------
# --------------------------EMS----------------------------------------
# ------------------------------------------------------------------------
def EMS_page(request):
    return render(request, 'ems.html')


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'ems.html')  # Redirect to a success page
    else:
        form = ProfileForm()
    details = EMS.objects.all()
    return render(request, 'profile.html', {'form': form, 'details': details})


def leave(request):
    if request.method == 'POST':
        # Extract form data
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        name = request.POST.get('name')
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        # Construct email content
        email_message = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'contact': contact,
            'subject': subject,
            'message': message,
            'start_date': start_date,
            'end_date': end_date,
            'reason': reason
        })

        try:
            # Send email
            send_mail(
                subject,
                email_message,
                email,
                [to_email],
                fail_silently=False,
            )
            return HttpResponse('Email sent successfully!')
        except Exception as e:
            return HttpResponse('An error occurred while sending email.')

    return render(request, 'leave.html')


def Taskassign(request):
    user_list = ['Ram', 'AjayPrajapat']
    if request.user.username in user_list:
        if request.method == 'POST':
            form = TaskForm2(request.POST)
            if form.is_valid():
                form.save()
                return redirect('EMS_page')  # Redirect to the same page after form submission
        else:
            form = TaskForm2()
        tasks = Task.objects.all()
        users = User.objects.all()
        return render(request, 'task_assignment.html', {'tasks': tasks, 'users': users, 'form': form})
    else:
        tasks_assigned_to_user = Task.objects.filter(assigned_to=request.user)
        return render(request, 'task_assignment_page.html', {'tasks': tasks_assigned_to_user})


def delete_task(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(pk=task_id)
            task.delete()  # Or mark the task as completed in your model
            send_email_notification(task)
            return HttpResponse('Task marked as done and email sent successfully!')
        except Task.DoesNotExist:
            return HttpResponse('Task does not exist.')
    else:
        return HttpResponse('Invalid request method.')


def send_email_notification(task):
    lead_email = 'ajayy9242@gmail.com'  # Change to the lead's email address
    subject = 'Task Completed'
    message = render_to_string('task_completed_email.html', {'task': task})
    send_mail(subject, message, 'from@example.com', [lead_email], fail_silently=False)


@login_required
def performance_page(request):
    if request.user.username != 'ram':
        return redirect('account_page')  # Redirect to user account page if not 'ram'

    form = PerformanceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        rated_user = form.cleaned_data['rated_user']
        rating = form.cleaned_data['rating']
        Performance_emp.objects.create(rater=request.user, rated_user=rated_user, rating=rating)
        return redirect('performance_page')

    return render(request, 'performance.html', {'form': form})


@login_required
def account_page(request):
    user_performance = Performance_emp.objects.filter(rated_user=request.user)
    return render(request, 'account.html', {'user_performance': user_performance})


def chatterbox(request):
    return render(request, 'ChatBox.html')


def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'user_list.html', {'users': users})


def send_message(request, receiver_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver_id = receiver_id
            message.save()
            return redirect('send_message', receiver_id=receiver_id)
    else:
        form = MessageForm()

    # Filter messages based on sender and receiver IDs
    user_id = request.user.id
    messages_sent_by_user = MSG.objects.filter(sender_id=user_id, receiver_id=receiver_id)
    messages_received_by_user = MSG.objects.filter(sender_id=receiver_id, receiver_id=user_id)

    # Combine both sets of messages
    messages = messages_sent_by_user | messages_received_by_user

    return render(request, 'send_message.html', {'form': form, 'messages': messages})


@login_required
def schedule_training(request):
    if request.user.username in ['Ram', 'AjayPrajapat']:
        if request.method == 'POST':
            form = TrainingSessionForm(request.POST)
            if form.is_valid():
                training_session = form.save(commit=False)
                training_session.assignee = request.user
                training_session.save()
                return redirect('manage_training')
        else:
            form = TrainingSessionForm()
        return render(request, 'training.html', {'form': form})
    else:
        return view_schedule(request)


@login_required
def manage_training(request):
    if request.user.username in ['Ram', 'AjayPrajapat']:
        training_sessions = Training.objects.all()
        return render(request, 'manage_training.html', {'training_sessions': training_sessions})
    else:
        return view_schedule(request)


@login_required
def view_schedule(request):
    training_sessions = Training.objects.all()
    return render(request, 'view_schedule.html', {'training_sessions': training_sessions})


def logout_view(request):
    logout(request)
    return redirect('product')


@login_required
def s_message(request):
    if request.method == 'POST':
        if request.user.is_staff:  # Check if user is admin
            content = request.POST.get('content')
            message = Message.objects.create(sender=request.user, content=content)
            return redirect('group_messages')
        else:
            return redirect('group_messages')  # Redirect non-admin users
    return render(request, 's_message.html')


@login_required
def group_messages(request):
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'group_messages.html', {'messages': messages})


@staff_member_required
def s_message(request):
    if request.method == 'POST':
        if request.user.is_staff:  # Check if user is admin
            content = request.POST.get('content')
            message = Message.objects.create(sender=request.user, content=content)
            return redirect('group_messages')
        else:
            return redirect('group_messages')  # Redirect non-admin users
    return render(request, 's_message.html')


# ----------------------------------------------------------------------------------------
# ---------------------------------Recipe Sharing-----------------------------------------
# -----------------------------------------------------------------------------------------

def recipe(request):
    return render(request, 'recipe.html')


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})


# ----------------------------------------------------------------------------------------------------#
# ------------------------------JOB-BOARD--------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------


def Careerregister(request):
    if request.method == 'POST':
        form = CareerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Hash the password before saving
            user.password1 = make_password(form.cleaned_data['password1'])
            user.save()
            return redirect('Careerlogin')  # Redirect to login page after successful registration
    else:
        form = CareerRegisterForm()
    return render(request, 'career-register.html', {'form': form})


def Careerlogin(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            users = CareerRegister.objects.filter(username=username)
            if users.exists():
                for user in users:
                    if user.password2 == password:
                        # Login successful
                        # You may set session variables or use Django's authentication system here
                        return redirect('job_list')  # Redirect to home page after login
                error = 'Invalid password'
            else:
                error = 'User does not exist'
    else:
        form = LoginForm()
    return render(request, 'career-login.html', {'form': form, 'error': error})


def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'post_job.html', {'form': form})


def job_details(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'job_details.html', {'job': job})


def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            # Redirect to the success page upon successful application
            return redirect('application_success')
    else:
        form = JobApplicationForm()
    return render(request, 'apply_job.html', {'form': form})


def application_success(request):
    # Render the success page
    return render(request, 'application_success.html')


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})


# ---------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------#
# -----------------------------------E-COM IMPLEMENTATION----------------------------------------------------#

def Ecom(request):
    return render(request, 'EcloseWave.html')
