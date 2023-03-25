from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name="Название")
    slug = models.SlugField(unique=True,
                            verbose_name="Метка",)

    def __str__(self):
        return self.name