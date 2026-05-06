from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    paid_amount = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

    def total_coast(self):
        return sum(item.get_coast() for item in self.items.all())

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    def get_coast(self):
        return self.price * self.quantity

    def __str__(self):
        return self.product.title