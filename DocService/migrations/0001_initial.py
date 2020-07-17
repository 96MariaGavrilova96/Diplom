# Generated by Django 3.0.8 on 2020-07-12 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('reg_number', models.IntegerField(primary_key=True, serialize=False)),
                ('from_person', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('to_person', models.CharField(max_length=100)),
                ('get_type', models.CharField(max_length=200)),
                ('doc_type', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
                ('text_html', models.FileField(upload_to='uploads/<django.db.models.fields.IntegerField>')),
            ],
        ),
    ]
