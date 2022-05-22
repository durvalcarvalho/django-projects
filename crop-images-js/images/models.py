from django.db import models

class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.file} - Uploaded at {self.uploaded_at}'

    class Meta:
        ordering = ('uploaded_at',)

