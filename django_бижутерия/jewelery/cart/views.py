from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView
from app.models import Product,Category
from django.views import View
from app.models import OrderItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    
    cart = request.session.get('cart', {})
    
    # Добавляем продукт в корзину или увеличиваем количество, если он уже там
    if str(product_id) in list(cart.keys()):
        print(cart)
        cart[str(product_id)]['quantity'] = cart[str(product_id)]['quantity'] + 1
    else:
        print(cart)
        cart[str(product_id)] =  {'quantity':1}

    
    # Обновляем сессию с новой корзиной
    request.session.modified = True
    return redirect('app:product_list')

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    
    return redirect('app:product_list')

def delete_categorie(request, cat_id):
    product = get_object_or_404(Category, pk=cat_id)
    product.delete()
    return redirect('app:product_list')

def add_to_cart_in_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    
    cart = request.session.get('cart', {})
    
    # Добавляем продукт в корзину или увеличиваем количество, если он уже там
    if str(product_id) in list(cart.keys()):
        print(cart)
        cart[str(product_id)]['quantity'] = cart[str(product_id)]['quantity'] + 1
    else:
        cart[str(product_id)] =  {'quantity':1}

    # Обновляем сессию с новой корзиной
    request.session.modified = True
    return redirect('cart:view_cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    
    cart = request.session.get('cart', {})
    
    # Добавляем продукт в корзину или увеличиваем количество, если он уже там
    if str(product_id) in list(cart.keys()) and cart[str(product_id)]['quantity'] > 1:
        print(cart)
        cart[str(product_id)]['quantity'] = cart[str(product_id)]['quantity'] - 1
    elif str(product_id) in list(cart.keys()) and cart[str(product_id)]['quantity'] == 1:
        cart.pop(str(product_id))

    # Обновляем сессию с новой корзиной
    request.session.modified = True
    return redirect('cart:view_cart')

def remove_from_cart_in_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    
    cart = request.session.get('cart', {})
    
    # Добавляем продукт в корзину или увеличиваем количество, если он уже там
    if str(product_id) in list(cart.keys()) and cart[str(product_id)]['quantity'] > 1:
        print(cart)
        cart[str(product_id)]['quantity'] = cart[str(product_id)]['quantity'] - 1
    elif str(product_id) in list(cart.keys()) and cart[str(product_id)]['quantity'] == 1:
        cart.pop(str(product_id))

    # Обновляем сессию с новой корзиной
    request.session.modified = True
    return redirect('cart:view_cart')



def view_cart(request):
    # Получаем текущую корзину из сессии
    cart = request.session.get('cart', {})
    
    # Получаем информацию о продуктах в корзине
    cart_info = []
    for product_id, data in cart.items():
        product_info = {
            'product': get_object_or_404(Product, pk=product_id),
            'quantity': data['quantity'],
            'price': get_object_or_404(Product, pk=product_id).price,    
        }
        cart_info.append(product_info)
    full_price = 0

    for _, data in cart.items():
        full_price+= data['quantity'] * get_object_or_404(Product, pk=product_id).price

    context = {'cart_info': cart_info,'full_price':full_price}
    # context = {'cart_info': cart_info}
    return render(request, 'cart/cart.html', context)




def get_session_go_to_order_and_clear(request):
    # Получение  сессии 
    cart = request.session.get('cart')
    if not cart:
        print('В корзине пусто')
    else:
        print(cart)
        for key,data_from_cart_item in cart.items():
            product = Product.objects.get(pk=int(key))
            OrderItem.objects.create(
                user=request.user,
                product=product,
                price=product.price,
                quantity=data_from_cart_item['quantity']
            )
        # Clear the cart in the session
        request.session['cart'] = {}

    # return render(request, 'cart/cart.html')
    return redirect('cart:order_page')

def order_for_klient_delete(request, pk):
    order = get_object_or_404(OrderItem, pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('cart:order_page')

    return render(request, 'cart/order_page.html', {'order': order})




class OrderPageView(View):
    template_name = 'cart/order_page.html'

    def get(self, request):
        # Get orders for the current user
        orders = OrderItem.objects.filter(user=request.user)

        context = {
            'orders': orders,
        }

        return render(request, self.template_name, context)
