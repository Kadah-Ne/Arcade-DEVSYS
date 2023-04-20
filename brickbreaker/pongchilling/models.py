from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255,null=True)
    mdp=models.CharField(max_length=255,null=True)
    currentscore=models.IntegerField(null=True)
    topscore=models.IntegerField(null=True)
    level=models.IntegerField(null=True)
    def __str__(self):
        return self.username+","+self.mdp+","+str(self.currentscore)
