from rest_framework import serializers
from sendurls.models import Urlinput


class UrlinputSerializer(serializers.ModelSerializer):  # default create i save method
    class Meta:
        model =Urlinput
        fields=['id','url_input']
#class UrlinputSerializer(serializers.Serializer):
#   id=serializers.IntegerField()
#   url_input=serializers.CharField(max_length=100,required=True)
#   # maila > format  code = serializers.CharField(style={'base_template': 'textarea.html'})
#
#   def create(self, validated_data):     #POST
#       return Urlinput.objects.create(**validated_data)
#
#   def update(self, instance, validated_data):
#       instance.url_input=validated_data.get('url_input',instance.url_input)
#       instance.save()
#       return instance


# form > formClasses Django

