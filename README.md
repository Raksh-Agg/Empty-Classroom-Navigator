# Class Room Navigator
Class Room Navigator is a Django web application that helps users to find an order of empty classrooms which require least effort from the user's side, also, finding an the order of rooms based on a class the user may have to attend during the day. Users can upload the timetable for their semester in thr form of a csv themselves, as a `TimeTable.csv` file


## File Structure
The key components include:
- `functionality/`: This directory contains the custom Python module with the following files:
  - `Navigator.py`: Gives the final order of rooms to be followed as a list
  - `ReadMap.py`: Reads CSV file of map and refines data to store it in a 2D list, containing distances of each room with each other in a sorted manner.
  - `ReadSchedule.py`: Contains functions to read schedule data.
  - `main.py`: Contains the main function (`the_apex`) that integrates all functionalities and returns a string.
- `myapp/`: This is the Django project directory with the following files:
  - `settings.py`: Django project settings file.
  - `urls.py`: Django project URLs configuration file.
- `templates/index.html`: The HTML template for the web application, containing the form for user input and the output display.
- `static/style.css`: The CSS file for styling the HTML template.

## Setup and Installation
To run the Class Room Navigator web application, follow these steps:
1. Clone this repository to your local machine.
2. Make sure you have Python and Django installed on your system.
3. Run the Django development server using the command `python manage.py runserver`.

## Usage
1. Access the application through your web browser by visiting `http://127.0.0.1:8000/`.
2. Fill in the class details in the provided form, such as the room, day, time, and preferred stay hours.
3. Click the "Submit" button to process the information and view the output.
4. The output will be displayed below the form, showing the optimal route for your class schedule.

## Contributing
Contributions to Class Room Navigator are welcome! If you have any suggestions you can message me over github or other social media platforms and I shall get back to you.
