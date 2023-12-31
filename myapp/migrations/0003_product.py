# Generated by Django 5.0 on 2023-12-08 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_signup_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('product_price', models.PositiveIntegerField()),
                ('product_category', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('kids', 'kids')], max_length=100)),
                ('product_brand', models.CharField(choices=[('luvis', 'luvis'), ('Diesel', 'Diesel'), ('polo', 'polo')], max_length=100)),
                ('product_size', models.CharField(choices=[('s', 's'), ('l', 'l'), ('xl', 'xl'), ('xxl', 'xxl')], max_length=100)),
                ('product_desc', models.TextField()),
                ('product_fimage', models.ImageField(upload_to='product_image/')),
                ('product_bimage', models.ImageField(upload_to='product_image/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.signup')),
            ],
        ),
    ]
