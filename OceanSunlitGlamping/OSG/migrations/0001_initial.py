# Generated by Django 5.0.1 on 2024-02-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='帳號')),
                ('password', models.CharField(max_length=64, verbose_name='密碼')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密碼')),
                ('age', models.IntegerField(verbose_name='年齡')),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='薪資')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='入職時間')),
            ],
        ),
    ]
