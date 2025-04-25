from django.urls import path
from . import views

urlpatterns = [
    path('create-program/', views.create_program, name='create_program'),
    path('programs/', views.program_list, name='program_list'),
    path('programs/edit/<int:program_id>/', views.edit_program, name='edit_program'),
    path('programs/delete/<int:program_id>/', views.delete_program, name='delete_program'),
    path('register-client/', views.register_client, name='register_client'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/edit/<int:client_id>/', views.edit_client, name='edit_client'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_client'),
    path('clients/enroll/<int:client_id>/', views.enroll_client, name='enroll_client'),
]

