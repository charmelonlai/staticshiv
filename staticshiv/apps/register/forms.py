from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.form.util import ErrorList
from captcha.fields import CaptchaField

class UserCreateForm(UserCreateForm):

	captcha = CaptchaField()

	class Meta:
		model = User
		field = ("username","email","password1","password2","captcha")

	def clean_username(self):
		username = self.cleaned_data["username"]
		try:
			User._default_manager.get(username__iexact=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(
			self.error_messages['duplicate_username'],
			code = 'duplicate_username',
		)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email__iexact = email).exclude(username=username).count():
			raise forms.ValidationError(u'Email address must be unique.')
		return email

	class LoginForm(AuthenticationForm):
		remember_me = forms.BooleanField(required=False)
