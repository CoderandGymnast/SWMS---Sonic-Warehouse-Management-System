from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.views import generic

from qr_bar_decoder.models import Section, List, Item, Product

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
	logout(request)
	return HttpResponseRedirect(reverse("login"))

def start(request):
	if request.user.is_authenticated:

		section_id = request.GET.get("id", "")
		section = get_object_or_404(Section, pk=section_id)
		items = Item.objects.filter(list__pk=section.list.id)
		products = []
		for item in items:
			products.append(Product.objects.get(pk=item.product.id))

		return render(
			request,
			"start.html",
			{"section_id": section_id, "items": items, "products": products}
		)
	else:
		return HttpResponseRedirect(
			f"{reverse('login')}?next={reverse('start')}")


