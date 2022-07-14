from rest_framework import viewsets
from .serializers import ReceptSerializer, HelpSerializer
from food.models import FoodRecept, Help
from rest_framework.generics import ListAPIView

class FoodReceptViewSet(viewsets.ModelViewSet):
    queryset = FoodRecept.objects.all()
    serializer_class = ReceptSerializer



class HelpView(ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer