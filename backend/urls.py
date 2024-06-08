from django.urls import path
from django.contrib import admin
# now import the views.py file into this code
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("admin", admin.site.urls),
  path('', views.CloseWave, name='CloseWave'),
  path('user_list', views.user_list, name='user_list'),
  path('manage', views.manage, name='manage'),
  path('show', views.show, name='show'),
  path('edit/<int:id>', views.edit, name='edit'),
  path('edit/update/<int:id>', views.update, name='update'),
  path('delete/<int:id>', views.destroy, name='destroy'),
  path('product', views.product, name='product'),
  path('product/todo', views.todo, name='todo'),
  path('product/editTodo/<int:id>', views.editTodo, name='editTodo'),
  path('product/editTodo/updateTodo/<int:id>', views.updateTodo, name='updateTodo'),
  path('product/deleteTodo/<int:id>', views.destroyTodo, name='destroyTodo'),
  path('product/EMS_page', views.EMS_page, name='EMS_page'),
  path('product/register', views.register, name='register'),
  path('product/login', views.login, name='login'),
  path('product/profile', views.profile, name='profile'),
  path('product/leave', views.leave, name='leave'),
  path('product/Taskassign', views.Taskassign, name='Taskassign'),
  path('product/done/delete/<int:task_id>/', views.delete_task, name='delete_task'),
  path('product/performance_page', views.performance_page, name='performance_page'),
  path('product/account_page', views.account_page, name='account_page'),
  path('product/user_list', views.user_list, name='user_list'),
  path('product/chatterbox', views.chatterbox, name='chatterbox'),
  path('product/send_message/<int:receiver_id>', views.send_message, name='send_message'),
  path('product/schedule_training', views.schedule_training, name='schedule_training'),
  path('product/manage_training', views.manage_training, name='manage_training'),
  path('product/view_schedule', views.view_schedule, name='view_schedule'),
  path('product/logout_view', views.logout_view, name='logout_view'),
  path('product/s_message', views.s_message, name='s_message'),
  path('product/group', views.group_messages, name='group_messages'),
  path('product/Recipe', views.recipe, name='recipe'),
  path('product/recipes', views.recipe_list, name='recipe_list'),
  path('product/recipe/<int:recipe_id>', views.recipe_detail, name='recipe_detail'),
  path('product/add_recipe', views.add_recipe, name='add_recipe'),
  path('product/Ecom', views.Ecom, name='Ecom'),
  path('product/job_list', views.job_list, name='job_list'),
  path('product/career-register', views.Careerregister, name='Careerregister'),
  path('product/career-login', views.Careerlogin, name='Careerlogin'),
  path('product/post_job/', views.post_job, name='post_job'),
  path('product/apply_job/<int:job_id>/', views.apply_job, name='apply_job'),
  path('product/job_list/', views.job_list, name='job_list'),
  path('product/application-success/', views.application_success, name='application_success'),
  ]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
