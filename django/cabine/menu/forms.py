import django.forms as forms


class ClipForm(forms.Form):
    cover = forms.FileField(
        label='Selecione o arquivo',
        help_text='max. 42 megabytes'
    )
