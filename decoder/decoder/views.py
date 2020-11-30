from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def landing(request):
	if request.user.is_authenticated:
		return render(
			request,
			"landing.html"
		)
	else:
		return HttpResponseRedirect(
			f"{reverse('login')}?next={reserve('landing')}")

def profile(request):
	return render(
		request,
		"registration/profile.html"
	)
