from django.shortcuts import render,redirect
from category.models import Category


def home(request):
    category=Category.objects.all()
    context={
        'category':category,
    }
    return render(
        request,'zay/index.html',
        context
        )












