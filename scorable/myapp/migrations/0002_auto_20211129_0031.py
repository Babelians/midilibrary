# Generated by Django 3.2.9 on 2021-11-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='tag_name_0',
        ),
        migrations.RemoveField(
            model_name='score',
            name='tag_name_1',
        ),
        migrations.RemoveField(
            model_name='score',
            name='tag_name_2',
        ),
        migrations.RemoveField(
            model_name='score',
            name='tag_name_3',
        ),
        migrations.RemoveField(
            model_name='score',
            name='tag_name_4',
        ),
        migrations.RemoveField(
            model_name='score',
            name='tag_name_5',
        ),
        migrations.RemoveField(
            model_name='score',
            name='tag_name_6',
        ),
        migrations.RemoveField(
            model_name='score',
            name='tag_name_7',
        ),
        migrations.RemoveField(
            model_name='score',
            name='tag_name_8',
        ),
        migrations.RemoveField(
            model_name='score',
            name='tag_name_9',
        ),
        migrations.AddField(
            model_name='score',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myapp.Tag'),
        ),
    ]
