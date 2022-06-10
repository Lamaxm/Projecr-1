from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'as_client', 'as_consultant')



class consultantRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'password2')

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
"""create serialize consultant"""

class clientRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'password','password2','first_name','last_name')


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
        user.as_client=True
        user.save()

        return user

"""create serialize cilent"""