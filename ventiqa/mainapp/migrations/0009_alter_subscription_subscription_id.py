# Generated by Django 4.1.7 on 2023-03-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_remove_subscription_id_subscription_subscription_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscription_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]