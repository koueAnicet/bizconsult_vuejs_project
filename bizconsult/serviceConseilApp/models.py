from django.db import models

# Create your models here.
class Reseau_social_team(models.Model)
    facebook_team = models.URLField(null=True)
    twitter_team = models.URLField(null=True)
    linkedin_team = models.URLField(null=True)

class Team(models.Model):
    label_team = models.CharField(max_length=100)
    name_team = models.CharField(max_length=50)
    job_team = models.CharField(max_length=100)
    image_team = models.FileField(upload_to="img_team")
    reseau_social = models.ForeignKey(Reseau_social_team , on_delete=models.CASCADE )
    

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

