from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductImeges


def shop(request):
    products = Product.objects.all().order_by('-uploaded_at')
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/shop.html', context)


def category(request, slug):
    category_obj = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category_obj).order_by('-uploaded_at')
    categories = Category.objects.all()
    context = {
        'category': category_obj,
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/shop.html', context)

def product(request, slug):
    product_obj = Product.objects.get(slug=slug)
    products_imeges = ProductImeges.objects.filter(product=product_obj)
    return render(request, 'shop/product.html', {'product': product_obj, 'imeges': products_imeges})
