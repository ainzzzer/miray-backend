from datetime import datetime

from django.conf import settings
from django.http import JsonResponse
from django.db.models import ProtectedError
from django.core.files.storage import FileSystemStorage

from rest_framework import status, serializers
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import APIException, ValidationError

from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from drf_spectacular.utils import OpenApiResponse, OpenApiExample


fs = FileSystemStorage(location=settings.MEDIA_ROOT)


def datetime_now() -> datetime:
    # return datetime.now() + relativedelta(hours=TIME_DIFFERENCE_BETWEEN_SERVER)
    pass


def parse_datetime(datetime_str: str):
    formats = ["%d.%m.%Y %H:%M", "%d.%m.%Y"]

    for fmt in formats:
        try:
            return datetime.strptime(datetime_str, fmt)
        except ValueError:
            continue

    return None  # Если не соответствует ни одному формату


def parse_boolean(value):
    """Приводит строковые значения к boolean"""
    if isinstance(value, bool):  # Уже bool
        return value
    if isinstance(value, str):
        value = value.lower()
        if value in ("true", "1"):
            return True
        if value in ("false", "0"):
            return False
    return None  # Некорректное значение


def save_file_to_server(file, instance):
    file_location = instance._meta.get_field("poster").upload_to

    if not file:
        raise ValidationError({"uploaded_files": [f"file not found"]})

    return fs.save(f"{file_location}/{file.name}", file)


class BadRequestExceptionSerializer(serializers.Serializer):
    field_name = serializers.ListSerializer(
        child=serializers.CharField(default="message")
    )
    code = serializers.IntegerField(default=400)


class ExceptionSerializer(serializers.Serializer):
    detail = serializers.CharField()


class ExceptionResponse(OpenApiResponse):
    def __init__(self, detail: str, description: str = None):
        self.description = description
        self.examples = [OpenApiExample(name="Пример", value={"detail": f"{detail}"})]
        self.response = ExceptionSerializer


class ConflictException(APIException):
    status_code = 409
    default_detail = "Произошла ошибка конфликта"
    default_code = 409


class BadRequestException(APIException):
    status_code = 400
    default_detail = "Некорректный запрос"
    default_code = 400


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, (TokenError, InvalidToken)):
        return JsonResponse(
            {"detail": "Неверный или истёкший токен", "code": 401}, status=401
        )
    elif (
        isinstance(exc, ValidationError)
        and context["view"].get_view_name() == "Token Verify"
    ):
        return JsonResponse(
            {"token": ["Токен занесен в черный список"], "code": 400}, status=400
        )
    elif isinstance(exc, ProtectedError):
        return JsonResponse({"detail": "Защищено от удаления", "code": 403}, status=403)
    elif not response:
        if not settings.DEBUG and not settings.TESTING:
            response = Response(
                {"detail": str(exc), "code": status.HTTP_500_INTERNAL_SERVER_ERROR},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    return response


def custom_page_not_found_view(request, exception):
    return JsonResponse({"detail": "Не найдена", "code": 404}, status=404)


# def custom_server_error_view(request):
#     return JsonResponse(
#         {"detail": "Внутренняя ошибка сервера", "code": 500}, status=500
#     )


def custom_bad_request_view(request, exception):
    return JsonResponse({"detail": "Некорректный запрос", "code": 400}, status=400)


def custom_permission_denied_view(request, exception):
    return JsonResponse({"detail": "Доступ запрещен", "code": 403}, status=403)
