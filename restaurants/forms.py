# encoding: utf-8
#表單模型化
from django import forms

class CommentForm(forms.Form):
    visitor = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 20, required = False) #required = False表示並非必填
    content = forms.CharField(max_length = 200, widget = forms.Textarea())
    
    #自定義驗證規則
    def clean_content(self):
    	content = self.cleaned_data['content']
    	if len(content) < 5:
    		raise forms.ValidationError('字數不足')
    	return content