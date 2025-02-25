from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import FarmerRegistrationForm, CustomerRegistrationForm
from .models import farmerprofile, Customerprofile
import traceback

# Create your views here.



# def farmer(request):
#     if request.method == 'POST':
#         form = FarmerRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(f"Farmer saved: {farmer}")  # Debugging
#             return redirect('farmer_dashboard')  # Redirect to a success page
#     else:
#         form = FarmerRegistrationForm()
#     return render(request, 'farmerregister.html', {'form': form})

# def farmer(request):
#     if request.method == 'POST':
#         name = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         farm_location = request.POST.get('farm_location')
#         farm_size = request.POST.get('farm_size')
#         crops_produced = request.POST.get('crops_produced')
        
#         en = FarmerRegistrationForm(name=name,farm_location=farm_location,farm_size=farm_size,crops_produced=crops_produced,email=email,password=password)
#         en.save()


        # Check if passwords match
        # if password != confirm_password:
        #     messages.error(request, "Passwords do not match.")
        #     return redirect('farmer')

        # # Check if the username or email already exists
        # if User.objects.filter(name=name).exists():
        #     messages.error(request, "Username already taken.")
        #     return redirect('farmer')
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Email already registered.")
        #     return redirect('farmer')

        # # Create a new user
        # try:
        #     user = User.objects.create_user(name=name, email=email, password=password)
        #     user.save()

        #     # Create a FarmerProfile for the user
        #     farmer.objects.create(
        #         user=user,
        #         farm_location=farm_location,
        #         farm_size=farm_size,
        #         crops_produced=crops_produced
        #     )

        #     messages.success(request, "Registration successful. Please log in.")
        #     return redirect('farmerlogin')
        # except Exception as e:
        #     messages.error(request, f"An error occurred: {e}")
        #     return redirect('farmer')

    # return render(request, 'farmerregister.html')
    
    


def farmer(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            farm_location = request.POST.get('farm_location')
            farm_size = request.POST.get('farm_size')
            crops_produced = request.POST.get('crops_produced')

            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return redirect('farmer')

            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            farmer = farmerprofile(
                user=user,

                name=name,
                email=email,
                farm_location=farm_location,
                farm_size=farm_size,
                crops_produced=crops_produced
            )
            farmer.password = make_password(password)

            farmer.save()  # Save the farmer profile after linking to the user


            messages.success(request, "Farmer registered successfully! Please log in.")
            messages.info(request, f"Registered farmer: {name}, Email: {email}")  # Debugging output

            print("Farmer registration successful.")  # Debugging output

            return redirect('farmerlogin')

            

        except Exception as e:
            print("Error during farmer registration:", str(e))  # Debugging output
            messages.error(request, "Registration failed due to an error. Please try again.")  # User-friendly error message


            import traceback
            print(f"Error during farmer registration: {str(e)}")
            print("Traceback:")
            print(traceback.format_exc())
            
            # Show user-friendly error message
            messages.error(request, f"Registration failed: {str(e)}")
            return render(request, 'farmerregister.html')

    return render(request, 'farmerregister.html')
    



def customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')  # Redirect to a success page
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customerregister.html', {'form': form})
