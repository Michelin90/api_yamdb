from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name="Название")
    slug = models.SlugField(unique=True,
                            verbose_name="Метка",)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200,
                            unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256,
                            unique=True)
    year = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='titles')
    description = models.CharField(max_length=400,
                                   blank=True,
                                   null=True)
    genre = models.ForeignKey(Genre,
                              on_delete=models.CASCADE,
                              related_name='titles')

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title_id = models.ForeignKey(Title,
                                 on_delete=models.CASCADE,
                                 related_name='genres')
    genre_id = models.ForeignKey(Genre,
                                 on_delete=models.CASCADE,
                                 related_name='genres')
