from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Customer(models.Model):
    phone_number = models.CharField(
        max_length=settings.MAX_LENGTH,
        null=False,
        blank=False,
        primary_key=True
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer'
    )


class DishCount(models.Model):
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE, db_index=True)
    order = models.ForeignKey('order', on_delete=models.CASCADE, db_index=True)

    count = models.IntegerField(default=1, null=False)


class Dish(models.Model):
    name = models.CharField(
        max_length=settings.MAX_LENGTH,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=settings.MAX_LENGTH,
        null=False,
        blank=False,
    )

    picture = models.ImageField(
        upload_to='uploads/'
    )

    description = models.TextField(
        null=True,
        blank=False,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


class Restaurant(models.Model):
    name = models.CharField(
        max_length=settings.MAX_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=settings.MAX_LENGTH,
        null=False,
        blank=False,
    )

    picture = models.ImageField(
        upload_to='uploads/'
    )

    phone_number = models.CharField(
        max_length=settings.MAX_LENGTH,
        null=False,
        blank=False,
        primary_key=True
    )

    coord_x = models.DecimalField(
        null=False,
        decimal_places=10,
        max_digits=40,
    )

    coord_y = models.DecimalField(
        null=False,
        decimal_places=10,
        max_digits=40,
    )

    dishes = models.ManyToManyField(
        Dish
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.DO_NOTHING,
        null=False,
    )

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.DO_NOTHING,
        null=False,
    )

    meal_date_time = models.DateTimeField(
        null=False,
    )

    comment = models.TextField(
        max_length=settings.MAX_LENGTH,
        null=True,
        blank=False,
    )

    person_count = models.IntegerField(
        null=False,
        default=1
    )

    status = models.IntegerField(
        null=False,
        choices=(
            ("NEW", 1),
            ("IN PROGRESS", 2),
            ("READY TO MEAL", 3),
            ("FINISHED", 4)
        ),
        default=1
    )

    dishes = models.ManyToManyField(
        Dish,
        through=DishCount
    )
