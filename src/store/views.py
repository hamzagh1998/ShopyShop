from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import logout
import json

from .models import Product, OrderItem, ShippingAddress
from .forms import ProductForm

def index(request):
    products = Product.objects.all()

    if request.POST:
        filter_value = request.POST['filter']
        if filter_value != 'All':
            products = Product.objects.filter(category=filter_value)

    return render(request, 'store/index.html', {'products': products})

def cartView(request):
    return render(request, 'store/cart.html')

def shippingDataView(request):
    shipping = ShippingAddress.objects.last()
    products = shipping.orderitem_set.all()
    return render(request, 'store/shippingData.html', {'shipping':shipping, 'products':products})

@csrf_exempt # Disable the csrf_token
def getValidation(request): # Validate the data that comes from AJAX
    costumerData, productsData = json.loads(request.body)[0], json.loads(request.body)[1]
    total = 0
    if costumerData[0] == None: return JsonResponse('invalid inputs', safe=False)
    ShippingAddress.objects.create(name=costumerData[0], phone=costumerData[1], address=costumerData[2], city=costumerData[3], state=costumerData[4], zipcode=costumerData[5])
    for i in range(len(productsData)):
        product = get_object_or_404(Product, id=productsData[i]['productId'])
        if productsData[i]['quantity'] < 0 or product.quantity < productsData[i]['quantity']:
            return JsonResponse('quantity out of range', safe=False)
        else:
            OrderItem.objects.create(shippingaddress=ShippingAddress.objects.last(), quantity=productsData[i]['quantity'], product=product)
            total += productsData[i]['quantity'] * product.price
            product.quantity -= productsData[i]['quantity']
            product.save()
    return JsonResponse(total, safe=False)

def productFormView(request):
    if not request.user.is_staff:
        return redirect('index')

    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'store/productForm.html', {'form':form})

def updateProductFormView(request, id):
    if not request.user.is_staff:
        return redirect('index')

    product = get_object_or_404(Product, id=id)
    if product.owner != request.user:
        return HttpResponse('This is not your product!')

    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    # else initiate filling the form with the product data
    form = ProductForm(initial={
        'category':product.category,
        'name':product.name,
        'quantity':product.quantity,
        'description':product.description,
        'image':product.image,
        'price':product.price,
    })
    return render(request, 'store/updateProductForm.html', {'form':form})

def deleteProduct(request, id):
    if not request.user.is_staff:
        return redirect('index')

    get_object_or_404(Product, id=id).delete()
    return redirect('index')


def shippingView(request):
    if not request.user.is_staff:
        return redirect('index')

    shippings = ShippingAddress.objects.all()

    if request.POST:
        filter_val = request.POST['filter']
        if filter_val  == 'True':
            print('shipped')
            shippings = ShippingAddress.objects.filter(shipped=True)
        elif filter_val  == 'False':
            print('Unshipped')
            shippings = ShippingAddress.objects.filter(shipped=False)

    return render(request, 'store/customersRequestes.html', {'shippings':shippings})

def orderListView(request, id):
    if not request.user.is_staff:
        return redirect('index')

    shipping = get_object_or_404(ShippingAddress, id=id)

    if request.POST:
        checkbox_value = request.POST.get('shipping')
        if bool(checkbox_value) == False:
            shipping.shipped = True
            shipping.save()
        elif bool(checkbox_value) == True:
            print('done')
            shipping.shipped = False
            shipping.save()

    return render(request, 'store/orederDetail.html', {'shipping': shipping, 'shippings': shipping.orderitem_set.all()})


def logOut(request):
    logout(request)
    return redirect('index')
