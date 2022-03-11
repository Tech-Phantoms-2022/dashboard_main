from django.db import models

# Create your models here.
class Hash(models.Model):
    id = models.IntegerField(primary_key=True)
    hash_id = models.IntegerField()
    frequency = models.CharField(max_length=70)
    # metadata = models.CharField(max_length=70)
    flag = models.BooleanField()
    
