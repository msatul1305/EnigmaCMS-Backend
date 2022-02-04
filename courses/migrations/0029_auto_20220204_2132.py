# Generated by Django 3.2.5 on 2022-02-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0028_auto_20220204_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Android', 'Android'), ('Web', 'Web'), ('Backend', 'Backend'), ('ML/AI', 'ML/AI'), ('UI/UX', 'UI/UX'), ('AR/VR', 'AR/VR'), ('CP', 'Competative Programming')], max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='home_page_display',
            field=models.CharField(blank=True, choices=[('Featured', 'Featured'), ('Exclusive', 'Exclusive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published'), ('Rejected', 'Rejected'), ('Created', 'Created')], default='Draft', max_length=20),
        ),
        # migrations.RemoveField(
        #     model_name='article',
        #     name='tag',
        # ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to='courses.Tag'),
        ),
    ]
