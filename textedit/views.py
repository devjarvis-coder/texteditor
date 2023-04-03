from django.shortcuts import render

# Create your views here.
# I have created this file - aman
from django.shortcuts import render, redirect
from django.http import HttpResponse
import phonenumbers
import pywhatkit as pw
from phonenumbers import timezone, geocoder, carrier


def index(request):
    return render(request, 'index.html')


def numbertrack(request):
    if request.method == 'POST':
        number = request.POST['number']
        phone = phonenumbers.parse(number)
        time = timezone.time_zones_for_number(phone)
        car = carrier.name_for_number(phone, "en")
        reg = geocoder.country_name_for_number(phone, "en")
        return render(request, 'track.html', {'phone': phone, 'time': time, 'car': car, 'reg': reg})
    return render(request, 'track.html')


def txttohand(request):
    if request.method == 'POST':
        data = request.POST['texted']
        # txt = """In this Python handwriting project, you will learn how to convert text to handwriting. It is a basic project
        # that will help you with a better understanding of Python."""
        pw.text_to_handwriting(data, "demo1.png", [0, 0, 138])
        print(" End ")
        return render(request, 'track.html', )
    return render(request, 'txttohand.html')
