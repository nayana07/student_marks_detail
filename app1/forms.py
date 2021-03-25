from django import forms
from django.core.exceptions import ValidationError
from .models import marks, sci_marks, art_marks, commerce_marks
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

class sci_marksform(forms.ModelForm):
     class Meta:
          model = sci_marks
          fields = "__all__"
          widgets = {
               'Roll_no': forms.NumberInput(attrs={'class' : "form-control"}),
               'Name': forms.TextInput(attrs={'class' : "form-control"}), 
               'Mathematics_Marks': forms.NumberInput(attrs={'id':"Maths",'name':'Maths','placeholder':"Mathematics Marks",'type':'number','class':"form-control prc"}), 
			'Physics_Marks': forms.NumberInput(attrs={'id':"Phy" , 'name':'Phy', 'placeholder' : "Physics Marks" , 'type':'number' , 'class' : "form-control prc"}), 
			'Chemistry_Marks': forms.NumberInput(attrs={'id':"Che" , 'name':'Che', 'placeholder' : "Chemistry Marks" , 'type':'number' , 'class' : "form-control prc"}),
               'Biology_Marks': forms.NumberInput(attrs={'id':"Bio" , 'name':'Bio', 'placeholder' : "Biology Marks" , 'type':'number' , 'class' : "form-control prc"}),
               'Computer_Marks': forms.NumberInput(attrs={'id':"Comp" , 'name':'Comp', 'placeholder' : "Computer Marks" , 'type':'number' , 'class' : "form-control prc"}),
               'English_Marks': forms.NumberInput(attrs={'id':"Eng" , 'name':'Eng', 'placeholder' : "English Marks" , 'type':'number' , 'class' : "form-control prc"}),
               'Hindi_Marks': forms.NumberInput(attrs={'id':"Hindi" , 'name':'Hindi', 'placeholder' : "Hindi Marks" , 'type':'number' , 'class' : "form-control prc"}),         
			'Total': forms.NumberInput(attrs={'id':'Total', 'class' : "form-control"}), 
               'Per': forms.NumberInput(attrs={'id':'Per', 'class' : "form-control"}),
          }

          
class art_marksform(forms.ModelForm):
	class Meta:
		model = art_marks
		fields = "__all__"
		widgets = {
               'Roll_no': forms.NumberInput(
                    attrs={'class' : "form-control"}),
               'Name': forms.TextInput(
                    attrs={'class' : "form-control"}), 
               'History_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}), 
               'Geography_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),
               'Political_science_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),           
			'Sociology_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),         
               'English_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),
               'Hindi_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),                    
               'Sanskrit_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),          
			'Total': forms.NumberInput(
                    attrs={'id':'Total', 'class' : "form-control"}), 
               'Per': forms.NumberInput(
                    attrs={'id':'Per', 'class' : "form-control"}),   	  	 	                        
        }

class commerce_marksform(forms.ModelForm):
	class Meta:
		model = commerce_marks
		fields = "__all__"
		widgets = {
               'Roll_no': forms.NumberInput(
                    attrs={'class' : "form-control"}),
               'Name': forms.TextInput(
                    attrs={'class' : "form-control"}), 
               'Accountancy_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}), 
               'Business_Studies_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}), 
			'Economics_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),
               'English_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),
               'Mathematics_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),     
               'Physical_Education_Marks': forms.NumberInput(
                    attrs={'class' : "form-control prc"}),                        
			'Total': forms.NumberInput(
                    attrs={'id':'Total', 'class' : "form-control"}), 
               'Per': forms.NumberInput(
                    attrs={'id':'Per', 'class' : "form-control"}),   	  	 	                        
        }                