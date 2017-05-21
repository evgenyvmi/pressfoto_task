# This Python file uses the following encoding: utf-8
from django.shortcuts import render
from .search import generic_search, perform_search
import re
import operator
from functools import reduce
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.db.models import Q, query
# Create your views here.    

def main_page(request):
	return render(request, 'Images/main_page.html')

def new_image(request):
	if request.method == 'POST':
		print('In POST')
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			print('hello')
			new_iamge = form.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/')
	else:
		form = ImageForm()
	return render(request, 'Images/new_image.html', {'form': form})

def full_image(request, image_id):
	image = Image.objects.get(id= image_id)
	return render(request, 'Images/full_image.html', {'image': image})

def images(request):
	images = Image.objects.all()
	return render(request, 'Images/images.html', {'images': images})

def image(request, image_id):
	image = Image.objects.get(id= image_id)
	if request.method == 'POST':
		image.delete()
		return HttpResponseRedirect('http://127.0.0.1:8000/images')
	else:
		return render(request, 'Images/image.html', {'image': image, 'image_id': image_id})

def edit_image(request, image_id):
	image = Image.objects.get(id= image_id)
	if request.method == 'POST':
		image.name = request.POST.get('name', '')
		image.description = request.POST.get('description', '')
		image.date = request.POST.get('date', '')
		image.save(update_fields=['description', 'date', 'name'])
		return HttpResponseRedirect('http://127.0.0.1:8000/images/' + image_id + '/')
	else:
		form = EditImageForm()
		return render(request, 'Images/edit.html', {'form':form, 'image':image.image})

def search(request):
	objects = []
	objects = generic_search(request, Image, ("name", "description"))
	return render(request, "Images/search_results.html", {"objects": objects,"search_string": request.GET.get('q', ""),})

