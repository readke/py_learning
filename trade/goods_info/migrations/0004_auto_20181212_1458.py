# Generated by Django 2.1 on 2018-12-12 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods_info', '0003_auto_20181212_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_country',
            name='goods',
            field=models.ForeignKey(db_column='db_column ', on_delete=django.db.models.deletion.CASCADE, to='goods_info.goods'),
        ),
    ]
