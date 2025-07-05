from django.conf import settings
from django.db import models
from main.models import ClothingItem, Size

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "В ожидании"),
        ("shipped", "Отправлен"),
        ("delivered", "Доставлен"),
        ("canceled", "Отменен"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=30, verbose_name="Отчество")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")
    apartment_number = models.CharField(max_length=10, verbose_name="Номер квартиры")
    postal_code = models.CharField(max_length=10, verbose_name="Почтовый индекс")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    tracking_number = models.CharField(max_length=40, blank=True, default="В ожидании", verbose_name="Номер отслеживания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Статус")

    def __str__(self):
        return f'Order {self.id} from {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.clothing_item} ({self.size})'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


