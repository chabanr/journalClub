# Generated by Django 2.1.7 on 2019-04-26 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190425_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_test',
            new_name='choice_text',
        ),
    ]
