# Generated by Django 2.2 on 2019-12-11 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0002_auto_20191211_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answermodel',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
