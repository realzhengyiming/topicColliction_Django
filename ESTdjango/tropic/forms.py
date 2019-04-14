

from django import forms
from captcha.fields import CaptchaField

class CaptchaTestForm(forms.Form):
    # form对注册表单的验证
    username = models.CharField(required=True,max_length=16)
    
    password = forms.CharField(required=True, min_length=16)  #密码的长度
    # 验证码,参数：错误信息 
    captcha = CaptchaField(error_messages={'invalid': '验证码错误啊'})

