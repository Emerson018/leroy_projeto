# Generated by Django 4.2.6 on 2023-11-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0008_produto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='avaliacoes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/'),
        ),
    ]