# Generated by Django 4.2.4 on 2023-10-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanagement', '0006_alter_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='brand',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='starting_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
