from rest_framework import serializers
from .models import drink

class DrinkSerializer(serializers.ModelSerializer):

    class Meta: 
        model = drink
        fields = '__all__'

        read_only_fields = ('id',)