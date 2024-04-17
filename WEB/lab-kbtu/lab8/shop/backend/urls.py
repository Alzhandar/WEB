from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.AllProductsView.as_view(), name='products'),
    path('products/<int:product_id>/', views.ProductView.as_view(), name='product_detailed'),
    path('categories/', views.AllCategoriesView.as_view(), name='categories'),
    path('categories/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:category_id>/products/', views.ProductsByCategoryView.as_view(), name='category_products'),
]
    # path('', views.product_list, name='product_list'),
    # path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    # path('products/category/<int:category_id>/', views.category_detail, name='category_detail'),
    # path('categories/', views.category_list, name='category_list'),

