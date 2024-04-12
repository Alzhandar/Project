from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('product/<int:pk>/', ProductTemplateView.as_view(), name='product'),
    path('category/<int:pk>/', CategoryTemplateView.as_view(), name='category'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path("products/", AllProductsView.as_view(), name='products'),
    path("products/<int:product_id>/", ProductView.as_view(), name='product_detail'),
    path("products/category/<int:category_id>/", CategoryProductView.as_view(), name='category_product'),
    path('add/', add_product, name='add_product'),
    path('product/<int:product_id>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/profile/', user_profile, name='profile'),
    path('profile/change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
]
