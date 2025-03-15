from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from drf_spectacular.utils import extend_schema

from . import open_api


@extend_schema(
    examples=[
        open_api.staff_example,
    ],
)
class CustomTokenObtainPairView(TokenObtainPairView):
    @extend_schema(responses={200: TokenObtainPairSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
