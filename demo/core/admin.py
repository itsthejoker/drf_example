from django.contrib import admin

from demo.core.models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Ingredient)
admin.site.register(Recipe)
