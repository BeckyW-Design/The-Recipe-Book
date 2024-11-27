from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)

class RecipeCard(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    servings = models.IntegerField()
    timings = models.IntegerField() 
    tag = models.CharField(max_length=100)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

