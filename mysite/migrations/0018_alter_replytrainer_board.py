# Generated by Django 4.2.1 on 2023-06-10 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_alter_replytrainer_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replytrainer',
            name='board',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mysite.board'),
        ),
    ]