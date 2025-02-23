from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import supabase
import environ
import database
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
            user=None
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            # return redirect('/register/')
            if user==None:
                return render(request,"signin.html")
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
        login(request,user)
        return render(request,"signupcontainer.html")
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
            return render(request,"businesslogic.html")

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

            # return JsonResponse({"message": "Business updated successfully"}, status=200)

    return render(request,"businesslogic.html")

@csrf_exempt
@login_required
def fetch_user_id(request):
    user=request.user
    user_id = user.id  # Get logged-in user's ID
    return JsonResponse({"userid":user_id})

@csrf_exempt
@login_required
def get_queue(request):
    user=request.user
    print(user.id)
    existing_business = supabase_client.table("BusinessDB").select("*").eq("busid", user.id).execute()
    print(existing_business.data[0]["name"])
    # if existing_business.data:
    # # Access the name column from the result
    #     business_name = existing_business.data["name"]
    #     print("Business Name:", business_name)
    try:
        names=database.mycuhzz(existing_business.data[0]["name"])
        print(names)
        return JsonResponse({"queue":names})
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({"message": "Error", "error": str(e)}, status=530)