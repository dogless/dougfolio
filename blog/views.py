import os
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
# Create your views here.


def home(request):
	return render(request, 'blog/index.html')

def contact(request):
	return render(request, 'blog/contact.html')

def resume(request):
	return render(request, 'blog/douglaschau.html')