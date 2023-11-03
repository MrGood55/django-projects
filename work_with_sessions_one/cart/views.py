from django.shortcuts import render,redirect
from app.models import Product
from decimal import Decimal
# Create your views here.


def index(request):
    cart = request.session.get('cart_products')
    print(f'len(cart) is {len(cart)}')
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
        # print(f'keys is {keys}')
        # print(f'cart for cart is {cart}')
        # print(f'products is {products}')
        print(f'cart.values is {cart}')
        context = {
            'products' : cart.values(),
            'sum' : sum

        }
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
    # print(f'cart is {cart}| item_pk is {item_pk}| ',product.id,product.title,product.price,product.img_url)
    return redirect('app:index')
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