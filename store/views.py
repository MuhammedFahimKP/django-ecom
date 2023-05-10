from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from category.models import Category


def shop(request,category_slug=None):
    categories=None
    product=None

    if category_slug !=None:
        categories=get_object_or_404(Category,slug=category_slug)
        product=Product.objects.all().filter(category=categories,is_available=True)
        product_count = product.count()
    else:
        product=Product.objects.all().filter(is_available=True)
        product_count = product.count()
    context={
        'product':product,
        'productcount':product_count
    }
    return render(
        request,
        'zay/shop.html',
        context
        )



def product_detail(request,category_slug,product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)

    except Exception as e:
        raise e
    
    context={
        'product':single_product
    }

    return render(
        request,
        'zay/shop-single.html',
        context
        )


