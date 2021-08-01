from rest_framework import serializers
from .models import Pokemon, Types

class TypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Types
        fields = ['id', 'name']
        # fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):

    type_ids = TypesSerializer(read_only=True, many=True)
    
    class Meta:
        model = Pokemon 
        # add all fields
        fields = '__all__'
        # get nested data
        # depth = 1

    
    # def get_type_ids(self, obj):

    #     type_ids = Types.objects.order_by('-id')
    #     return TypesSerializer(type_ids, read_only=True, many=True, context=self.context)