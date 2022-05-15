from django import forms
from .models import Activity, ActivityScore
 
 
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity

        fields = [
            "name",
            "description",
            "location", 
            "location_type"
        ]

