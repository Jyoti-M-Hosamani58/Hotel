# Generated by Django 3.0 on 2024-07-22 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0004_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pracel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=100, null=True)),
                ('bill_date', models.DateField()),
                ('item_code', models.CharField(max_length=100, null=True)),
                ('item_name', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('gst', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('qty', models.IntegerField()),
                ('tax_amt', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('total_gst', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
