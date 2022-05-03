from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class UserCreateForm(UserBaseForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserBaseForm.Meta):
        fields = ['username', 'email', 'phone', 'password']


# 장고에서 만들어놓은 UserCreationForm을 가져다쓰는걸 추천
class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email']


class LoginFrom():
    pass
