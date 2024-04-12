from django.shortcuts import render, get_object_or_404,redirect
from .models import Product, Category
from django.db.models import Q
from django.views import View
from django.http.response import JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .forms import ProductForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login


class AllProductsView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')  
        products = Product.objects.all()
        if search_query:
            products = products.filter(Q(name__icontains=search_query) | Q(desc__icontains=search_query))
        
        response = [
            {
                'name': product.name,
                'description': product.desc,
                'price': product.price
            } for product in products
        ]
        return JsonResponse(data={'response': response})


class ProductView(View):
    def get(self,request,product_id):
        product=Product.objects.filter(id=product_id).first()
        if not product:
            return JsonResponse(data={})
        product_dict={
                'name':product.name,
                'description':product.desc,
                'price':product.price,
                'stock':product.stock
        }
        return JsonResponse(data=product_dict) 


class CategoryProductView(View):
    def get(self, request, category_id):
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        products = Product.objects.filter(category_id=category_id)

        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

        response = [
            {
                'name': product.name,
                'description': product.desc,
                'price': product.price
            } for product in products
        ]
        return JsonResponse(data={'response': response})


class HomeTemplateView(TemplateView):
    template_name='products/home.html'

class ProductTemplateView(DetailView):
    model=Product
    template_name='products/product.html'
    context_object_name='product'

def product_template(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',context={
        "product":product
    })

class CategoryTemplateView(DetailView):
    model=Category
    template_name='products/category.html'
    context_object_name='category'

class ContactTemplateView(TemplateView):
    template_name='products/contact.html'

class AboutTemplateView(TemplateView):
    template_name='products/about.html'

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ProductForm()
    return render(request, 'products/add-product.html', {'form': form})


class ProductUpdateView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(instance=product)
        return render(request, 'products/edit_product.html', {'form': form, 'product_id': product_id})

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product_id)  
        return render(request, 'products/edit_product.html', {'form': form, 'product_id': product_id})
    
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')  

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home') 

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('profile') 


class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
        return render(request, 'registration/register.html', {'form': form})