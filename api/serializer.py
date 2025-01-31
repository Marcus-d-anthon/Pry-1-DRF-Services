from rest_framework import serializers
from .models import DatosProgramadores

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosProgramadores
        fields = '__all__'