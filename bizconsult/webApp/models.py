from django.db import models

# Create your models here.

class Site_info(models.Model):
    name_site = models.CharField(max_length=50)
    phone_site = models.IntegerField()
    email_site = models.EmailField(max_length=100)
    address_site = models.CharField(max_length=100)
    copyright_site = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

class Banner (models.Model):
    title_banner = models.CharField(max_length=255) 
    description_banner = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)


class Service(models.Model):
    label_service = models.CharField(max_length=255)
    icon_service = models.CharField(max_length=30)
    title_service = models.CharField(max_length=30)
    description_service = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

class Reseau_social(models.Model):
    twitter_Reseau = models.URLField(null=True)
    facebook_Reseau =  models.URLField(null=True)
    youtube_Reseau =  models.URLField(null=True)
    instagram_Reseau =  models.URLField(null=True)
    linkedin_Reseau = models.URLField(null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)