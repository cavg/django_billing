from django.db import models
from account.models import Company

PERIOD_CHOICE = (
    ('monthly', 'monthly'),
    ('quarterly', 'quarterly'),
    ('biannual', 'biannual'),
    ('annual', 'annual')
)

class Plan(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    hide = models.BooleanField(default=False, blank=False, null=False)
    discount = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=25, blank=False, null=False, choices=PERIOD_CHOICE, default=PERIOD_CHOICE[3])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return "{}".format(self.name)

class Item(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=25, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return "{}".format(self.name)

    def plan_name(self):
        return "{}".format(self.plan.name)


class OrderPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def company_name(self):
        return "{}".format(self.company.name)

    def plan_name(self):
        return "{}".format(self.plan.name)

    def __str__(self):
        return "{} - {}".format(self.plan.name, self.company.name)

STATUS_CHOICE = (
    ('created', 'created'),
    ('failed', 'failed'),
    ('pending', 'pending'),
    ('verified', 'verified')
)

METHOD_CHOICE = (
    ('kiphu', 'kiphu'),
    ('e_transfer', 'e_transfer'),
    ('cash', 'cash'),
    ('mercadopago', 'mercadopago'),
    ('webpay', 'webpay')
)

class Payment(models.Model):
    order_plan = models.ForeignKey(OrderPlan, on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=25, blank=False, null=False, choices=STATUS_CHOICE, default=STATUS_CHOICE[0])
    amount = models.IntegerField(blank=False, null=False)
    method = models.CharField(max_length=25, blank=True, null=False, choices=METHOD_CHOICE, default=METHOD_CHOICE[0])
    secondary_id = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return "{}".format(self.id)

