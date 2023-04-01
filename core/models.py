import magic
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models

ext_validator = FileExtensionValidator(["png", "jpg", "pdf"])


def validate_file_mimetype(file):
    accept = ["image/png", "image/jpeg", "application/pdf"]
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    print(file_mime_type)
    if file_mime_type not in accept:
        raise ValidationError("Unsupported file type")


class Dog(models.Model):
    name = models.CharField(max_length=64)
    image = models.FileField(
        upload_to="dogs/", validators=[ext_validator, validate_file_mimetype]
    )

    def __str__(self):
        return self.name

    def delete(self):
        self.image.delete()
        super().delete()
