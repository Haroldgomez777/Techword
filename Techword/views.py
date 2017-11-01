from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect

def profile(request):
	return redirect('/')