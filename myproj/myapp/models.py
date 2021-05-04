from django.db import models

# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    addr = models.TextField()
    status = models.IntegerField()

    class Meta:
        ordering = ('created',)


