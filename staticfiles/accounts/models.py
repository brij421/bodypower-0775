from django.db import models
from django.forms import ModelForm

class Wallpaper(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly defining the primary key as BigAutoField
    photo = models.FileField(upload_to='wallpaper/')

    def __str__(self):
        return f"Wallpaper {self.id}"

class WallpaperForm(ModelForm):
    class Meta:
        model = Wallpaper
        fields = '__all__'
