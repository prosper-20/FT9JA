from django.contrib import admin
from .models import Trade, Trader,TradeRecord

class TradeAdmin(admin.ModelAdmin):
    list_display = ["sender", "amount", "receiver", "transaction_date"]
    list_filter = ["sender"]
    search_fields = ["amount", "sender"]


admin.site.register(Trader)

admin.site.register(Trade, TradeAdmin)


class TradeRecordAdmin(admin.ModelAdmin):
    list_display = ["trader", "profit_or_loss", "made_profit", "transaction_date"]
    list_filter = ["trader"]

admin.site.register(TradeRecord, TradeRecordAdmin)


