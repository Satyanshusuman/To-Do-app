# Generated by Django 4.2.1 on 2023-07-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_tasks_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
