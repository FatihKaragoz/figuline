# Generated by Django 2.2.7 on 2019-12-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_about_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='productContain',
            field=models.CharField(max_length=1000, verbose_name='Ürün açıklaması'),
        ),
    ]
