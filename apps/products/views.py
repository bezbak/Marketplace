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
    return render(request, 'upload-work.html', context)