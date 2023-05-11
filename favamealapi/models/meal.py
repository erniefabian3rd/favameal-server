from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    """Meal Model"""
    name = models.CharField(max_length=55)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    # TODO: Establish a many-to-many relationship with User through the appropriate join model
    favorites = models.ManyToManyField(User, through="FavoriteMeal", related_name="meals")
    ratings = models.ManyToManyField(User, through="MealRating", related_name="meal_ratings")
    
    # TODO: Add an user_rating custom properties
    @property
    def user_rating(self):
        return self.__user_rating

    @user_rating.setter
    def user_rating(self, value):
        self.__user_rating = value

    # TODO: Add an avg_rating custom properties
    @property
    def avg_rating(self):
        return self.__avg_rating

    @avg_rating.setter
    def avg_rating(self, value):
        self.__avg_rating = value

    # TODO: Add an is_favorite custom properties
    @property
    def is_favorite(self):
        return self.__is_favorite

    @is_favorite.setter
    def is_favorite(self, value):
        self.__is_favorite = value