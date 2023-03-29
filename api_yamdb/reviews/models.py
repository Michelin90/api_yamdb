from django.core.validators import (MinValueValidator,
                                    MaxValueValidator,)
from django.db import models

from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name="Название",
                            db_index=True,
                            )
    slug = models.SlugField(unique=True,
                            verbose_name="Метка",)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            db_index=True,
                            )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256,
                            unique=True)
    year = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 null=True)
    description = models.CharField(max_length=400,
                                   blank=True,
                                   null=True)
    genre = models.ManyToManyField(Genre,
                                   related_name='titles',
                                   )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title_id = models.ForeignKey(Title,
                                 on_delete=models.CASCADE,
                                 related_name='genres')
    genre_id = models.ForeignKey(Genre,
                                 on_delete=models.CASCADE,
                                 related_name='genres')


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        blank=True,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
        db_index=False
    )
    text = models.CharField(
        max_length=200
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
        db_index=False
    )
    score = models.IntegerField(
        'Оценка',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        ),
        error_messages={'validators': 'Допустимая оценка от 1 до 10!'}
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author'),
                name='unique review'
            )]
        ordering = ('pub_date', )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='автор'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='отзыв'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['author_id']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
