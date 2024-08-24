from django.shortcuts import render,HttpResponse

# Create your views here.

def main(request):
    return HttpResponse("Hi this is the main page")