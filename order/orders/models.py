from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'orders'
        


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ('-order__created_at',)
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        db_table = 'order_items'
