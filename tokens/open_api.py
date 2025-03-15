from drf_spectacular.utils import OpenApiExample


staff_example = OpenApiExample(
    name="Сотрудник",
    value={
        "username": "+7 (777) 123 45 67",
        "password": "12345678",
    },
    request_only=True,
)
