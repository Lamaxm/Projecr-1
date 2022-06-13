from os import stat
from urllib import response

from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .models import User
from .serializers import consultantRegisterSerializer, clientRegisterSerializer, UserSerializer, \
    CustomRegisterSerializer


@api_view(['POST'])
def add_user(request : Request):

    new_user = CustomRegisterSerializer(data=request.data)
    if new_user.is_valid():
        new_user.save()
        dataResponse = {
            "msg": "Created Successfully",
            "new_user": new_user.data
        }
        return Response(dataResponse)
    else:
        print(new_user.errors)
        dataResponse = {"msg" : "couldn't create a user"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_user(request: Request, user_id):
    user_dalete = User.objects.get(id=user_id)
    user_dalete.delete()
    return Response({"msg" : "Deleted Successfully"})

"""delete any user"""
@api_view(['PUT'])
def update_user(request : Request, user_id):
    user_update = User.objects.get(id=user_id)

    updated_user = UserSerializer(instance=user_update, data=request.data)
    if updated_user.is_valid():
        updated_user.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_user.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

"""update any user"""

@api_view(['POST'])
def login_user(request : Request):

    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            #create the token , then give the token to the user in the response
            token = AccessToken.for_user(user)
            responseData = {
                "msg" : "Your token is ready",
                "token" : str(token)
            }
            return Response(responseData)


    return Response({"msg" : "please provide your username & password"}, status=status.HTTP_401_UNAUTHORIZED)