from django.shortcuts import render

def FirstPage (request):
    return render(request, 'index.html')

