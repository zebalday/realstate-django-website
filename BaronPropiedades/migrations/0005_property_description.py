# Generated by Django 4.0.6 on 2024-02-05 23:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BaronPropiedades', '0004_alter_client_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Breve descripción'),
        ),
    ]