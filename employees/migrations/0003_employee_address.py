# Generated by Django 2.1.2 on 2019-01-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20181230_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
