from django import forms
from basic_app.models import student

class studentForm(forms.ModelForm):
    class Meta():
        model = student
        fields = "__all__"
