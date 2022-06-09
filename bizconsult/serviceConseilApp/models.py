from django.db import models

# Create your models here.
class Service(models.Model):
    
    icon_service = models.CharField(max_length=30)
    title_service = models.CharField(max_length=30)
    description_service = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

class Reseau_social_team(models.Model):
    facebook_team = models.URLField(null=True)
    twitter_team = models.URLField(null=True)
    linkedin_team = models.URLField(null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    
class Team(models.Model):
    
    name_team = models.CharField(max_length=50)
    last_name_team = models.CharField(max_length=100)
    job_team = models.CharField(max_length=100)
    image_team = models.FileField(upload_to="img_team")
    reseau_social = models.ForeignKey(Reseau_social_team , on_delete=models.CASCADE )

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.name_team

class Testimonial(models.Model):
    name_Testimonial = models.CharField(max_length=50)
    works_Testimonial = models.CharField(max_length=50)
    comment_Testimonial = models.TextField()
    image_Testimonial = models.FileField(upload_to="img_testimonial")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name_Testimonial