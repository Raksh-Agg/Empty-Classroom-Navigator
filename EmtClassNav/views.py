import csv
from django.shortcuts import render

# views.py

from .forms import ClassRoomForm
# from functionality import Navigator, ReadMap, ReadSchedule, main
from functionality.Navigator import final_function
from functionality.ReadMap import refine_map_data
from functionality.ReadSchedule import refine_schedule_data
from functionality.main import the_apex

def index(request):
    return render(request, 'index.html')

# views.py

def submit_form(request):
    if request.method == 'POST':
        form = ClassRoomForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            day = form.cleaned_data['day']
            time = form.cleaned_data['time']
            stay_from = form.cleaned_data['stay_from']
            stay_to = form.cleaned_data['stay_to']

            # Call functions from main.py with the required parameters
            lines = the_apex(room, day, time, stay_from, stay_to)
            print (lines)
            # Render the template with the lines fetched from main.py
            return render(request, 'index.html', {'lines': lines})
        else : 
            print ("Test Hello")
            print (form.errors)

    else:
        form = ClassRoomForm()

    return render(request, 'index.html', {'form': form})

