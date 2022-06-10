from django.contrib import admin
from webApp.models import *

# Register your models here.
admin.site.register(Site_info)
admin.site.register(Banner)
admin.site.register(Social_Network)

admin.site.register(Feature)
admin.site.register(About)

@admin.register(Potentialite)
class PotentialiteAdmin(admin.ModelAdmin):
    list_display = ('Icon', 'title','description','created_at', 'updated_at','deleted_at')



# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name_contact",
        "email_contact",
        "comments_contact",
        "created_at",
        "updated_at",
        "deleted_at",
    ) 