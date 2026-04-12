from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import User, Product, Order

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('products')
            else:
                error = 'Incorrect username or password.'
        except User.DoesNotExist:
            error = 'Incorrect username or password.'
    return render(request, 'hello_world/login.html', {'error': error})


def products_view(request):
    if not request.session.get('user_id'):
        return redirect('login')
    products = Product.objects.all()
    return render(request, 'hello_world/products.html', {'products': products})


def buy_view(request, product_id):
    if not request.session.get('user_id'):
        return redirect('login')
    product = get_object_or_404(Product, id=product_id)
    user    = get_object_or_404(User, id=request.session['user_id'])
    order   = Order.objects.create(user=user, product=product, cost=product.cost)
    return render(request, 'hello_world/order_confirmation.html', {
        'order':   order,
        'product': product,
        'user':    user,
    })


def logout_view(request):
    request.session.flush()
    return redirect('login')