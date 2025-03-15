from rest_framework.viewsets import ModelViewSet

from drf_spectacular.utils import extend_schema

from project.permissions import IsStaffOrClientWithPermReadOnly

from .serializers import (CategorySerializer, ProductTypeSerializer,
                          OptionSerializer, OptionValueSerializer)
from .models import Category, ProductType, Option, OptionValue


@extend_schema(
    tags=["Категории"]
)
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrClientWithPermReadOnly]


@extend_schema(
    tags=["Типы товаров"]
)
class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsStaffOrClientWithPermReadOnly]


@extend_schema(
    tags=["Характеристики"]
)
class OptionViewSet(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsStaffOrClientWithPermReadOnly]


@extend_schema(
    tags=["Опции характеристик"]
)
class OptionValueViewSet(ModelViewSet):
    queryset = OptionValue.objects.all()
    serializer_class = OptionValueSerializer
    permission_classes = [IsStaffOrClientWithPermReadOnly]
