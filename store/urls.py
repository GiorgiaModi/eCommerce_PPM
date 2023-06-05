from django.urls import path
from . import views

#from .views import add_to_cart

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.update_item, name="update_item"),
    path('search/', views.search, name="search"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('likeProduct/<int:id>/', views.likeProduct, name='likeProduct'),
    path('likedProducts/', views.likedProducts, name='likedProducts'),
    path('category_page/<int:id>/', views.category, name='category'),
]