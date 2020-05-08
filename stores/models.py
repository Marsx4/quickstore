from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class StoreType(models.Model):
    store_categories=(('stater','Starter'),('basic','Basic'),('premium','Premium'),('unlimited','Unlimited'))
    category=models.CharField(choices=store_categories,max_length=20)
    maximum_products=models.PositiveIntegerField()
    description=models.TextField(blank=True)
    cost=models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.category 


class Store(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(default='business description')
    category=models.ForeignKey(StoreType,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
