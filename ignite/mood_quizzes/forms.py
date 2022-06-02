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