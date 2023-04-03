# Generated by Django 4.1.7 on 2023-03-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_result_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('product_name', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
