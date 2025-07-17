from django import forms
from . import models

class AddSkillsForm(forms.ModelForm):
    class Meta:
        model = models.AddSkills
        fields = ['title', 'category','description','availability','location']

class RequestSkillsForm(forms.ModelForm):
    class Meta:
        model = models.RequestSkills
        fields = ['category','location','description']