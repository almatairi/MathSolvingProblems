from django.shortcuts import render, redirect
from .forms import RegisterUser
from django.contrib.auth import login
def viewUsers(request):
    
    context = {}
    return render(request, 'users/viewUsers.html',context)
def registUsr(request):
    form = RegisterUser
    if request.method == "post":
        form = registUsr(request.post)

    if form.is_valid() :
        user = form.save(commit=False)
        user.username=user.username.lower()
        user.save()
        login(request, user)
        return redirect("index")
        context = {
            "form" : form 
        }
    return render(request, 'users/registerUser.html', context)
