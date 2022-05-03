from random import choices
import django
from django import forms

from .models import Post

from django.core.exceptions import ValidationError


# class PostBaseForm(forms.Form):
#     CATEGPRY_CHOICES = [
#         ('1', '일반'),
#         ('2', '계정'),
#     ]

#     image = forms.ImageField(label="이미지")
#     # forms에서는 TextField를 제공해주지않아서 widget으로 해결
#     content = forms.CharField(label="내용", widget=forms.Textarea, required=True)
#     category = forms.ChoiceField(label="카테고리", choices=CATEGPRY_CHOICES)


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


# 기존에 baseform을 정의에두고 커스텀해서 사용
class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']

# 유효성검사에 대한 custum - def clean_filedname
    def clean_content(self):
        data = self.cleaned_data['content']
        if "비속어" == data:
            raise ValidationError("비속어는 사용하실수 없습니다")
        return data


class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']


class PostDetailForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super(PostDetailForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            key.fields[key].widget.attrs['disabled'] = True
