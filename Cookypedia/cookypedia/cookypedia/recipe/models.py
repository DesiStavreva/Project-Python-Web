from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from cookypedia.core.validators import image_size_validator_5mb

UserModel = get_user_model()


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class ChoicesStringsMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Type(ChoicesStringsMixin, Enum):
    STARTER = 'Starter'
    MAIN = 'Main'
    DESSERT = 'Dessert'


class RecipeModel(models.Model):
    name = models.CharField(max_length=30)
    recipe_photo = models.ImageField(null=False, blank=False, validators=(image_size_validator_5mb,),
                                     upload_to='photos/')
    type = models.CharField(
        choices=Type.choices(),
        max_length=Type.max_length(),
    )
    ingredients = models.TextField(null=False, blank=False)
    cook_time = models.PositiveIntegerField(null=False, blank=False)
    method = models.TextField(null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk} - {self.name}"
