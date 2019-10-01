from django import forms
forms .models import faculty

class Factultyform(forms.Modelform):

    class Meta:
        model=factulty
        fields='__all__'