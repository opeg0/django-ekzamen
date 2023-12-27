from django import forms
from django.utils.translation import gettext_lazy as _
from .models import User, Penalty


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=150, label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=150, label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)
        labels = {
            'username': _('Логин'),
        }
        help_texts = {
            'username': None,
        }

    def password_confirm(self):
        validate = self.cleaned_data
        if validate['password'] != validate['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return validate['password2']

class UserAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=150, label='Логин')
    password = forms.CharField(max_length=150, label='Пароль', widget=forms.PasswordInput)

class PenaltyForm(forms.ModelForm):
    class Meta:
        model = Penalty
        fields = '__all__'
        labels = {
            'name': _('Номер автомобиля'),
            'description': _('Описание'),
            'penalty_type': _('Тип штрафа')
        }