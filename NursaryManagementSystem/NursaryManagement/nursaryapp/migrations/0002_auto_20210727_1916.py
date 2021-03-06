# Generated by Django 3.2.5 on 2021-07-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursaryapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='Seeds',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='batch',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='details',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
