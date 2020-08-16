from django import forms
from .models import todo
class todoform(forms.ModelForm):
    class Meta:
        model=todo
        fields=['title','due_date']
class delaform(forms.ModelForm):
    class Meta:
        model=todo
        fields=['title']
