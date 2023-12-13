from django import forms
class EmpForm(forms.Form):
    Nam=forms.CharField()
    Job=forms.CharField()
    Loc=forms.CharField()
    Sal=forms.FloatField()
