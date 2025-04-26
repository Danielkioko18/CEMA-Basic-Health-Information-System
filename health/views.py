from django.shortcuts import render, redirect
from .models import HealthProgram, Client
from .forms import HealthProgramForm, ClientForm, EnrollClientForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ClientProfileSerializer
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Create a program view
@login_required
def create_program(request):
    if request.method == 'POST':
        form = HealthProgramForm(request.POST)
        if form.is_valid():
            # Save the new health program to the database
            form.save()
            messages.success(request, "Health program created successfully!")
            return redirect('program_list')  # Assuming there's a program list view to redirect to
    else:
        form = HealthProgramForm()

    return render(request, 'create_program.html', {'form': form})

# view the programs created in a  list
@login_required
def program_list(request):
    programs = HealthProgram.objects.all()
    return render(request, 'program_list.html', {'programs': programs})

# Edit the program details
@login_required
def edit_program(request, program_id):
    program = get_object_or_404(HealthProgram, id=program_id)
    if request.method == 'POST':
        form = HealthProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program_list')# redirect to the program list after editing
    else:
        form = HealthProgramForm(instance=program)
    return render(request, 'edit_program.html', {'form': form, 'program': program})

#delete program from the list of programs
def delete_program(request, program_id):
    program = get_object_or_404(HealthProgram, id=program_id)
    program.delete()
    return redirect('program_list')


# Register client view
@login_required
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client registered successfully!")
            return redirect('client_list')  # Redirect after successful registration to the lists page
    else:
        form = ClientForm()

    return render(request, 'register_client.html', {'form': form})

# Client list view
@login_required
def client_list(request):
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(contact_number__icontains=query)
        )
    else:
        clients = Client.objects.all()

    return render(request, 'client_list.html', {'clients': clients, 'query': query})

# Edit Clients
@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # redirect to client list after successful update
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'register_client.html', {'form': form, 'is_edit': True})


# delete client from the list
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('client_list')

# enroll a regiistered client to programs
@login_required
def enroll_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == 'POST':
        form = EnrollClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')# redirect to client list
    else:
        form = EnrollClientForm(instance=client)

    return render(request, 'enroll_client.html', {'form': form, 'client': client})

# Client's profile view
@login_required
def client_profile(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client_profile.html', {'client': client})



# API endpoint to retrieve client profile information
@api_view(['GET'])
def client_profile_api(request, client_id):
    '''
    Expose client details view for use in other systems
    API endpoint to retrieve a client's profile in JSON format.
    Includes the client's basic details and enrolled programs.
    '''
    client = get_object_or_404(Client, id=client_id)
    serializer = ClientProfileSerializer(client)
    return Response(serializer.data, content_type='application/json')# display the details in JSON format