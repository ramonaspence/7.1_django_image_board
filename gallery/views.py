from django.views.generic import TemplateView
from .models import Painting

class Gallery(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        pictures = Painting.objects.all()

        context = {
            'pictures': pictures
        }

        return context



# Create your views here.
