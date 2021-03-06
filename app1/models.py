from django.db import models
from django import views

class marks(models.Model):
	Roll_no = models.IntegerField()
	Name=models.CharField(max_length=30)
	Math_Marks = models.IntegerField()
	Physics_Marks = models.IntegerField()
	Chemistry_Marks = models.IntegerField()
	Total = models.IntegerField()
	Per = models.FloatField()

	
	def __str__(self):
		return "ID:{},Roll_no:{},Name:{}".format(self.pk,self.Roll_no,self.Name)




#  Create your models here.
