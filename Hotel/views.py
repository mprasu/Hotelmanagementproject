from django.shortcuts import render
from django.views.generic import TemplateView
from Hotel.models import HotelSuprabat
# Create your views here.
class HotelListView(TemplateView):
	template_name = 'hotel-list.html'
	def get_context_data(self, *args, **kwargs):
		return {'hotelrecs':HotelSuprabat.objects.all()}