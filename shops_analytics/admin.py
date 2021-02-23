from django.contrib import admin
from .models import *
from .models import DataProductsale


class BalanceOperationAdmin(admin.ModelAdmin):
    model = DataProductsale
    list_display = ['receipt_id', 'date', 'original_price', 'price', 'qty', 'discount', 'margin_price_total',
                    'total_price', 'client', 'product', 'shop', 'terminal', 'week_day', 'dt', 'refund', 'bulk']


admin.site.register(DataProductsale, BalanceOperationAdmin)

