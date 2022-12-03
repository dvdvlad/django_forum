# Generated by Django 4.1 on 2022-12-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('user_creater', models.CharField(max_length=50, verbose_name='Никнейм пользователя')),
            ],
        ),
    ]
