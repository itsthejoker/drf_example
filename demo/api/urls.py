from django.urls import path, include
from rest_framework import routers

from demo.api.views import (
    AuthorViewSet,
    StarWarsShitpostViewSet,
    ArticleViewSet,
    RecipeViewSet,
)

router = routers.DefaultRouter()

router.register(r"authors", AuthorViewSet)
router.register(r"articles", ArticleViewSet)
router.register(r"recipes", RecipeViewSet)

# One or the other. Either give it to the router and let it handle routes for you OR
# give it its own URL down below.

urls = [
    path("", include(router.urls)),
    path("shitposts/", StarWarsShitpostViewSet.as_view()),
]
