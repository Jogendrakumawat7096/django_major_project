# Generated by Django 5.0 on 2023-12-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='User_images/')),
                ('user_type', models.CharField(default='buyer', max_length=100)),
            ],
        ),
    ]
