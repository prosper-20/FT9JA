import random
import time
from django.core.management.base import BaseCommand
from trade.models import Trader, TradeRecord
from django.http import HttpResponse
from decimal import Decimal

# class Command(BaseCommand):
#     help = 'Simulate trader performance'

#     def handle(self, *args, **options):
#         traders = Trader.objects.all()

#         while True:
#             for trader in traders:
#                 # Simulate profit or loss (randomly generate a value between -5 and 5)
#                 profit_or_loss = random.uniform(-5, 5)
#                 trader.balance += profit_or_loss
#                 trader.save()

#                 # Record the trade in the database
#                 TradeRecord.objects.create(trader=trader, profit_or_loss=profit_or_loss)

#             # Sleep for one minute (adjust as needed)
#             time.sleep(60)



def simulate_profit_and_loss(request):
    traders = Trader.objects.all()
    for trader in traders:
        # Simulate profit or loss (randomly generate a value between -5 and 5)
        profit_or_loss = random.uniform(-5, 5)
        if profit_or_loss < 0:
            TradeRecord.objects.create(trader=trader, profit_or_loss=profit_or_loss, made_profit=False)
            trader.balance += Decimal(profit_or_loss)
            trader.save()
        else:
            trader.balance += Decimal(profit_or_loss)
            trader.save()
            TradeRecord.objects.create(trader=trader, profit_or_loss=profit_or_loss)

    return HttpResponse("Simulation Complete!!, Pls refer back to your dashboard")


