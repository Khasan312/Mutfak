from django.contrib import admin

from .models import FoodRecept, Category, Help, Raiting, LVL,Favorite

admin.site.register(FoodRecept)
admin.site.register(Category)
admin.site.register(Raiting)
admin.site.register(LVL)
admin.site.register(Favorite)
admin.site.register(Help)