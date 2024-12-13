from django.urls import path
from .views import BrandList, BrandDetail, OrderList, OrderDetail, UserList, UserDetail, CategoryList, CategoryDetail, CardList, CardDetail, ProductList, ProductDetail, ProductCategoryList, ProductCategoryDetail, OrderProductList, OrderProductDetail
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.order_add, name='order_add'),
    path('orders/<int:id>/', views.order_detail, name='order_detail'),
    path('orders/edit/<int:order_id>/', views.order_edit, name='order_edit'),
    path('orders/<int:order_id>/delete/', views.order_confirm_delete, name='order_confirm_delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),

    path('brand/', BrandList.as_view()),
    path('brand/<int:pk>/', BrandDetail.as_view()),

    path('order/', OrderList.as_view()),
    path('order/<int:pk>', OrderDetail.as_view()),

    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),

    path('category/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),

    path('card/', CardList.as_view()),
    path('card/<int:pk>/', CardDetail.as_view()),

    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),

    path('product_category/', ProductCategoryList.as_view()),
    path('product/<int:pk>/', ProductCategoryDetail.as_view()),

    path('order_product/', OrderProductList.as_view()),
    path('order_product/<int:pk>/', OrderProductDetail.as_view()),



    ]