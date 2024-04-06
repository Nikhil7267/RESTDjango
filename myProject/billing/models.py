from django.db import models
from django.contrib.auth.models import AbstractUser

# Employee Model
from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Cashier', 'Cashier'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Cashier')

    # Custom related_name for groups
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='employee_set',
        related_query_name='employee',
    )

    # Custom related_name for user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='employee_set',
        related_query_name='employee',
    )

    def __str__(self):
        return self.username



# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Sale Model
class Sale(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale for {self.product.name} by {self.employee.username}"
