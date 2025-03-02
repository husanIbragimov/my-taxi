from ckeditor.fields import RichTextField
from django.db import models

from apps.common.models import BaseModel


class Ad(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to="ads/")

    class Meta:
        db_table = "ads"
        ordering = ["-id"]
        verbose_name = "Ad"
        verbose_name_plural = "Ads"

    def __str__(self):
        return f"{self.title}"


class AdImages(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="ads/")

    class Meta:
        ordering = ["id"]
        db_table = "ad_images"
        verbose_name = "Ad Image"
        verbose_name_plural = "Ad Images"
