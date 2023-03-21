from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200,
                            unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name