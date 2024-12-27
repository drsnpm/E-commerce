# Generated by Django 5.0.6 on 2024-05-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_products_description_alter_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('uname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]