from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('shorten', csrf_exempt(views.shorten_post)),
    path('<short_code>/stats', csrf_exempt(views.short_code_get_stats)),
    path('<short_code>', csrf_exempt(views.short_code_get)),
]

