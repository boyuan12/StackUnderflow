from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, email=email, password=password)

        return redirect("/")

    else:
        return render(request, "auth/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("login unsuccessfully")
            return render(request, "auth/login.html", {"error": "Invalid username and password"})

    else:
        return render(request, "auth/login.html")

def logout_view(request):
    logout(request)
    return redirect("/")

