# Generated by Django 5.1.6 on 2025-02-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_alter_categorynumenclature_options'),
        ('tasks', '0002_task_sla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='sla',
            field=models.ManyToManyField(blank=True, null=True, to='settings.categorynumenclature', verbose_name='sla'),
        ),
    ]
