# Generated by Django 4.2.6 on 2024-04-01 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 1, 4, 53, 0, 686325, tzinfo=datetime.timezone.utc), verbose_name='published date'),
        ),
    ]
