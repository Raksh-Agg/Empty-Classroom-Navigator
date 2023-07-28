import csv
from django.shortcuts import render

room = 6100
time = ""
map_csv_file = []
schedule_csv_file = []

def index(request):
    return render(request, 'index.html')

def submit_form(request):
    if request.method == 'POST':
        room = request.POST.get('room')
        time = request.POST.get('time')
        map_csv_file = request.FILES['map_csv']
        schedule_csv_file = request.FILES['schedule_csv']

        # Process the uploaded CSV files here
        # Example: Read the CSV data using the csv module
        map_data = []
        schedule_data = []

        if map_csv_file:
            reader = csv.reader(map_csv_file)
            map_data = list(reader)

        if schedule_csv_file:
            reader = csv.reader(schedule_csv_file)
            schedule_data = list(reader)

        # Do further processing with the form data and CSV data as needed

        # You can pass the form data and processed CSV data to a new template
        return render(request, 'result.html', {
            'room': room,
            'time': time,
            'map_data': map_data,
            'schedule_data': schedule_data,
        })
    else:
        # Handle other HTTP methods (GET, etc.) here if needed
        pass
