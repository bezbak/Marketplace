from django.shortcuts import render
from apps.settings.models import Settings
# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    context = {
        'setting':setting
    }
    return render(request, 'index.html', context)