from django.db import models

# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    addr = models.TextField()
    status = models.IntegerField()

    class Meta:
        ordering = ('created',)

class books(models.Model):
    name = models.CharField(max_length=10)
    descr = models.CharField(max_length=10)
    status = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='user_profile', on_delete=models.CASCADE, )

