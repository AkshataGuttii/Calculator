from django.shortcuts import render

# Create your views here.
def details(request):
    user = "akshata"
    return render(request, 'calculater.html')