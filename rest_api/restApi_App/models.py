from django.db import models

# Create your models here.
# class Location(models.Model):
#     locationName = models.TextField(max_length=100, unique=True)

#     def __str__(self):
#         return self.locationName
    

class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)



    def __str__(self):
        return self.title