from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=4)

class Document(models.Model):
    updated_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    expiration_date = models.DateTimeField(blank=True, null=True)
    expired = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        s = ''

        if self.expired:
            s += '[EXPIRED] '

        s += f'{self.updated_file.name} - Expires: {self.expiration_date}'

        return s


