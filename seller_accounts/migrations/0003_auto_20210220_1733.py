# Generated by Django 3.1.6 on 2021-02-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_accounts', '0002_auto_20210207_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='about',
            field=models.TextField(),
        ),
    ]
