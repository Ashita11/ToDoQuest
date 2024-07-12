from django.db import models

class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

class listitem(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE,null= True,blank= True)
    name=models.CharField(max_length=100)

class tasks(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE,null= True,blank= True)
    list=models.ForeignKey(listitem,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    desc=models.TextField()
    due_date=models.DateField()
    completed=models.BooleanField(default=False)
    priority = models.CharField(max_length=10)
