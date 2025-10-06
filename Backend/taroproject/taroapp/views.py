from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render,HttpResponse
from .serializers import TaroSerializer
from .models import TaroCard
from rest_framework import viewsets
def test(request):
    return HttpResponse('test')

@method_decorator(cache_page(60 * 5),name='list')
class TaroViewSet(viewsets.ModelViewSet):
    serializer_class = TaroSerializer

    def get_queryset(self):
        return TaroCard.objects.all()



