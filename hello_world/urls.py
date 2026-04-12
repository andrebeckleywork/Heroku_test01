from django.urls import path
from . import views

urlpatterns = [
    path('',         views.login_view,    name='login'),
    path('products/', views.products_view, name='products'),
    path('buy/<int:product_id>/', views.buy_view, name='buy'),
    path('logout/',   views.logout_view,   name='logout'),
]