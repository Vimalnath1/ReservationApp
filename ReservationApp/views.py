from django.shortcuts import render

def my_view(request):
    return render(request, 'main.html')
def first_page(request):
    return render(request,"Businessoptions.html")
def sign_in(request):
    return render(request,"signin.html")
def sign_up(request):
    return render(request,"signup.html")
def sign_up_container(request):
    return render(request,"signupcontainer.html")