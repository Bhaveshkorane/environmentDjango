# Generated by Django 4.2.13 on 2024-07-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='empDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='emp',
        ),
    ]
