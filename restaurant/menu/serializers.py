from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuMainCategory
        fields = "__all__"


class MainCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuMainCategory
        fields = ["id", "name"]


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = "__all__"


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = ["id", "name", "thumbnail"]


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class IngredientListSerializer(serializers.ModelSerializer):
    dish = serializers.CharField(source="dish.name")
    class Meta:
        model = Ingredient
        fields = "__all__"


class SubCategoryDetailSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = MenuSubCategory
        fields = ["dishes"]


class DishListSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = ["name", "image", "ingredients"]
