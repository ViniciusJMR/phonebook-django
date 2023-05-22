from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from . import models

#Three ways to config fields
class ContactForm(forms.ModelForm):
    # First
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class-a',
                'placeholder': 'Escreva Aqui',
            }
        ),
        label='First Name',
        help_text='Text de ajuda para seu usuário',
    )

    # Second
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'class-a',
    #         'placeholder': 'Escreva Aqui',
    #     })

    def clean(self): 
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid',
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não insira ABC neste campo',
                    code='invalid',
                )
            )
        return first_name 


    class Meta:
        model = models.Contact 
        fields = ('first_name','last_name','phone',)
        # Third
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'class',
        #             'placeholder': 'Escreva Aqui',
        #         }
        #     )
        # }
        
    