from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"product-types", views.ProductTypeViewSet)
router.register(r"options", views.OptionViewSet)
router.register(r"option-values", views.OptionValueViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
