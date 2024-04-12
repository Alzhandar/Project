from django.contrib import admin
from .models import *
from django import forms
# Register your models here.

class ProductAdminForm(forms.ModelForm):
    desc=forms.CharField(widget=forms.Textarea(attrs={'rows':20,'cols':80}))
    class Meta:
        model=Product
        fields='__all__'

class ProductAdmin(admin.ModelAdmin):
    form=ProductAdminForm
    list_display=['name','price','desc','stock']
    list_filter=['price']
    search_fields=['name']
admin.site.register(Product,ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone']
    search_fields=['email']
admin.site.register(Customer,CustomerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category,CategoryAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=['product','quantity','customer']
admin.site.register(Order,OrderAdmin)
