from django.shortcuts import render
from .models import photo

# Create your views here.
def photo_list(request):
    queryset = photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, "templates",context)