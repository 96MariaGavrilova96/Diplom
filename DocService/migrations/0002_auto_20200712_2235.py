# Generated by Django 3.0.8 on 2020-07-12 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DocService', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='text_html',
            new_name='doc_file',
        ),
    ]