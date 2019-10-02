from django.contrib import admin
from .models import photo

# Register your models here.
class photoAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]
    
    class Meta:
        model = photo
        
admin.site.register(photo, photoAdmin)        
    
