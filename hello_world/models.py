from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    username   = models.CharField(max_length=100, unique=True)
    password   = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'hello_world'


class Product(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField()
    cost        = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'hello_world'


class Order(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_of_order = models.DateTimeField(auto_now_add=True)
    cost         = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} — {self.user.username}"

    class Meta:
        app_label = 'hello_world'