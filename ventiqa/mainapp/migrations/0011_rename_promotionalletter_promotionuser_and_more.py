# Generated by Django 4.1.7 on 2023-04-03 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_promotionalletter'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PromotionalLetter',
            new_name='PromotionUser',
        ),
        migrations.AlterModelOptions(
            name='promotionuser',
            options={'verbose_name_plural': 'Promotion Users'},
        ),
    ]
