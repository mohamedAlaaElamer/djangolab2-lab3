from django import forms
from .models import *
class InsertTrainee(forms.Form):
    name= forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}))
    nationnum= forms.IntegerField()
    course= forms.ChoiceField(choices=[(c.id,c.name) for c in Course.objects.all()])

class InsertTrainee2(forms.ModelForm):
    #course = forms.ChoiceField(choices=[(c.id, c.name) for c in Course.objects.all()])
    class Meta:
       model=Trainee
       fields='__all__'#['name','nationalnum']#
