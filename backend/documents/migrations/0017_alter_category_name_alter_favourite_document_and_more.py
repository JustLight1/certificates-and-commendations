# Generated by Django 4.2.4 on 2023-09-21 03:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0016_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, help_text='Введите категорию документа', max_length=55, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Название должно содержать буквы кириллицы', regex='^[А-Яа-я]+$')], verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite', to='documents.document', verbose_name='Шаблон в избранном'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
