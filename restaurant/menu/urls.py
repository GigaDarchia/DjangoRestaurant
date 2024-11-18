from .views import RestaurantViewSet, MainCategoryViewSet, SubCategoryViewSet, DishViewSet, IngredientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('restaurants', RestaurantViewSet, basename="restaurants")
router.register('main-categories', MainCategoryViewSet, basename='main-categories')
router.register('subcategories', SubCategoryViewSet, basename="subcategories")
router.register('dishes', DishViewSet, basename="dishes")
router.register('ingredient', IngredientViewSet, basename='ingredient')

urlpatterns = [] + router.urls
