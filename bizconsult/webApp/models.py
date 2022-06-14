from django.db import models

# Create your models here.

class Site_info(models.Model):
    name_site = models.CharField(max_length=50)
    phone_site = models.CharField(max_length=15)
    email_site = models.EmailField(max_length=100)
    address_site = models.CharField(max_length=100)
    copyright_site = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.name_site

class Banner (models.Model):
    title_banner = models.CharField(max_length=255) 
    description_banner = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title_banner


class Social_Network(models.Model):
    twitter_network = models.URLField(null=True)
    facebook_network =  models.URLField(null=True)
    youtube_network =  models.URLField(null=True)
    instagram_network =  models.URLField(null=True)
    linkedin_network = models.URLField(null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

class Contact(models.Model):
    name_contact = models.CharField(max_length=15)
    email_contact = models.EmailField(max_length=255)
    subject_contact = models.CharField(max_length=50)
    comments_contact = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name_contact


class Potentialite(models.Model):
    Icon = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description= models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title 

class Feature(models.Model):
    label_feature = models.CharField (max_length=50)
    description = models.TextField()
    
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.label_feature

class About(models.Model):
    title_about = models.CharField(max_length=255)
    description_about = models.TextField()
    image_about = models.FileField(upload_to="image_about")

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title_about



