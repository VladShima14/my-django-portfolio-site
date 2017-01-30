from django.conf import settings
from .forms import ContactForm
from .models import Topic, SliderItem


def agro(request):
    
    return {'topics': Topic.objects.all(),
            'items': SliderItem.objects.all(),
            'form': ContactForm(),
            }