from django.shortcuts import render
from apps.settings.models import Settings
from apps.products.models import Product
from apps.category.models import Category
# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    products = Product.objects.all().filter(product_status = 'Активный').order_by('-id')
    categories = Category.objects.all()[:10]
    context = {
        'setting':setting,
        'products':products,
        'categories':categories,
    }
    return render(request, 'index.html', context)