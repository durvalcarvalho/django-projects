from django.db import models
from django.core.files.base import ContentFile

from PIL import Image
from io import BytesIO
import numpy as np

from photos.utils import get_filtered_image


class Upload(models.Model):
    class ActionChoices(models.TextChoices):
        NO_FILTER = 'NO_FILTER', 'No Filter'
        COLORIZED = 'COLORIZED', 'Colorized'
        GRAYSCALE = 'GRAYSCALE', 'Grayscale'
        BLURRED = 'BLURRED', 'Blurred'
        BINARY = 'BINARY', 'Binary'
        INVERT = 'INVERT', 'Invert'

    image = models.ImageField(upload_to='images')
    action = models.CharField(
        max_length=20,
        choices=ActionChoices.choices,
        default=ActionChoices.NO_FILTER,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        img = Image.open(self.image)

        cv_img = np.array(img)
        img = get_filtered_image(cv_img, self.action)

        im_pil = Image.fromarray(img)

        buffer = BytesIO()
        im_pil.save(buffer, format='JPEG')
        img_png = buffer.getvalue()

        self.image.save(
            str(self.image),
            ContentFile(img_png),
            save=False
        )

        super().save(*args, **kwargs)