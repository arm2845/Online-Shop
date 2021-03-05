from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
import json
from .utils import cookieCart, cartData
from users.models import Profile
from django.core.paginator import Paginator
from django.db.models import Q


def store(request):

    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


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


def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {'user': user}
    return render(request, 'store/user_profile.html', context)


def order_completed(request):
    data = cartData(request)
    order = data['order']
    items = data['items']
    cartItems = 0
    order = 0
    items = 0
    return render(request, 'store/order_completed.html', {'cartItems': cartItems, 'order': order,'items': items})


def searchposts(request):

    data = cartData(request)
    cartItems = data['cartItems']

    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups = Q(name__icontains=query) | Q(country__icontains=query)

            products = Product.objects.filter(lookups).distinct()

            context = {'products': products,
                     'submitbutton': submitbutton,
                       'cartItems': cartItems}

            return render(request, 'store/search.html', context)

        else:
            context = {'cartItems': cartItems}
            return render(request, 'store/search.html', context)

    else:
        return render(request, 'store/search.html')