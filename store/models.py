from uuid import uuid4
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNISEX = 'U'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNISEX, 'Unisex'),
    ]

    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=512, unique=True)
    description = models.TextField()
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )
    count = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=UNISEX)

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = [['cart', 'product']]
