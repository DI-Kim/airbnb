from django.db import models
from common.models import CommonModel


# Create your models here.
class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):
    file = models.FileField()
    # OneToOneField는 ForiegnKey와 비슷하지만, 여러개를 가질 수 있는 ForiegnKey와는 다르게 한개만 가질 수 있다. (unique, 고유한 관계)
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="video",
    )

    def __str__(self):
        return "Video File"
