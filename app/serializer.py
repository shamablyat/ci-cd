from rest_framework import serializers 
from models import * 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = API
        fields = ('login','password')