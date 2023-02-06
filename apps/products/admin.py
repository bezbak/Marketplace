from django.contrib import admin
from apps.products.models import Product, Currency
from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'owner', 'price', 'currency', 'product_status', 'category', 'get_image2')
    list_display_links = ('title', 'id')
    list_editable = ('product_status',)
    list_filter = ('category__name', 'product_status')
    readonly_fields = ('get_image',)
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width="300" height="200">')
    
    def get_image2(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width="100" height="50">')
    
    get_image.short_description = "Image"
    get_image2.short_description = "Image"
admin.site.register(Currency)