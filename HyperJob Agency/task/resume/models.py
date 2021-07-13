from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.conf import settings


class Resume(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


