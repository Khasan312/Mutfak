from django.db import models
from users.models import User

class LVL(models.Model):

    level = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.level

    class Meta:
        app_label = 'food'


class Raiting(models.Model):
    raiting = models.PositiveIntegerField(blank=True, null=True)# 5 possible rating values

    def __str__(self) -> str:
        return str(self.raiting)


class Category(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class FoodRecept(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='authors')
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='foods', blank=True, null=True)
    ingredients = models.TextField(max_length=300)
    level = models.ForeignKey(LVL, on_delete=models.CASCADE)
    time_for_cook = models.IntegerField()
    quantity_of_calories = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    raiting = models.ManyToManyField(Raiting)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodRecept, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)



class Help(models.Model):
    help = models.TextField()

    def __str__(self) -> str:
        return self.help
