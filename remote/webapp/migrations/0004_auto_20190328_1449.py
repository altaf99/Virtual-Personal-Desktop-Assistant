# Generated by Django 2.1.7 on 2019-03-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190328_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='done',
            field=models.CharField(default='false', max_length=10),
        ),
    ]