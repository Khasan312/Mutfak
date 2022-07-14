from rest_framework import serializers
from .models import FoodRecept, Help

class ReceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodRecept
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Help
        fields = ['help']

