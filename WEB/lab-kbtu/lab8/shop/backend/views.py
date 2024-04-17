from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.views import View
from django.http.response import JsonResponse

class AllProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        data = [{'name': product.name, 'description': product.desc, 'price': product.price} for product in products]
        return JsonResponse(data={'products': data})

class ProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        data = {'name': product.name, 'description': product.desc, 'price': product.price}
        return JsonResponse(data=data)

class AllCategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        data = [{'name': category.name} for category in categories]
        return JsonResponse(data={'categories': data})

class CategoryDetailView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        data = {'name': category.name}
        return JsonResponse(data=data)

class ProductsByCategoryView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = category.products.all()
        data = [{'name': product.name, 'description': product.desc, 'price': product.price} for product in products]
        return JsonResponse(data={'products': data})


# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'products/product_list.html', {'products': products})


# def product_detail(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     return render(request, 'products/product_detail.html', {'product': product})


# def category_detail(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
#     products = category.products.all()
#     return render(request, 'products/category_detail.html', {'category': category, 'products': products})


# def product_list(request):
#     search_query = request.GET.get('search_query', '')
#     if search_query:
#         products = Product.objects.filter(Q(name__icontains=search_query) | Q(desc__icontains=search_query))
#     else:
#         products = Product.objects.all()
#     return render(request, 'products/product_list.html', {'products': products})


# def category_detail(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
#     products = category.products.all()

#     price_min = request.GET.get('price_min')
#     price_max = request.GET.get('price_max')

#     if price_min:
#         products = products.filter(price__gte=price_min)
#     if price_max:
#         products = products.filter(price__lte=price_max)

#     return render(request, 'products/category_detail.html', {'category': category, 'products': products})

# def category_list(request):
#     categories = Category.objects.all()
#     return render(request, 'products/category_list.html', {'categories': categories})