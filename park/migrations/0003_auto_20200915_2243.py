# Generated by Django 3.0.3 on 2020-09-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0002_tblticket_postingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblticket',
            name='postingdate',
            field=models.DateField(auto_now=True),
        ),
    ]
