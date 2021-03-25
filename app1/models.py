from django.db import models
from django import views

class marks(models.Model):
	Roll_no = models.IntegerField(unique=True)
	Name=models.CharField(max_length=30)
	Math_Marks = models.IntegerField()
	Physics_Marks = models.IntegerField()
	Chemistry_Marks = models.IntegerField()
	Total = models.IntegerField()
	Per = models.FloatField()

	
	def __str__(self):
		return "ID:{},Roll_no:{},Name:{}".format(self.pk,self.Roll_no,self.Name)

class sci_marks(models.Model):
	Roll_no = models.IntegerField(unique=True)
	Name=models.CharField(max_length=30)
	Physics_Marks = models.IntegerField()
	Chemistry_Marks = models.IntegerField()
	Mathematics_Marks = models.IntegerField(null=True,blank=True)
	Biology_Marks = models.IntegerField(null=True,blank=True)
	Computer_Marks = models.IntegerField(null=True,blank=True)
	English_Marks = models.IntegerField()
	Hindi_Marks = models.IntegerField()
	Total = models.IntegerField()
	Per = models.FloatField()

	
	def __str__(self):
		return "ID:{},Roll_no:{},Name:{}".format(self.pk,self.Roll_no,self.Name)

class art_marks(models.Model):
	Roll_no = models.IntegerField(unique=True)
	Name=models.CharField(max_length=30)
	History_Marks = models.IntegerField()
	Geography_Marks = models.IntegerField()
	Political_science_Marks = models.IntegerField()
	Sociology_Marks = models.IntegerField()
	English_Marks = models.IntegerField(null=True,blank=True)
	Hindi_Marks = models.IntegerField(null=True,blank=True)
	Sanskrit_Marks = models.IntegerField(null=True,blank=True)
	Total = models.IntegerField()
	Per = models.FloatField()

	
	def __str__(self):
		return "ID:{},Roll_no:{},Name:{}".format(self.pk,self.Roll_no,self.Name)

class commerce_marks(models.Model):
	Roll_no = models.IntegerField(unique=True)
	Name=models.CharField(max_length=30)
	Accountancy_Marks = models.IntegerField()
	Business_Studies_Marks = models.IntegerField()
	Economics_Marks = models.IntegerField()
	English_Marks = models.IntegerField()
	Mathematics_Marks = models.IntegerField()
	Physical_Education_Marks = models.IntegerField(null=True,blank=True)
	Total = models.IntegerField()
	Per = models.FloatField()

	
	def __str__(self):
		return "ID:{},Roll_no:{},Name:{}".format(self.pk,self.Roll_no,self.Name)						




#  Create your models here.
