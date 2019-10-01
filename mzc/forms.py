from django import forms
forms .models import faculty

class Factultyform('forms.Modelform'):

    class Meta:
        model=Factulty
        fields='_all_'