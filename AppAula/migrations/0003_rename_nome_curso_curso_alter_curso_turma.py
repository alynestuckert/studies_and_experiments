# Generated by Django 5.2 on 2025-04-06 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAula', '0002_post_autor_post_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='nome',
            new_name='curso',
        ),
        migrations.AlterField(
            model_name='curso',
            name='turma',
            field=models.CharField(max_length=100),
        ),
    ]
