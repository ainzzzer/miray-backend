from rest_framework.viewsets import ModelViewSet

from drf_spectacular.utils import extend_schema

from .serializers import (CategorySerializer, ProductTypeSerializer,
                          OptionSeriaizer, OptionValueSerializer)
from .models import Category, ProductType, Option, OptionValue


@extend_schema(
    tags=["Категории"]
)
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = None


@extend_schema(
    tags=["Типы товаров"]
)
class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    # permission_classes = None


@extend_schema(
    tags=["Характеристики"]
)
class OptionViewSet(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSeriaizer
    # permission_classes = None


@extend_schema(
    tags=["Опции характеристик"]
)
class OptionValueViewSet(ModelViewSet):
    queryset = OptionValue.objects.all()
    serializer_class = OptionValueSerializer
    # permission_classes = None
