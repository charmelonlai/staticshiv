from django.shortcuts import render
from django.http import HttpResponseRedirect
from staticshiv.apps.register.forms import UserCreateForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_check(user):
	if user is not None and user.is_active:
		return True
	return False

class TestView(FormView):
	