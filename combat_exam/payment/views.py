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