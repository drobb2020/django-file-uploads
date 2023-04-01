from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='dogs/')

    def __str__(self):
        return self.name

    def delete(self):
        self.image.delete()
        super().delete()
