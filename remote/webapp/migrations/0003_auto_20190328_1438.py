# Generated by Django 2.1.7 on 2019-03-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190316_0303'),
    ]

    operations = [
        migrations.CreateModel(
            name='command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]