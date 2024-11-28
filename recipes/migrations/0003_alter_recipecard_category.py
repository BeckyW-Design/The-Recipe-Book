# Generated by Django 4.2.16 on 2024-11-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipecard_category_alter_recipecard_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipecard',
            name='category',
            field=models.CharField(choices=[('GF', 'Gluten Free'), ('QM', '20mins or less'), ('Vg', 'Vegan'), ('V', 'Vegetarian')], max_length=2),
        ),
    ]
