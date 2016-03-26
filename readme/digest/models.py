from markdown import markdown
from django.db import models

class GuoKe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    content = models.TextField()
    time = models.CharField(max_length=128)
    author_url = models.URLField()

    def __unicode__(self):
        return self.title
    

