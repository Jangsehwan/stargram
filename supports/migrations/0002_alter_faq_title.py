# Generated by Django 4.0.3 on 2022-04-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='title',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='질문 제목'),
        ),
    ]