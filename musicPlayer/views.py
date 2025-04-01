from django.shortcuts import render

# Create your views here.
def getIndexPage(req):
    print("index page requested")
    return render(req, 'index.html')

def gotoUserPage(req):
    data = req.POST
    username = data.get("username")
    email = data.get("email")
    print(f"User {username} requested")
    print(f"User {email} requested")
    return render(req, 'user.html')