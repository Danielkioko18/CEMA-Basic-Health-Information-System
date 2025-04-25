from django.shortcuts import render, redirect
from .models import HealthProgram
from .forms import HealthProgramForm
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

