# forms.py

from django import forms

# Taking input from HTML side, and setting constraints on those inputs
class ClassRoomForm(forms.Form):
    room = forms.CharField(max_length=4)
    day = forms.ChoiceField(choices=[("0", "Monday"), ("1", "Tuesday"), ("2", "Wednesday"),
                                     ("3", "Thursday"), ("4", "Friday"), ("5", "Saturday")])
    time = forms.ChoiceField(choices=[("0", "8 AM - 9 AM"), ("1", "9 AM - 10 AM"), ("2", "10 AM - 11 AM"),
                                      ("3", "11 AM - 12 PM"), ("4", "12 PM - 1 PM"), ("5", "1 PM - 2 PM"),
                                      ("6", "2 PM - 3 PM"), ("7", "3 PM - 4 PM"), ("8", "4 PM - 5 PM"), ("9", "5 PM - 6 PM")])
    stay_from = forms.ChoiceField(choices=[(str(i), f"{i} AM") for i in range(0, 9)])
    stay_to = forms.ChoiceField(choices=[(str(i), f"{i} AM") for i in range(1, 10)])
