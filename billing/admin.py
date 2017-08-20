# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Plan
from .models import Item
from .models import OrderPlan
from .models import Payment

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'discount', 'hide')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'name', 'price')

class OrderPlanAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'plan_name', 'created_at', 'updated_at')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('status', 'amount', 'method', 'created_at', 'updated_at')

admin.site.register(Item, ItemAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(OrderPlan, OrderPlanAdmin)
admin.site.register(Payment, PaymentAdmin)