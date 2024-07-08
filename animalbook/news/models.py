from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
