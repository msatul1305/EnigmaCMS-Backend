# Generated by Django 3.2.5 on 2021-11-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20211106_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Draft', 'Draft'), ('Created', 'Created'), ('Published', 'Published')], default='Draft', max_length=20),
        ),
    ]