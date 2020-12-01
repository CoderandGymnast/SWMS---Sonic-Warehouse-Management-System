from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

def landing(request):
	if request.user.is_authenticated:
		return render(
			request,
			"landing.html"
		)
	else:
		return HttpResponseRedirect(
			f"{reverse('login')}?next={reverse('landing')}")

def profile(request):
	return render(
		request,
		"registration/profile.html"
	)

def logout(request):
	print("...")
	logout(request)
	return HttpResponseRedirect(reverse("login"))


