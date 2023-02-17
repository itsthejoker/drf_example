from rest_framework import serializers

from demo.core.models import Author, Article, Recipe


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    important_field = serializers.IntegerField(source="get_important_value")

    class Meta:
        model = Article
        fields = [
            "title",
            "body",
            "author",
            "is_published",
            "important_field",
        ]


class IngredientField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientField(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = "__all__"


class ShitpostSerializer(serializers.Serializer):
    quote = serializers.CharField(max_length=120)
    character = serializers.CharField(max_length=120)
