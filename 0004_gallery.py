# Generated by Django 4.2.4 on 2023-09-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nssps', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='GALLERY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='galleray/image')),
            ],
        ),
    ]