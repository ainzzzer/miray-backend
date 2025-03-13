from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)


class ProductType(models.Model):
    """Тип, к которому будут относиться продукты.

    К примеру: золотые изделия, серебряные и т.д."""

    name = models.CharField(max_length=150, unique=True)
    # Стоимость за грамм
    price = models.PositiveIntegerField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    product_type = models.ForeignKey(
        ProductType, on_delete=models.CASCADE, related_name="products")  # PROTECT
    weight = models.FloatField(validators=[MinValueValidator(0)])
    discount_percentage = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(100)])
    is_available = models.BooleanField(default=False)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_posters/", max_length=500)

    # Порядок фотографий
    # Фото с индексом 1 будет заглавным
    index = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("product", "index")


class ProductFile(models.Model):
    """Медиа файлы продукта."""

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="products_files/", max_length=500)


class Option(models.Model):
    """Характеристика для продуктов."""

    name = models.CharField(max_length=50, unique=True)
    is_general = models.BooleanField(default=False)


class OptionValue(models.Model):
    """Значение характеристики для продуктов."""

    option = models.ForeignKey(
        Option, on_delete=models.CASCADE, related_name="option_values")
    value = models.CharField(max_length=50)

    class Meta:
        unique_together = ("option", "value")


class ProductOption(models.Model):
    """Характеристика продукта.

    Связующая таблица."""

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="options")
    option = models.ForeignKey(
        Option, on_delete=models.CASCADE, related_name="product_options")

    class Meta:
        unique_together = ("product", "option")


class ProductOptionValue(models.Model):
    """Значение характеристики продукта.

    Связующая таблица."""

    product_option = models.ForeignKey(
        ProductOption, on_delete=models.CASCADE, related_name="product_option_values")
    option_value = models.ForeignKey(
        OptionValue, on_delete=models.CASCADE, related_name="product_option_values")

    class Meta:
        unique_together = ("product_option", "option_value")
