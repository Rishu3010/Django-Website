# Generated by Django 4.1.7 on 2023-03-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_subscription_subscription_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(default='', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscription_id',
            field=models.IntegerField(default='', primary_key=True, serialize=False),
        ),
    ]