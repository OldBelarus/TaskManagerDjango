from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from task_management_system_app import views
from django.urls import path, include
from task_management_system_app.views import CustomLoginView

urlpatterns = [
    # Административный интерфейс
    path('admin/', admin.site.urls),

    # Аутентификация
    # Используем встроенное представление Django для логина, но указываем свой шаблон.
    path('accounts/login/', CustomLoginView.as_view(), name='login'),

    # Переопределяем логаут — здесь можно использовать ваше представление.
    path('accounts/logout/', views.LogoutPage, name='logout'),

    # Другие стандартные URL-ы аутентификации (смена пароля и т.д.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Регистрация нового пользователя
    path('register/', views.register, name='register'),

    # Страницы управления задачами и категориями
    # После логина для обычного пользователя перенаправляем на страницу с заданиями
    path('user/', views.user_tasks_list, name='user_tasks_list'),

    # Главная страница – список категорий
    path('', views.category_list, name='category_list'),

    # Создание и просмотр задач по категориям
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.category_tasks, name='category_tasks'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),

    # CRUD-операции над задачами
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/update/<int:task_id>/', views.update_task, name='update_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # Страница со статистикой (например, диаграмма задач)
    path('task-chart/', views.task_chart, name='task_chart'),
    path('tasks/toggle/<int:task_id>/', views.toggle_task_completion, name='toggle_task')

]

handler404 = 'task_management_system_app.views.custom_404_view'