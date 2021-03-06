# Generated by Django 3.2.4 on 2021-06-29 20:41

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Education', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='Education', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
