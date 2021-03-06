from django.shortcuts import render
from django.http import HttpResponse
from .forms import marksform
from .models import marks
# Create your views here.

def home(request):
	return render(request,'home.html')

def Marks(request):
	form = marksform()
	print(form)
	print(request.method)
	if request.method == "POST":
		form = marksform(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			print("successfully")
	context={'form':form}
	return render(request,'marks.html',context)

def leaderboard(request):
	Marks=marks.objects.all()
	print(Marks)
	return render(request,'leaderboard.html',{'Marks': Marks})

def search(request):
	query = request.GET['query']
	data = marks.objects.filter(Name__icontains=query)
	param={'data':data}
	return render(request,'search.html',param)
	#return Httparesponse('this is search')

	