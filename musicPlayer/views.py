from django.shortcuts import render

# Create your views here.
def getIndexPage(req):
    print("index page requested")
    return render(req, 'index.html')