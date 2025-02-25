from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages



def home(request):
    return render(request,"index.html")
    

def produce_view(request):
    return render(request,"produce.html")

def vegetable(request):
    return render(request,"vegetable.html")

def leafygreens(request):
    return render(request,"leafygreens.html")

def seasonalfruits(request):
    return render(request,"fruits.html")

def rootvegetables(request):
    return render(request,"rootvegetables.html")

def dairyproduct(request):
    return render(request,"dairyproducts.html")

def summer(request):
    return render(request,"summer.html")

def autumn(request):
    return render(request,"autumn.html")

def winter(request):
    return render(request,"winter.html")

def spring(request):
    return render(request,"spring.html")

# def farmer_login(request):
#     if request.method == 'POST':
#         # Get username and password from the form
#         username = request.POST['Username']
#         password = request.POST['Password']

#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             # If credentials are correct, log the user in
#             login(request, user)
#             # Redirect to the dashboard page
#             return redirect('farmer_dashboard')
#         else:
#             # If credentials are invalid, show an error message
#             return render(request, 'farmerlogin.html', {'error': 'Invalid username or password'})
#     else:
#         # Render the login page for GET requests
#         return render(request, 'farmerlogin.html')



def farmerlogin(request):
    return render(request,"farmerlogin.html")
    # return redirect('farmer_dashboard')

def customerlogin(request):
    return render(request,"customerlogin.html")


# def farmer_register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
        
#         print(f"Username: {username}, Password: {password}, Confirm Password: {confirm_password}")  # Debugging

#         # Check if passwords match
#         if password != confirm_password:
#             messages.error(request, "Passwords do not match.")
#             return redirect('farmerregister')

#         # Check if the username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken.")
#             return redirect('farmerregister')

#         # Create a new user
#         try:
#             user = User.objects.create_user(username=username, password=password)
#             user.save()
#             print(f"User created: {user}")  # Debugging
#             messages.success(request, "Registration successful. Please log in.")
#             return redirect('farmer_login')
#         except Exception as e:
#             print(f"Error creating user: {e}")  # Debugging
#             messages.error(request, "An error occurred during registration.")
#             return redirect('farmer_register')

#     return render(request, 'farmerregister.html')

def farmer(request):
    return render(request,"farmerregister.html")

def customer(request):
    return render(request,"customerregister.html")

from django.contrib.auth.decorators import login_required
@login_required
def farmer_dashboard(request):
    return render(request,"farmer_dashboard.html")

def customer_dashboard(request):
    return render(request,"customer_dashboard.html")