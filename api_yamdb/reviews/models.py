from django.db import models


from django.db.models.base import ModelBase


User = ModelBase('User', (models.Model,), {'__module__': 'reviews.models', 'app_label': 'your_app'})
Review = ModelBase('Post', (models.Model,), {'__module__': 'reviews.models', 'app_label': 'your_app'})


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
    created = models.DateTimeField(
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


class Category(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name="Название")
    slug = models.SlugField(unique=True,
                            verbose_name="Метка",)

    def __str__(self):
        return self.name
