from django.db import models

# Create your models here.
class photo(models.Model):
    title = models.CharField(max_length=200 )
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
                                     
      