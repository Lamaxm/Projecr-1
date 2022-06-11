from rest_framework import serializers
from .models import User, comment, courses


class commentSerializer(serializers.ModelSerializer):
    class Meta :
        model = comment
        fields = '__all__'

class coursesSerializer(serializers.ModelSerializer):
    class Meta :
        model = courses
        fields = '__all__'