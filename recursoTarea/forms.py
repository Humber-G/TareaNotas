from django import forms
from django.forms import fields
from .models import Nota

class NotaFormulario(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NotaFormulario, self).__init__(*args, **kwargs)

        for campoVisible in self.visible_fields():
            campoVisible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Nota
        fields = '__all__'