# Generated by Django 4.2.6 on 2024-05-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='test',
            field=models.CharField(max_length=223, null=True),
        ),
    ]
