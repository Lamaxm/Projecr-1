from rest_framework import serializers
from .models import User, profil_client, profil_consultant
from allauth.account.adapter import get_adapter


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username',"last_name", 'password', 'as_client',"first_name", 'as_consultant' ,'password2']


class CustomRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    as_client = serializers.BooleanField()
    as_consultant = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'as_client', 'as_consultant','password2')

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password does not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.as_consultant=True
        user.save()

        return user



class consultantRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = profil_consultant
        fields = '__all_'


"""create serialize consultant"""

class clientRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = profil_client
        fields = '__all__'


"""create serialize cilent"""