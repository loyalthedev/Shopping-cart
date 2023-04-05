from django.contrib import admin
# from .models import Brand
from .models import Headphones

# Register your models here.


@admin.register(Headphones)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description', 'price')
    list_display_links = ('id',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_editable = ('name', 'description', 'price')
