# Generated by Django 3.2 on 2021-12-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_theme_background_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='background_color',
            field=models.CharField(choices=[('red', 'red'), ('pink', 'pink'), ('lightpink', 'light pink'), ('lightgreen', 'light green'), ('orange', 'orange'), ('yellow', 'yellow'), ('lightgoldenrodyellow', 'light yellow'), ('green', 'green'), ('blue', 'blue'), ('lightblue', 'light blue'), ('Indigo', 'indigo'), ('white', 'white')], default='#474444 ', max_length=150),
        ),
    ]
