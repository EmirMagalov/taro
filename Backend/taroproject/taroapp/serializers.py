from rest_framework import serializers
from .models import TaroCard

class TaroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaroCard
        fields = "__all__"



