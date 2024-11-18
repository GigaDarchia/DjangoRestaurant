from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import User


class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()