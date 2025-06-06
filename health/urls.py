from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Health app URLs parterns
urlpatterns = [
    path('create-program/', views.create_program, name='create_program'),
    path('home', views.program_list, name='program_list'),
    path('programs/edit/<int:program_id>/', views.edit_program, name='edit_program'),
    path('programs/delete/<int:program_id>/', views.delete_program, name='delete_program'),
    path('register-client/', views.register_client, name='register_client'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/edit/<int:client_id>/', views.edit_client, name='edit_client'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_client'),
    path('clients/enroll/<int:client_id>/', views.enroll_client, name='enroll_client'),
    path('clients/profile/<int:client_id>/', views.client_profile, name='client_profile'),
    path('api/client-profile/<int:client_id>/', views.client_profile_api, name='client_profile_api'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

