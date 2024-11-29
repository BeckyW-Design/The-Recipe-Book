from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class RecipeCard(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    servings = models.IntegerField()
    timings = models.IntegerField() 
    tag = models.SlugField(max_length=100)

    category_choices = [
        ('GF', 'Gluten Free'),
        ('QM', '20mins or less'),
        ('Vg', 'Vegan'),
        ('V', 'Vegetarian')
    ]
    category = models.CharField(max_length=2, choices=category_choices)
    method = models.TextField(null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title



