from django.db import models


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class Meta:
        db_table = "countries"

    def __str__(self):
        return self.name
