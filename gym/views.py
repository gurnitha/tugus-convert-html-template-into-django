from django.shortcuts import render

# Create your views here.


def home_view(request):
	return render(request, "gym/index.html")


def why_view(request):
	return render(request, "gym/why.html")