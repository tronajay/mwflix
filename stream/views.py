from django.shortcuts import render

# Create your views here.
def platforms(request):
    return render(request,'stream/platforms.html')