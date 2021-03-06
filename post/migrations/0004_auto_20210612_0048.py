# Generated by Django 3.2.1 on 2021-06-12 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210602_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('memo', 'MEMO'), ('algorithm', 'ALGORITHM'), ('weddew', 'WEDDEW'), ('dotori postoffice', 'DOTORI POSTOFFICE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_choices',
            field=models.CharField(choices=[('workout', 'WORKOUT'), ('algorithm', 'ALGORITHM'), ('software development', 'SOFTWARE DEVELOPMENT'), ('reading', 'READING'), ('dotori postoffice', 'DOTORI POSTOFFICE'), ('weddew', 'WEDDEW')], max_length=100),
        ),
    ]
