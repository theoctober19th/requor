# Generated by Django 2.2 on 2019-12-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answermodel',
            options={'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='questionmodel',
            options={'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterField(
            model_name='answermodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='answer_images'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question_images'),
        ),
    ]
