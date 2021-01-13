# Generated by Django 3.0.1 on 2021-01-13 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210106_0854'),
        ('order', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Variants'),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Variants'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(editable=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled')], default='New', max_length=10),
        ),
    ]