# Generated by Django 3.2.8 on 2021-10-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allegy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'allegies',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='allegies',
            field=models.ManyToManyField(to='products.Allegy'),
        ),
    ]
