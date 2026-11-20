from rest_framework.generics import RetrieveAPIView,RetrieveUpdateAPIView
from account.serializers import UserSerializer,ProfileSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ProfileView(RetrieveAPIView):
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class ProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user.profile