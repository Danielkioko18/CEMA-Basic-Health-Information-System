from django.urls import path
from . import views

urlpatterns = [
    path('create-program/', views.create_program, name='create_program'),
    path('programs/', views.program_list, name='program_list'),
    path('programs/edit/<int:program_id>/', views.edit_program, name='edit_program'),
    path('programs/delete/<int:program_id>/', views.delete_program, name='delete_program'),
]
