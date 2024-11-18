from django.contrib import admin
from .models import MenuMainCategory, MenuSubCategory, Restaurant, Dish, Ingredient

# Register your models here.

@admin.register(MenuMainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(MenuSubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

