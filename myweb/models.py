from django.db import models

# Create your models here.


class TodoItem(models.Model):
    titel = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


# models.py


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="static/images/")

    def __str__(self):
        return self.product_name
