# Generated by Django 4.2.6 on 2023-11-11 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_produto_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
