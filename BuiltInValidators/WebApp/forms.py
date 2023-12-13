from django import forms
from django.core import validators

class EmpForm(forms.Form):
    Name = forms.CharField()
    Sala = forms.IntegerField()

    def clean(self):
        totalformclean = super().clean()

        iname = totalformclean['Name']
        if len(iname)<10:
            raise  forms.ValidationError("Name must be min 10 characters")
        isal = totalformclean['Sala']
        if isal==0:
            raise forms.ValidationError("salary must be >0")
#def StartsWithAlpha(value):
#   if value.isalpha() != True:
#      raise forms.ValidationError("Name must have only alphabets")

#class EmpForm (forms.Form):
#    Name=forms.CharField(validators=[StartsWithAlpha])
#    Sals=forms.IntegerField()
#    FeedBack=forms.CharField(widget=forms.Textarea,
#                             validators=[validators.MaxLengthValidator(40),
#                            validators.MinLengthValidator(10)])
     
