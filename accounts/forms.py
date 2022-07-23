from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'gender']

        labels = {
            'username': 'ID',
            'password': 'PASSWORD',
            'first_name': 'NAME',
            'gender': 'GENDER'
        }
        widgets = {
            "username": forms.TextInput(attrs={
                'placeholder': '아이디를 입력하세요',
                'name': 'username',
                'style': 'font-size: 18px; height: 24px',
                'class': 'form-item-input'
            }),
            "password": forms.PasswordInput(attrs={
                'placeholder': '숫자, 영문 포함 8자리 이상',
                'name': 'password',
                'style': 'font-size: 18px; height: 24px',
                'class': 'form-item-input'
            }),
            "first_name": forms.TextInput(attrs={
                'placeholder': '닉네임을 입력하세요',
                'name': 'name',
                'style': 'font-size: 18px; height: 24px',
                'class': 'form-item-input',
            }),
            "gender": forms.RadioSelect()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user
