from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import supabase
import environ
# Create your views here.

env=environ.Env()
supabase_client = supabase.create_client( # type: ignore
    env("SUPABASE_URL"),
    env("SUPABASE_KEY")  # Supabase API Key
)

@csrf_exempt
def signup(request):
    if request.method=="POST":
        print(request.POST)
        userName = request.POST.get('username',"")
        code = request.POST.get('password',"")
        # user = User.objects.exists(username=userName)
        if User.objects.filter(username=userName).exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            # return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            username=userName,
            password=code
        )
        data = {
            "username": userName,
            "busid": user.id,  # Linking Django user ID with Supabase

        }
        response = supabase_client.table("BusinessDB").insert(data).execute()

        # if response.get("error"):
        #     messages.error(request, "Failed to register user in Supabase!")
    
            # return redirect('/register/')  

        messages.success(request, "Account created successfully!")
        # return redirect('http://127.0.0.1:5500/Sample1.html')
        # print(user)
        # Set the user's password and save the user object
        # user.set_password(password)
        user.save()
        return HttpResponse(status=201)
        # return JsonResponse({'status': 'success', 'message': 'User created or updated successfully.'})    
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return JsonResponse({'status': 'Failure', 'message': 'Password was wrong'})    
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return HttpResponse(status=201)

@csrf_exempt
@login_required
def business_signup(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        addr = request.POST.get('address', "")
        seats = request.POST.get('capacity', 0)
        type = request.POST.get('type', "")

        user = request.user 

        existing_business = supabase_client.table("BusinessDB").select("busid").eq("busid", user.id).execute()

        if existing_business.data:
            response = supabase_client.table("BusinessDB").update({
                "name": name,
                "address": addr,
                "capacity": int(seats),
                "type": type,
            }).eq("busid", user.id).execute()

            if "error" in response:
                return JsonResponse({"error": "Failed to update business"}, status=500)

            return JsonResponse({"message": "Business updated successfully"}, status=200)

    return HttpResponse(status=204) 
