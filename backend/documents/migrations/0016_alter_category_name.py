# Generated by Django 4.2.4 on 2023-09-14 04:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0015_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, help_text='Введите категорию документа', max_length=55, validators=[django.core.validators.RegexValidator], verbose_name='Категория'),
        ),
    ]