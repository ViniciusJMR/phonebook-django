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
    