import random
from typing import Any

from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from demo.api.serializers import (
    ArticleSerializer,
    AuthorSerializer,
    ShitpostSerializer,
    RecipeSerializer,
)
from demo.core.models import Author, Article, Recipe


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(detail=True, methods=["GET"])
    def ingredients(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        return Response(data={'ingredients': [i.name for i in recipe.ingredients.all()]})

    @action(detail=False, methods=["GET"])
    def count(self, request):
        return Response(data={'total_recipes': Recipe.objects.count()})


class StarWarsShitpostViewSet(generics.GenericAPIView):
    data = [
        {
            "quote": "Hello there, General Kenobi.",
            "character": "General Grevious",
        },
        {
            "quote": "Did you ever hear the Tragedy of Darth Plagueis the Wise?",
            "character": "Darth Sidious",
        },
        {
            "quote": "AAAAAUUUUUGGGGHHHHH",
            "character": "Darth Vader",
        },
    ]

    serializer_class = ShitpostSerializer

    def get(self, *args: Any, **kwargs: Any) -> Response:
        data = ShitpostSerializer(random.choice(self.data)).data

        return Response(data)
