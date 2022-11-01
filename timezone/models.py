from time import time
from django.db import models


class Timezone(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
