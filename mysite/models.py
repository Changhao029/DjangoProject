from django.db import models


class Category(models.Model):
    """

    """
    title = models.CharField(verbose_name="category", max_length=32)


class Article(models.Model):
    """

    """
    status_choices = (
        (1, "published"),
        (2, "deleted")
    )
    title = models.CharField(verbose_name='title', max_length=32)
    summary = models.CharField(verbose_name='summary', max_length=255)
    content = models.TextField(verbose_name='content')
    category = models.ForeignKey(verbose_name='category', to='Category', on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name='status', choices=status_choices, default=1)