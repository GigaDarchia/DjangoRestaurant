from django.db import models
from django.contrib.auth import settings
from django.utils.translation import gettext_lazy as _


class Restaurant(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    address = models.CharField(max_length=200, verbose_name=_("Address"))
    number = models.CharField(max_length=14, verbose_name=_("Number"))
    thumbnail = models.ImageField(upload_to="Restaurant Thumbnails", verbose_name=_("Thumbnail Image"), blank=True,
                                  null=True)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Owner"),
                              related_name="restaurants")

    def __str__(self):
        return self.name


class MenuMainCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    restaurant = models.ForeignKey(to="Restaurant", on_delete=models.CASCADE, verbose_name=_("Restaurant"),
                                   related_name="main_categories")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Menu main category")
        verbose_name_plural = _("Menu main categories")


class MenuSubCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    thumbnail = models.ImageField(upload_to="Category Thumbnails", verbose_name=_("Thumbnail Image"), blank=True,
                                  null=True)
    parent = models.ForeignKey(to="MenuMainCategory", on_delete=models.CASCADE, verbose_name=_("Parent Category"),
                               related_name="children")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Menu subcategory")
        verbose_name_plural = _("Menu subcategories")


class Dish(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    image = models.ImageField(upload_to="Dish Thumbnails", blank=True, null=True, verbose_name=_("Image"))
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)
    category = models.ForeignKey(to="MenuSubCategory", on_delete=models.CASCADE, verbose_name=_("Category"),
                                 related_name="dishes")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Dishes")


class Ingredient(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    dish = models.ForeignKey(to="Dish", on_delete=models.CASCADE, verbose_name=_("Dish"), related_name='ingredients')

    def __str__(self):
        return self.name
