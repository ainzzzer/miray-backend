from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView, TokenVerifyView

from .views import CustomTokenObtainPairView


urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("token/verify/", TokenVerifyView.as_view()),
    path("token/blacklist/", TokenBlacklistView.as_view()),
]
