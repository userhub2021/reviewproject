# Generated by Django 3.2.9 on 2022-01-11 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewpost', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='userful_review',
            new_name='useful_review',
        ),
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='userful_review_record',
            new_name='useful_review_record',
        ),
    ]
