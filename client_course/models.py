from django.db import models


class ClientCourse(models.Model):
    client = models.ForeignKey(
        "client.Client", on_delete=models.CASCADE, related_name="courses")
    course = models.ForeignKey(
        "course.Course", on_delete=models.CASCADE, related_name="client_courses")
    current_video_progress = models.TextField(default="[]")

    class Meta:
        unique_together = ("client", "course")


class ClientLesson(models.Model):
    class Status(models.TextChoices):
        CLOSED = "closed", "Закрыт"
        OPENED = "opened", "Открыт"
        PASSED = "passed", "Пройден"

    client_course = models.ForeignKey(
        ClientCourse, on_delete=models.CASCADE, related_name="lessons")
    lesson = models.ForeignKey(
        "course.Lesson", on_delete=models.CASCADE, related_name="client_lessons")
    status = models.CharField(
        max_length=25, choices=Status.choices, default=Status.CLOSED)

    class Meta:
        unique_together = ("client_course", "lesson")
