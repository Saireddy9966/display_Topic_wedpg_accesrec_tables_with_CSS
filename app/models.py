from django.db import models

# Create your models here.
class Topic(models.Model):
    game_name=models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.game_name

class webpage(models.Model):
    pno=models.IntegerField()
    game_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField()
    def __str__(self):
        return self.name

class acessrecord(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return self.author