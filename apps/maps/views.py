from django.shortcuts import render

# Create your views here.

def event_maps(request):
	return render(request, 'maps/index.html')