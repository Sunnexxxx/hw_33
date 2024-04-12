# Generated by Django 5.0.4 on 2024-04-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password_reset_link', models.CharField(max_length=255)),
                ('needs_password_reset', models.BooleanField(default=True)),
            ],
        ),
    ]