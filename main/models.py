from django.db import models
from django.core.files.storage import default_storage

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/')

    def delete(self, *args, **kwargs):
        if self.image and default_storage.exists(self.image.name):
            default_storage.delete(self.image.name)

        super().delete(*args, **kwargs)
    def __str__(self):
        return f'Image {self.id}'
