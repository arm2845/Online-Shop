from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
import json
from .utils import cartData
from users.models import Profile
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


def store(request):

    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page') # returns the current page number
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'cartItems': cartItems}

    if request.method == 'POST':
        query = request.POST.get('q')

        if query is not None:
            lookups = Q(name__icontains=query) | Q(country__icontains=query) # Q is used to search in multiple columns of database

            products = Product.objects.filter(lookups).distinct() # distinct is used to avoid duplicates
            paginator = Paginator(products, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {'products': products, 'cartItems': cartItems, 'page_obj': page_obj}

            return render(request, 'store/store.html', context)

        else:

            return render(request, 'store/store.html', context)

    return render(request, 'store/store.html', context)


def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


@login_required()
def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


@login_required()
def confirm(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    profile = Profile.objects.get(user=request.user.id)
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'profile': profile}

    return render(request, 'store/confirm_order.html', context)


def view_product(request, pk):
    data = cartData(request)
    cartItems = data['cartItems']
    product = get_object_or_404(Product, pk=pk)
    context = {'cartItems': cartItems, 'product': product}
    return render(request, 'store/view.html', context)


@login_required()
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {'user': user}
    return render(request, 'store/user_profile.html', context)


@login_required()
def order_completed(request):
    data = cartData(request)
    order = data['order']
    cartItems = 0
    items = data['items']
    order.complete = True
    order.save()
    message = 'Your order was confirmed. Thank you for choosing us. Regards Wineshop administration.'
    profile = Profile.objects.get(user=request.user.id)
    email = profile.email
    send_mail('Order confirmation', message, 'thebestonlineshopever@gmail.com', [email], fail_silently=False)


    return render(request, 'store/order_completed.html', {'order': order, 'cartItems': cartItems, 'items': items})


