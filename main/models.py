from django.db import models


class PushbulletClient(models.Model):
    access_token = models.CharField(max_length=64, unique=True)
    signed_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.access_token
