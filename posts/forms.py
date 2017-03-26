from django import forms
from . import models


class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post  # 声明一下我使用的是models.Post这个model
        fields = [
            "title",
            "content"
        ]

