from rest_framework import serializers
from .models import User, comment, courses, available_time


class commentSerializer(serializers.ModelSerializer):
    """For Serializing Comment"""
    class Meta :
        model = comment
        fields = '__all__'

class coursesSerializer(serializers.ModelSerializer):
    """For Serializing Course"""
    class Meta :
        model = courses
        fields = '__all__'

class timesSerializer(serializers.ModelSerializer):
    """For Serializing Time"""
    class Meta :
        model = available_time
        fields = '__all__'