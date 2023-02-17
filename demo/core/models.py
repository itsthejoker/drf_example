from django.db import models
from django.template.defaultfilters import slugify

from demo.core.mixins import ModelTimeStampMixin


class Author(models.Model):
    name = models.CharField(max_length=120)
    tagline = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Article(ModelTimeStampMixin):
    title: str = models.CharField(max_length=100)
    body: str = models.TextField()
    author: Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug: str = models.CharField(max_length=100, null=True, blank=True)
    is_published: bool = models.BooleanField(default=False)

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super().save(**kwargs)

    def get_important_value(self) -> int:
        """Sometimes we just need an important computed value."""
        return 42

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Recipe(ModelTimeStampMixin):
    title: str = models.CharField(max_length=100)
    instructions: str = models.TextField()
    ingredients: list[Ingredient] = models.ManyToManyField(Ingredient)
    author: Author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
