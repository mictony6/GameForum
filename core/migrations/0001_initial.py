# Generated by Django 4.1.1 on 2022-09-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
    ]
