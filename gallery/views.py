from django.views import generic
from .models import Painting


class Gallery(generic.TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        pictures = Painting.objects.all()

        context = {
            'pictures': pictures
        }

        return context
    

class Gallery_list(generic.ListView):
    model = Painting
    template_name = 'paintings_list.html'
    
    # def get_queryset(self):
    #     queryset = Painting.objects.all()
    #     return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        pictures = Painting.objects.all()

        context = {
            'pictures': pictures
        }

        return context




