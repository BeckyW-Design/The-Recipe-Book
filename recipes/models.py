from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=30)
    email = models.EmailField(unique=True, blank=False)

def __str__(self):
        return f"{self.fname} {self.lname}"


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

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(RecipeCard, on_delete=models.CASCADE, related_name="ingredient")
    name = models.CharField(max_length=150)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

    unit_choices = [
        ("grams","Grams"),
        ("kilograms","Kilograms"),
        ("cups","Cups"),
        ("tablespoon","Tablespoon"),
        ("teaspoon","Teaspoon"),
        ("small", "Small"),
        ("medium", "Medium"),
        ("large","Large"),
    ]

    unit = models.CharField(max_length=20, choices=unit_choices)    

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"


class Comment(models.Model):
    RecipeCard = models.ForeignKey(
        RecipeCard, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)



