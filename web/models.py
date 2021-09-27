from django.db import models


# Create your models here.
class note(models.Model):
    nid = models.AutoField(primary_key=True)
    text = models.CharField(max_length=300)
    img = models.ImageField(upload_to='media/')
    date = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    
