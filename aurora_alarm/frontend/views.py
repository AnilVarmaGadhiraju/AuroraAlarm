from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.list import ListView
from models import PhotoWithLocation


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class AuroralActivityView(generic.TemplateView):
    template_name = 'auroral_activity.html'


class AlarmsView(generic.TemplateView):
    template_name = 'alarms.html'


class GalleryView(generic.TemplateView):
    template_name = 'gallery.html'


class MapView(generic.TemplateView):
    template_name = 'map.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class PhotoWithLocationView(object):
    queryset = PhotoWithLocation.objects.order_by("-id")


class PhotoWithLocationListView(PhotoWithLocationView, ListView):
    paginate_by = 8


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

