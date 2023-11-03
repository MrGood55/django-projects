from django.shortcuts import render
from .models import Product
### thrird party libs
import requests
# Create your views here.


def index(request):
    cart = request.session.get('cart_products')
    if not cart:
        cart = request.session['cart_products'] = {}

    products = Product.objects.all()
    context = {'products':products}
    return render(request,'app/index.html',context)

def load(request):
    r = requests.get('https://fakestoreapi.com/products')
    # print(r.json())
    for item in r.json():
        product = Product(
            title = item['title'],
            description = item['description'],
            price = item['price'],
            img_url = item['image']
        )
        product.save()
    return render(request,'app/index.html')

def detail(request,item_pk):
    product = Product.objects.get(pk=item_pk)
    recently_viewed_products = None
    if 'recently_viewed' in request.session:
        if item_pk in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(item_pk)

        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products,
                                          key= lambda x: request.session['recently_viewed'].index(x.id)
                                          )
        request.session['recently_viewed'].insert(0,item_pk)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [item_pk]
    request.session.modified = True

    context = {
        'product':product,
        'recently_viewed_products':recently_viewed_products
    }
    return render(request,'app/detail.html',context)