from django.shortcuts import render,redirect
from django.http import JsonResponse
from app.models import Product
from decimal import Decimal
# Create your views here.


def index(request):
    cart = request.session.get('cart_products')
    # print(f'len(cart) is {len(cart)}')
    if len(cart) >= 1:
        keys = list(cart.keys())
        products = Product.objects.filter(pk__in=keys)
        for product in products:
            cart[str(product.id)]['product'] = product
        sum = 0
        for item in cart.values():
            item['price'] = round(Decimal(item['product'].price),2)
            item['total'] = round(item['price']*item['quantity'],2)
            sum += item['total']
        # print(f'cart.values is {cart}')
        context = {
            'products' : cart.values(),
            'sum' : sum
        }


        print(f'sum is {context}')
        print(f'sum is {sum}')
    else:
        context = {

        }
    return render(request,'cart/cart.html',context)
def get_to_cart(request,item_pk):
    # product = Product.objects.get(pk=item_pk)
    cart = request.session.get('cart_products')
    if cart.get(str(item_pk),False) is False:
        cart[str(item_pk)] ={
            'quantity':1
        }
    else:
        cart[str(item_pk)]['quantity'] = cart[str(item_pk)]['quantity'] +1
    request.session.modified = True

    # return redirect('app:index')
    return JsonResponse({'data':cart,'items_in_cart': len(cart)})


def get_to_cart_for_btn(request):
    cart_session = request.session.get('cart_products')
    if cart_session.get(str(request.GET['id']), False) is False:
        cart_session[str(request.GET['id'])] = {
            'quantity': 1
        }
    else:
        cart_session[str(request.GET['id'])]['quantity'] = cart_session[str(request.GET['id'])]['quantity'] + 1

    request.session.modified = True




    return JsonResponse({'data':cart_session,'items_in_cart': len(cart_session)})
def clear_cart(request):
    request.session['cart_products'] = {}
    request.session.modified = True
    return redirect('cart:shopping_cart')
def plus_item(request,item_pk):
    cart = request.session.get('cart_products')
    if cart.get(str(item_pk),False) is False:
        cart[str(item_pk)] ={
            'quantity':1
        }
    else:
        cart[str(item_pk)]['quantity'] = cart[str(item_pk)]['quantity'] +1
    request.session.modified = True
    return redirect('cart:shopping_cart')
def minus_item(request,item_pk):
    cart = request.session.get('cart_products')
    if cart.get(str(item_pk),False) is not False:
        # print(f"quantity is {cart[str(item_pk)]['quantity']}")
        if int(cart[str(item_pk)]['quantity']) > 1:
            cart[str(item_pk)]['quantity'] = cart[str(item_pk)]['quantity'] -1
        else:
            cart.pop(str(item_pk))
    else:
        # print('wtf')
        pass

    request.session.modified = True
    return redirect('cart:shopping_cart')