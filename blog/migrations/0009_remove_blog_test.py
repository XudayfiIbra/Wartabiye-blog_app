# Generated by Django 4.2.6 on 2024-05-08 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='test',
        ),
    ]