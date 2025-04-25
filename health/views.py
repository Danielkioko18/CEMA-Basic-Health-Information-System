from django.shortcuts import render, redirect
from .models import HealthProgram, Client
from .forms import HealthProgramForm, ClientForm
from django.shortcuts import get_object_or_404

def create_program(request):
    if request.method == 'POST':
        form = HealthProgramForm(request.POST)
        if form.is_valid():
            # Save the new health program to the database
            form.save()
            return redirect('program_list')  # Assuming there's a program list view to redirect to
    else:
        form = HealthProgramForm()

    return render(request, 'create_program.html', {'form': form})

# view the program list
def program_list(request):
    programs = HealthProgram.objects.all()
    return render(request, 'program_list.html', {'programs': programs})


def edit_program(request, program_id):
    program = get_object_or_404(HealthProgram, id=program_id)
    if request.method == 'POST':
        form = HealthProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = HealthProgramForm(instance=program)
    return render(request, 'edit_program.html', {'form': form, 'program': program})


def delete_program(request, program_id):
    program = get_object_or_404(HealthProgram, id=program_id)
    program.delete()
    return redirect('program_list')


# Register client view
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Redirect after successful registration
    else:
        form = ClientForm()

    return render(request, 'register_client.html', {'form': form})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'register_client.html', {'form': form})


def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('client_list')

