# Generated by Django 3.2.5 on 2021-07-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('details', models.CharField(max_length=100, null=True)),
                ('Seeds', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
            ],
        ),
    ]