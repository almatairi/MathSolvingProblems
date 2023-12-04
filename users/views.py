from django.shortcuts import render

def viewUsers(request):
    
    context = {}
    return render(request, 'users/viewUsers.html',context)
