# Generated by Django 4.2.1 on 2023-06-07 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_alter_board_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
