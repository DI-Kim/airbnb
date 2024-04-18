from django.db import models


# Create your models here.
class House(models.Model):
    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Positive Numbers Only"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, help_text="Does this house allow pets?"
    )
    # on_delete를 통해서 users.User가 삭제되었을 때 house가 어떻게 되는지 설정할 수 있다.
    # models.CASCADE : user 삭제시 house 삭제
    # models.SET_NULL : user 삭제시 owner 값을 NULL로 변경
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
