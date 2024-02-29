from django.forms import ModelForm
from captcha.fields import CaptchaField
from .models import CustomUser

class SubmissionForm(ModelForm):
  captcha = CaptchaField()

  class Meta:
    model = CustomUser
    fields = ('name', 'email', 'phone', 'company', 'message')

  