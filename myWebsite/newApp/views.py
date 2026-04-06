from django.shortcuts import render, get_object_or_404
from .models import Product, Feedback

def app(request):
    products = Product.objects.all()
    return render(request, 'newApp/app.html', {'products': products})

def about(request):
    return render(request, 'newApp/about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            Feedback.objects.create(name=name, email=email, subject=subject, message=message)
            success = True
    return render(request, 'newApp/contact.html', {'success': success})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'newApp/product_detail.html', {'product': product})
