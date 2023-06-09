# Generated by Django 4.2.1 on 2023-06-13 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0023_delete_commentt'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.trainer')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.board')),
            ],
            options={
                'verbose_name': '댓글T',
                'verbose_name_plural': '댓글T',
                'db_table': 'commentT',
            },
        ),
    ]
