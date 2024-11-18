from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class CustomModelViewSet(ModelViewSet):
    """
    A custom model viewset that includes additional permission checks.
    Checks if the requesting user owns the object before allowing deletion.
    """
    user_lookup = None  # Specify the ownership lookup path in subclasses.

    def destroy(self, request, *args, **kwargs):
        """
        Custom delete method that ensures only the owner of an object can delete it.
        Raises PermissionDenied if the user does not own the item.
        """
        # Retrieve the object instance to be deleted.
        instance = self.get_object()

        # Check if the user is the owner by filtering with user_lookup.
        owner_exists = self.get_queryset().filter(
            pk=instance.pk,
            **{self.user_lookup: request.user.id}
        ).exists()

        if not owner_exists:
            # Raise an error if the user does not own the item.
            raise PermissionDenied("You don't own this item.")

        # Proceed with the default delete behavior if ownership is validated.
        return super().destroy(request, *args, **kwargs)


class RestaurantViewSet(CustomModelViewSet):
    """
    ViewSet for managing Restaurant objects.
    Ensures that only the owner of a restaurant can delete it.
    """
    queryset = Restaurant.objects.select_related('owner')
    user_lookup = "owner_id"  # Path to check ownership.

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """
        Determines the serializer class based on the action.
        Returns a list serializer for listing and a detailed serializer otherwise.
        """
        return RestaurantListSerializer if self.action == 'list' else RestaurantSerializer

    def perform_create(self, serializer):
        """
        Assigns the currently authenticated user as the owner when creating a restaurant.
        """
        serializer.save(owner=self.request.user)


class MainCategoryViewSet(CustomModelViewSet):
    """
    ViewSet for managing main menu categories within a restaurant.
    Ensures that only the owner of the associated restaurant can delete categories.
    """
    queryset = MenuMainCategory.objects.select_related('restaurant')
    user_lookup = "restaurant__owner_id"  # Path to check ownership.
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Determines the serializer class based on the action.
        Returns a list serializer for listing and a detailed serializer otherwise.
        """
        return MainCategoryListSerializer if self.action == 'list' else MainCategorySerializer


class SubCategoryViewSet(CustomModelViewSet):
    """
    ViewSet for managing subcategories within main menu categories.
    Ensures that only the owner of the associated restaurant can delete subcategories.
    """
    queryset = MenuSubCategory.objects.select_related('parent')
    user_lookup = "parent__restaurant__owner_id"  # Path to check ownership.
    filterset_fields = ["parent", "name"]  # Allow filtering by parent category and name.
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Determines the serializer class based on the action.
        Returns different serializers for listing, retrieving, or modifying.
        """
        if self.action == "list":
            return SubCategoryListSerializer
        elif self.action == "retrieve":
            return SubCategoryDetailSerializer
        else:
            return SubCategorySerializer


class DishViewSet(CustomModelViewSet):
    """
    ViewSet for managing dishes within menu categories.
    Ensures that only the owner of the associated restaurant can delete dishes.
    """
    queryset = Dish.objects.select_related('category')
    user_lookup = "category__parent__restaurant__owner__id"  # Path to check ownership.
    filterset_fields = ["category", "name"]  # Allow filtering by category and name.
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Determines the serializer class based on the action.
        Returns a list serializer for listing and a detailed serializer otherwise.
        """
        return DishListSerializer if self.action == 'list' else DishSerializer

class IngredientViewSet(CustomModelViewSet):
    queryset = Ingredient.objects.select_related('dish')
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return IngredientListSerializer if self.action == 'list' else IngredientSerializer