
from django.contrib import admin
from django.urls import path, include

admin.site.site_header='Мой онлайн-магазин'
admin.site.site_title='Мой онлайн-магазин'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')), 
    
]
