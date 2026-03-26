from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

class StudyEntry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    topic = models.CharField(max_length=200, blank=False)

    study_date = models.DateField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    progress = models.IntegerField(blank=False)

    description = RichTextField(blank=False)
    notes = RichTextField(blank=False)

    def __str__(self):
        return self.topic

class StudyImage(models.Model):

    entry = models.ForeignKey(
        StudyEntry,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(upload_to="study_images/")