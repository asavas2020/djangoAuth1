from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'user_example/index.html')

def special(request):
    return render(request, "user_example/special.html")


def register(request):
    form = UserCreationForm(request.POST or None)
    # form = UserCreationForm()
    # if request.metod == "POST":
    #     form = UserCreationForm(request.POST) # (request.POST or None) bu 3 satır kod yerine geçiyor
    if form.is_valid():
        form.save()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1") # password1 html den value olarak geliyo
        user = authenticate(username=username, password = password) 
        login(request, user) # bu 4 satır kod kullanıcının register olduktan sonra otomatik olarak ogin olmasını sağlar bunu yazmazsa kullanıcı tekrar login olması gerekir
        return redirect("home")

    context = {
        "form" : form
    }

    return render(request, "registration/register.html", context)