from django.db import models
import uuid
from django.contrib.auth.models import User

class Trade(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, max_length=30)
    sender = models.ForeignKey(User, related_name="money_sender", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.id


class Trader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(default=100, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username

class TradeRecord(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, max_length=30)
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    profit_or_loss = models.DecimalField(max_digits=10, decimal_places=2)
    made_profit = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-transaction_date"]

    def __str__(self):
        return self.trader.user.username

    



    
