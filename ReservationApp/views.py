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
def business_logic(request):
    return render(request,"businesslogic.html")
def customer_options(request):
    return render(request,"Customeroptions.html")
def reservation_search(request):
    return render(request,"ReservationSearch.html")
def reserve_form(request):
    return render(request,"ReserveForm.html")
def confirmation(request):
    return render(request,"Confirmation.html")