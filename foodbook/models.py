from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, null=True)
    votes = models.IntegerField(default=0)
    
    
class User_Profile(models.Model):
    ##user_key = models.IntegerField(primary_key=True)
    ##User key should be created automatically.  Redundant code.
    user_profile_name = models.CharField(max_length=200,blank=True,null=True)
    image_tags = models.CommaSeparatedIntegerField(max_length=200,blank=True,null=True)
    favorite_restaurants = models.CommaSeparatedIntegerField(max_length=200,blank=True,null=True)
    
    def __init__(self,user_name,image_tags,favorite_restaurants):
        self._user_profile_name = user_name
        self._image_tags = image_tags
        self._favorite_restaurants = favorite_restaurants
        
##Create the image table
class Image(models.Model):
    image_url = models.CharField(max_length=600,blank=True, null=True)
    image_tags = models.CommaSeparatedIntegerField(max_length=200,blank=True, null=True)
    image_text = models.CharField(max_length=140,blank=True, null=True)
    image_views = models.IntegerField(blank=True,null=True)
    image_likes = models.IntegerField(blank=True,null=True)
    image_dislikes = models.IntegerField(blank=True,null=True)
    restaurant_key = models.IntegerField(blank=True,null=True)
    
    def __init__(self,image_url,image_tags,image_text,image_views,_image_likes,image_dislikes, restaurant_key):
        self._image_url = image_url
        self._image_tags = image_tags
        self._image_text = image_text
        self._image_views = image_views
        self._image_likes = image_likes
        self._image_dislikes = image_dislikes
        self._restaurant_key = restaraunt_key