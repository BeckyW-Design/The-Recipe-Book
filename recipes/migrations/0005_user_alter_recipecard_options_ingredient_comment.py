# Generated by Django 4.2.16 on 2024-11-29 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipecard_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='recipecard',
            options={'ordering': ['-created_on']},
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unit', models.CharField(choices=[('grams', 'Grams'), ('kilograms', 'Kilograms'), ('cups', 'Cups'), ('tablespoon', 'Tablespoon'), ('teaspoon', 'Teaspoon'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=20)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='recipes.recipecard')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('RecipeCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipes.recipecard')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to='recipes.user')),
            ],
        ),
    ]