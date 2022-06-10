from django.contrib import admin
from serviceConseilApp.models import *
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Service)

admin.site.register(Testimonial)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'name_team', 'job_team', 'created_at', 'updated_at','deleted_at')
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image_team.url}" style="height:100px; width:150px">')

@admin.register(Reseau_social_team)
class ReseauAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon','link', 'team','created_at', 'updated_at','deleted_at')