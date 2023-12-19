# Generated by Django 4.2.5 on 2023-12-19 14:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_choice_voted_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='voted_users',
        ),
        migrations.AddField(
            model_name='post',
            name='voted_users',
            field=models.ManyToManyField(blank=True, related_name='voted_choices', to=settings.AUTH_USER_MODEL),
        ),
    ]
