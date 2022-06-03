from django.db import models



class Color(models.Model):
    hexcode = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hexcode
