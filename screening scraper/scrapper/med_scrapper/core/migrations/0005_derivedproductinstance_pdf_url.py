# Generated by Django 5.2 on 2025-05-22 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_derivedproductinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='derivedproductinstance',
            name='pdf_url',
            field=models.URLField(blank=True, help_text='pdf url for the product item', max_length=1000, null=True),
        ),
    ]
