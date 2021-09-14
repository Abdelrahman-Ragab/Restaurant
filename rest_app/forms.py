from django import forms
from .models import *

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
        

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'