import datetime

from django.db import models


class Document(models.Model):
    reg_number = models.AutoField(primary_key=True)
    regist_date = models.CharField(blank=True, null=True, default=datetime.datetime.now().strftime("%m/%d/%Y"),
                                   max_length=20)
    from_person = models.CharField(max_length=100)
    track_number = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    get_date = models.CharField(max_length=30)
    to_person = models.CharField(max_length=100)
    get_type = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    reg_person = models.CharField(max_length=100)
    doc_file = models.FileField(blank=True, upload_to='uploads/' + reg_number.__str__())
