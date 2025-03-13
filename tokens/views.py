from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from drf_spectacular.utils import extend_schema, OpenApiExample

from project.utils import ExceptionResponse

from . import schemas


@extend_schema(
    responses={
        200: TokenObtainPairSerializer,
        401: ExceptionResponse(
            "Не найдено активной учетной записи с указанными данными"
        ),
    },
    examples=[
        OpenApiExample(
            name="Cуперадмин",
            value={
                "username": "test_super_admin",
                "password": "12345678",
            },
            request_only=True,
        ),
        OpenApiExample(
            name="Админ1",
            value={
                "username": "Ast1areg-1",
                "password": "123456ergre780-",
            },
            request_only=True,
        ),
    ],
)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = schemas.TokenObtainPairResponseSerializer

    @extend_schema(
        responses={
            200: schemas.TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
