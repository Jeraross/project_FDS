from django.urls import path
from app_cuida import views
from django.contrib import admin


urlpatterns = [
    path('', views.register,name='register'),
    path('home/', views.home, name='home'), 
    path('admin/', admin.site.urls),
    path('pacientes/', views.pacientes, name='listagem_pacientes'),
    path('update/<int:id_paciente>/', views.update, name='update_paciente'),
    path('delete/<int:id_paciente>/', views.delete_paciente, name='delete_paciente'),
    path('login/', views.login_view, name='login'), 
]

