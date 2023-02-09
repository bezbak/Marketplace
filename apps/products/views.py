from django.shortcuts import render, redirect
from apps.products.models import Product, Currency
from apps.category.models import Category
from apps.settings.models import Settings
from django.http import HttpResponseRedirect

# Create your views here.
def create_product(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    setting = Settings.objects.latest('id')
    currency = Currency.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        price = request.POST.get('price')
        curr = request.POST.get('currency')
        category = request.POST.get('category')
        try:
            product = Product.objects.create(title = title, image = image, description = description, price = price, currency_id = curr, category_id = category, owner = request.user)
            product.save()
            return redirect('index')
        except:
            return redirect('create_product')
    context = {
        'setting':setting,
        'currency':currency,
        'categories':categories,
    }
    return render(request, 'products/upload-work.html', context)

def product_detail(request, id):
    product = Product.objects.get(id = id)
    setting = Settings.objects.latest('id')
    context = {
        'setting': setting,
        'product': product,
    }
    return render(request, 'products/item-detail-one.html', context)

def product_update(request, id):
    product = Product.objects.get(id=id)
    if not request.user.is_authenticated and request.user != product.owner:
        return HttpResponseRedirect("/")
    setting = Settings.objects.latest('id')
    currency = Currency.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        price = request.POST.get('price')
        curr = request.POST.get('currency')
        category = request.POST.get('category')
        # try:
        product = Product.objects.get(id=id)
        product.title = title
        product.image = image
        product.description = description
        product.price = price
        product.currency.id = curr
        product.category.id = category
        product.save()
        return redirect('product_detail', product.id)
        # except:
        #     return redirect('product_update', product.id)
    context = {
        'setting': setting,
        'product': product,
        'currency':currency,
        'categories':categories,
    }
    return render(request, 'products/product_update.html', context)

def product_delete(request, id):
    if not request.user.is_authenticated and request.user != product.owner:
        return HttpResponseRedirect("/")
    product = Product.objects.get(id=id)
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        if 'yes' in request.POST:
            product.delete()
            return redirect('index')
        if 'no' in request.POST:
            return redirect('product_detail', product.id)
    context = {
        'setting': setting,
        'product': product,
    }
    return render(request, 'products/product_delete.html', context)