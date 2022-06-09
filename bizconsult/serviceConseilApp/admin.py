from django.contrib import admin
from serviceConseilApp.models import *
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Service)
admin.site.register(Reseau_social_team)
admin.site.register(Testimonial)

@admin.register(Team)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'name_team', 'job_team', 'reseau_social', 'created_at', 'updated_at','deleted_at')
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image_team.url}" style="height:100px; width:200px">')