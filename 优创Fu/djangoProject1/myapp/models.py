from django.db import models


# Create your models here.

class book(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

class Project(models.Model):
    projectname = models.CharField(max_length=45)       # 对应 VARCHAR(45)
    projectteam = models.CharField(max_length=45)       # 对应 VARCHAR(45)
    projectpeople = models.IntegerField()               # 对应 INT
    companysituation = models.CharField(max_length=255) # 对应 VARCHAR(255)
    projectdescription = models.CharField(max_length=255) # 对应 VARCHAR(255)
    #image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # 新增字段

    def __str__(self):
        return f"Feedback by {self.name or 'Anonymous'}"
