from django import forms
from django.core.exceptions import ValidationError
from .models import marks
class marksform(forms.ModelForm):
	class Meta:
		model = marks
		fields = "__all__"
		widgets = {
            'Roll_no': forms.NumberInput(
                 attrs={'class' : "form-control"}),
            'Name': forms.TextInput(
                 attrs={'class' : "form-control"}), 
            'Math_Marks': forms.NumberInput(
                 attrs={'class' : "form-control prc"}), 
			'Physics_Marks': forms.NumberInput(
                 attrs={'class' : "form-control prc"}), 
			'Chemistry_Marks': forms.NumberInput(
                 attrs={'class' : "form-control prc"}),
			'Total': forms.NumberInput(
                 attrs={'id':'Total', 'class' : "form-control"}), 
               'Per': forms.NumberInput(
                 attrs={'id':'Per', 'class' : "form-control"}),   	  	 	                        
        }