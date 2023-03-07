from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=255,null=True)
    mdp=models.CharField(max_length=255,null=True)
    currentscore=models.IntegerField()
    topscore=models.IntegerField()
    level=models.IntegerField()
    def __str__(self):
        return self.username,self.mdp,str(self.score)
