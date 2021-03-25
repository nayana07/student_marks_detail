from django.shortcuts import render
from django.http import HttpResponse
from .forms import marksform, sci_marksform, art_marksform, commerce_marksform
from .models import marks, sci_marks, art_marks, commerce_marks
# Create your views here.

def home(request):
	return render(request,'home.html')

def sci(request):
	return render(request,'sci.html')
	
def scicence_marks(request):
	thank = False
	form = sci_marksform()
	if request.method == "POST":
		form = sci_marksform(request.POST)
		if form.is_valid():
			form.save()
			thank = True
			print("successfully")
		else:
			print(form.errors)	
	context={'form':form, 'thank':thank}
	return render(request,'sci_marks.html',context)

def science_leaderboard(request):
	Marks = sci_marks.objects.all()
	return render(request,'sci_leaderboard.html',{'Marks': Marks})		

def sci_search(request):
	if request.method == 'POST':
		query = request.POST.get('query','')
		data = sci_marks.objects.filter(Name__icontains=query)
		param={'data':data}
		return render(request,'sci_search.html',param)
	return render(request,'sci_search.html')	

def art(request):
	return render(request,'art.html')

def arts_marks(request):
	thank = False
	form = art_marksform()
	if request.method == "POST":
		form = art_marksform(request.POST)
		if form.is_valid():
			form.save()
			thank = True
			print("successfully")
		else:
			print(form.errors)	
	context={'form':form, 'thank':thank}
	return render(request,'art_marks.html',context)	

def art_leaderboard(request):
	Marks = art_marks.objects.all()
	return render(request,'art_leaderboard.html',{'Marks': Marks})	

def art_search(request):
	if request.method == 'POST':
		query = request.POST.get('query','')
		print(query)
		data = art_marks.objects.filter(Name__icontains=query)
		print(data)
		param={'data':data}
		return render(request,'art_search.html',param)
	return render(request,'art_search.html')	

def commerce(request):
	return render(request,'commerce.html')

def com_marks(request):
	thank = False
	form = commerce_marksform()
	if request.method == "POST":
		form = commerce_marksform(request.POST)
		if form.is_valid():
			form.save()
			thank = True
			print("successfully")
		else:
			print(form.errors)	
	context={'form':form, 'thank':thank}
	return render(request,'commerce_marks.html',context)					

def commerce_leaderboard(request):
	Marks = commerce_marks.objects.all()
	return render(request,'commerce_leaderboard.html',{'Marks': Marks})	

def commerce_search(request):
	if request.method == 'POST':
		query = request.POST.get('query','')
		data = commerce_marks.objects.filter(Name__icontains=query)
		param={'data':data}
		return render(request,'commerce_search.html',param)
	return render(request,'commerce_search.html')		
	#return Httparesponse('this is search')

	