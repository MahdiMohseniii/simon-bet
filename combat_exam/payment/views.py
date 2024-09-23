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


# ***|pay pall|***
# views.py  
# from django.shortcuts import render, redirect  
# from django.conf import settings  
# from paypalrestsdk import Payment  
# import paypalrestsdk  

# # Configure PayPal SDK  
# paypalrestsdk.configure({  
#     "mode": settings.PAYPAL_MODE,  
#     "client_id": settings.PAYPAL_CLIENT_ID,  
#     "client_secret": settings.PAYPAL_CLIENT_SECRET  
# })  

# def checkout(request):  
#     return render(request, 'checkout.html')  

# def create_payment(request):  
#     if request.method == 'POST':  
#         payment = Payment({  
#             "intent": "sale",  
#             "payer": {  
#                 "payment_method": "paypal"  
#             },  
#             "redirect_urls": {  
#                 "return_url": request.build_absolute_uri('/payment/success/'),  
#                 "cancel_url": request.build_absolute_uri('/payment/cancel/')  
#             },  
#             "transactions": [{  
#                 "item_list": {  
#                     "items": [{  
#                         "name": "Item Name",  
#                         "sku": "item",  
#                         "price": "10.00",  
#                         "currency": "USD",  
#                         "quantity": 1  
#                     }]  
#                 },  
#                 "amount": {  
#                     "total": "10.00",  
#                     "currency": "USD"  
#                 },  
#                 "description": "This is the payment description."  
#             }]  
#         })  

#         if payment.create():  
#             print("Payment created successfully")  
#             for link in payment.links:  
#                 if link.rel == "approval_url":  
#                     return redirect(link.href)  
#         else:  
#             print(payment.error)  

#     return redirect('checkout')  

# def payment_success(request):  
#     return render(request, 'success.html')  

# def payment_cancel(request):  
#     return render(request, 'cancel.html')