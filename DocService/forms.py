import datetime

from django import forms
from DocService.models import Document


class DateInput(forms.DateInput):
    input_type = 'date'


class DocForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('reg_number', 'regist_date', 'from_person', 'description', 'get_date', 'to_person', 'get_type',
                  'doc_type', 'comment', 'doc_file', 'reg_person', 'track_number')
        widgets = {
            'from_person': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'get_date': DateInput(attrs={'class': 'form-control'}),
            'to_person': forms.TextInput(attrs={'class': 'form-control'}),
            'get_type': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_type': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'track_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(DocForm, self).__init__(*args, **kwargs)
        self.fields['get_date'].input_formats = ['%d.%m.%Y']
        self.fields['reg_person'].required = False
        self.fields['comment'].required = False
