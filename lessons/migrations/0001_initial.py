# Generated by Django 3.2.9 on 2022-11-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='lessonImage')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Tarihi')),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
    ]