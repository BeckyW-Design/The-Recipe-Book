from django.db import models
from recipes.models import RecipeCard

# Create your models here.
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
