# Generated by Django 3.0.8 on 2020-09-02 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
