# Generated by Django 4.2.6 on 2023-11-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_remove_produto_id_alter_produto_lm'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='link',
            field=models.URLField(default='www.leroymerlin.com.br'),
            preserve_default=False,
        ),
    ]