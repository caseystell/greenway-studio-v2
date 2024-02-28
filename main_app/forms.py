from django import forms
from captcha.fields import CaptchaField
from .models import CustomUser

class SubmissionForm(forms.Form):
  captcha = CaptchaField()

  class Meta:
    model = CustomUser
    fields = '__all__'

  