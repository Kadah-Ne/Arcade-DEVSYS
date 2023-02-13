from django.shortcuts import render

# Create your views here.
def pongchilling(request):
    return render(request, 'yes.html', {})