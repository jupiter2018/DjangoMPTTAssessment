from django import forms
from showData.models import File

class FileForm(forms.Form):
    choices=File.objects.all()
    file_name = forms.CharField(label='File name', max_length=100)
    parent = forms.ChoiceField(choices=choices, widget=forms.Select())