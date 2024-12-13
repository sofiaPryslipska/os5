from django.test import TestCase
from django.urls import reverse
from .models import User, Brand, Product, Order
from django.utils import timezone


class OrderTestCase(TestCase):
    def setUp(self):
        # Створення користувача
        self.user = User.objects.create(
            username='testuser',
            first_name='Test',
            last_name='User',
            password='12345',  # У реальному проекті пароль потрібно хешувати
            telephone='1234567890'
        )

        # Створення бренду і продукту
        self.brand = Brand.objects.create(title="Test Brand")
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product.",
            price=100.00,
            brand=self.brand
        )

        # Створення замовлення
        self.order = Order.objects.create(
            date=timezone.now(),
            status="to ship",
            payment="waiting",
            price=100.00,
            user=self.user,  # Використовуємо користувача, якого створили
            address="Test Address"
        )

    def test_order_list_view(self):
        # Якщо користувач не авторизований, перевіримо редирект
        response = self.client.get(reverse('order_list'))
        self.assertRedirects(response, '/login/?next=/online_shop/orders/') # Перевірка редиректу на сторінку входу

        # Авторизація користувача
        self.client.login(username='testuser', password='12345')

        # Запит до сторінки замовлень після логіну
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)  # Перевірка, що статус 200 після логіну
        self.assertContains(response, 'Test Product')  # Перевірка, чи є продукт у відповіді
