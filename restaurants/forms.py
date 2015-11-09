# encoding: utf-8
#表單模型化
from django import forms

class CommentForm(forms.Form):
    visitor = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 20, required = False) #required = False表示並非必填
    content = forms.CharField(max_length = 200, widget = forms.Textarea())