from django.shortcuts import render,redirect
from django.http import JsonResponse
from app.models import Product
from decimal import Decimal
# Create your views here.


def index(request):
    
    cart = request.session.get('cart_products')
    if len(cart) >= 1:
        keys = list(cart.keys())
        products = Product.objects.filter(pk__in=keys)
        for product in products:
            cart[str(product.id)]['id'] = product.id
            cart[str(product.id)]['title'] = product.title
            cart[str(product.id)]['img_url'] = product.img_url
            cart[str(product.id)]['price'] = round(float(product.price),2)
            

        sum = 0
        for item in cart.values():
            # item['price'] = round(Decimal(item['price']),2)
            item['total'] = round(item['price']*item['quantity'],2)
            sum += item['total']
        # sum = round(sum,2)
        # cart['sum'] = sum
        
        request.session.modified = True
        
        context = {
            'products' : cart.values(),
            'sum' : sum
        }


        # print(f'sum is {context}')
        # print(f'sum is {sum}')
    else:
        context = {

        }
    return render(request,'cart/cart.html',context)
def get_to_cart(request,item_pk):
    
    
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
    if request.POST.get('action') == 'post':
        cart_session = request.session.get('cart_products')
        if cart_session.get(str(request.POST.get('id')), False) is False:
            cart_session[str(request.POST.get('id'))] = {
                'quantity': 1
            }
        else:
            cart_session[str(request.POST.get('id'))]['quantity'] = cart_session[str(request.POST.get('id'))]['quantity'] + 1
            
        request.session.modified = True

        return JsonResponse({'data':cart_session,'items_in_cart': len(cart_session)})
    else:
        return JsonResponse({})

        
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
    # return redirect('cart:shopping_cart')
    return JsonResponse({'data':cart})



def plus_item_btn(request):
    if request.POST.get('action') == 'post':
        cart_session = request.session.get('cart_products')
        cart_session[str(request.POST.get('id'))]['quantity'] = cart_session[str(request.POST.get('id'))]['quantity'] + 1
            
    request.session.modified = True

    return JsonResponse({'data':cart_session})



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