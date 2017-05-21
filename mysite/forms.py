# This Python file uses the following encoding: utf-8
from django.forms import ModelForm
from .models import Image
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ImageForm(ModelForm):
	class Meta:
		model = Image
		fields = ('image', 'name', 'description')

class EditImageForm(ModelForm):
	class Meta:
		model = Image
		fields = ('name', 'description', 'date')