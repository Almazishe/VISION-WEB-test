from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserAccountSerializer

User = get_user_model()

class UserAccountListAPIView(ListAPIView):

    serializer_class = UserAccountSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
