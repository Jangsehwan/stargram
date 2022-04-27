# Generated by Django 4.0.3 on 2022-04-14 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='질문')),
                ('category', models.TextField(choices=[('일반', '일반'), ('계정', '계정'), ('기타', '기타')], verbose_name='카테고리')),
                ('answer', models.TextField(verbose_name='답변')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='작성일')),
                ('last_modified_writter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
