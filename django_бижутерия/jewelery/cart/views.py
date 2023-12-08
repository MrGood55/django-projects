from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView
from app.models import Product



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    print(request.session.get())
    cart = request.session.get('cart', {})
    
    # Добавляем продукт в корзину или увеличиваем количество, если он уже там
    current_quantity = cart.get(int(product_id), 0)
    print(current_quantity,type(current_quantity))
    cart[int(product_id)] = current_quantity + 1
    
    # Обновляем сессию с новой корзиной
    request.session['cart'] = cart
    request.session.modified = True
    print(request.session['cart'])
    return redirect('app:product_list')

# def add_to_cart(request, product_id):
#     if request.POST.get('action') == 'post':
#         cart_session = request.session.get('cart_products')
#         if cart_session.get(str(request.POST.get('id')), False) is False:
#             cart_session[str(request.POST.get('id'))] = {
#                 'quantity': 1
#             }
#         else:
#             cart_session[str(request.POST.get('id'))]['quantity'] = cart_session[str(request.POST.get('id'))]['quantity'] + 1
            
#         request.session.modified = True


def view_cart(request):
    # Получаем текущую корзину из сессии
    cart = request.session.get('cart', {})
    
    # Получаем информацию о продуктах в корзине
    cart_info = []
    for product_id, quantity in cart.items():
        product_info = {
            'product': get_object_or_404(Product, pk=product_id),
            'quantity': quantity,
        }
        cart_info.append(product_info)
    
    context = {'cart_info': cart_info}
    return render(request, 'cart/cart.html', context)
