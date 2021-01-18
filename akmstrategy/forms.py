from django import forms

class DiscussTheProjectForm(forms.Form):

    name = forms.CharField(max_length=255,
                           label='',
                           required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'my-2 p-3 w-75',
                                   'placeholder': 'Имя'
                               })
                           )
    phone = forms.CharField(max_length=255,
                            label='',
                            required=True,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'my-2 p-3 w-75',
                                    'placeholder': 'Телефон'
                                })
                           )
    description = forms.CharField(label='',
                                  max_length=255,
                                  required=True,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'my-2 mb-3 p-3 w-75',
                                          'placeholder': 'Коротко опишите задачу'
                                      })
                                  )