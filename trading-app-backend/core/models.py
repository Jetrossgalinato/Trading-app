from django.db import models
from django.contrib.auth.models import AbstractUser 

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=20)  # e.g., 'kg', 'sack', 'liters'
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Trade(models.Model):
    TRADE_TYPE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)  # Corrected reference
    quantity = models.PositiveIntegerField()
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trade_type} {self.quantity} of {self.product.name} by {self.user.username}"

class Message(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)  # Corrected reference
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.user.username} at {self.timestamp}"

class Notification(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)  # Corrected reference
    type = models.CharField(max_length=50) 
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

class UserProfile(AbstractUser ):
    location = models.CharField(max_length=100, blank=True, null=True)
    membership_status = models.CharField(max_length=20, choices=[('FREE', 'Free'), ('PREMIUM', 'Premium')], default='FREE')

    def __str__(self):
        return self.username