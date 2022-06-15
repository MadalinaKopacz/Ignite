from django import forms
from .models import Question


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["qtype", "text"]
    

class QuestionUpdateTypeForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["qtype"]


class QuestionUpdateTextForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text"]


class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["qtype", "text"]


class QuizForm(forms.Form):
    CHOICES=[('2','Strongly disagree'),
                ('4', "Disagree"),
                ('6', "Neutral"),
                ('8', "Agree"),
                ('10', "Strongly agree")]

    answer1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    answer2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    answer3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)