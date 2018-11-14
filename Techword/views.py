from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
	return redirect('/')

def profile(request):
	return redirect('/')