# Generated by Django 3.2.5 on 2021-07-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdid', models.CharField(max_length=70)),
                ('stdemail', models.EmailField(max_length=70)),
                ('stdpass', models.CharField(max_length=70)),
            ],
        ),
    ]