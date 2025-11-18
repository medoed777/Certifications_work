from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название поставщика")
    email = models.EmailField(verbose_name="email поставщика")
    country = models.CharField(max_length=100, verbose_name="Страна поставщика")
    city = models.CharField(max_length=100, verbose_name="Город поставщика")
    street = models.CharField(max_length=255, verbose_name="Улица поставщика")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома поставщика")

    def __str__(self):
        return self.name


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    product_name = models.CharField(max_length=255, verbose_name="Название продукта")
    product_model = models.CharField(max_length=255, verbose_name="Модель продукта")
    product_release_date = models.DateField(verbose_name="Дата выпуска продукта")

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="suppliers",
        null=True,
        verbose_name="Поставщик",
    )
    debt_to_supplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name="Уровень иерархии")

    def __str__(self):
        return self.name
