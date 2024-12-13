from rest_framework import generics
from .models import Brand, Product, Category, Card, User , Order , OrderProduct, ProductCategory
from .serializers import BrandSerializer, OrderSerializer, UserSerializer, CategorySerializer, CardSerializer, ProductSerializer, ProductCategorySerializer, OrderProductSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def order_confirm_delete(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)

    product_price = sum(op.product.price for op in order.order_products.all())
    order.total_price = product_price + order.price

    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    return render(request, 'online_shop/order_confirm_delete.html', {'order': order})

def order_edit(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'online_shop/order_form.html', {'form': form})

def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'online_shop/order_form.html', {'form': form})



@login_required
def order_list(request):
    orders = Order.objects.prefetch_related('order_products__product').all()
    for order in orders:
        product_price = sum(op.product.price for op in order.order_products.all())
        order.product_price = product_price
        order.total_price = product_price + order.price
    return render(request, 'online_shop/order_list.html', {'orders': orders})

def order_detail(request, id):
    order = get_object_or_404(Order, order_id=id)

    product_price = sum(op.product.price for op in order.order_products.all())
    total_price = order.price + product_price

    return render(request, 'online_shop/order_detail.html', {
        'order': order,
        'product_price': product_price,
        'total_price': total_price,
    })


class BrandList(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()



class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CardList(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetail(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCategoryList(generics.ListCreateAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class OrderProductList(generics.ListCreateAPIView):
    serializer_class = OrderProductSerializer
    queryset = OrderProduct.objects.all()


class OrderProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderProductSerializer
    queryset = OrderProduct.objects.all()










