# Generated by Django 5.1 on 2024-08-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_chatbot_App', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='instructions',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
