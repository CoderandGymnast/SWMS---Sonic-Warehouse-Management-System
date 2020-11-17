from django.urls import path
from . import views

app_name = "qr_bar_decoder"
urlpatterns = [
	path('', views.index, name="index"),
]
