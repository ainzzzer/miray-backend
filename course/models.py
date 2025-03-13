from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Lesson(models.Model):
    name = models.CharField(max_length=255, unique=True)
    index = models.PositiveSmallIntegerField()
    video = models.FileField(upload_to="lesson_videos/", max_length=500)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons")

    class Meta:
        unique_together = ("course", "index")
