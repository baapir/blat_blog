#from django.contrib.auth.models import User
from .models import Blat
import django_filters

class BlatFilter(django_filters.FilterSet):
    class Meta:
        model = Blat
        fields = ['charactor', ]
