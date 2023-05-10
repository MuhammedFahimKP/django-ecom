from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop,name="shop"),
    path('<slug:category_slug>',views.shop,name="products_by_category"),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail,name="products_detail")
]