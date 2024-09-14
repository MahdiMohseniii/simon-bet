from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


def FirstPage (request):
    return render(request, 'index.html')

def Login_user (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate( request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('main')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    else:
        return render(request, 'login.html')

def Logout_user (request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('home')

def signup_user (request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, ('Signup successful!'))
            return redirect("main")
        else:
            messages.error(request, ('There was an error with your signup. Please correct the form.'))
            return redirect("signup")
    
    else:
        return render(request, 'signup.html', {'form': form})
    
def about(request):
    return render(request, 'about.html')

def main(request):
    return render(request, 'main.html')

# *********************
# payment/views.py  
from django.shortcuts import render, redirect  
from django.http import JsonResponse  

def checkout(request):  
    return render(request, 'checkout.html')  

def create_payment(request):  
    if request.method == 'POST':  
        amount = request.POST.get('amount', 100)  # Default amount  
        # Simulate payment processing  
        return redirect('payment_success', amount=amount)  

    return redirect('checkout')  

def payment_success(request, amount):  
    return render(request, 'success.html', {'amount': amount})  

def payment_cancel(request):  
    return render(request, 'cancel.html')