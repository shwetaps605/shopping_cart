# Generated by Django 3.0.7 on 2020-06-08 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=50.0)),
            ],
        ),
    ]
