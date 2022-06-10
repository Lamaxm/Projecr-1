from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import consultantRegisterSerializer, clientRegisterSerializer, UserSerializer


@api_view(['POST'])
def add_consultant(request : Request):

    new_consultant = consultantRegisterSerializer(data=request.data)
    if new_consultant.is_valid():
        new_consultant.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "consultant" : new_consultant.data
        }
        return Response(dataResponse)
    else:
        print(new_consultant.errors)
        dataResponse = {"msg" : "couldn't create a consultant"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_client(request : Request):

    new_client = clientRegisterSerializer(data=request.data)
    if new_client.is_valid():
        new_client.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "client" : new_client.data
        }
        return Response(dataResponse)
    else:
        print(new_client.errors)
        dataResponse = {"msg" : "couldn't create a client"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_consultant(request : Request):
    consultant = User.objects.filter(as_consultant=True)

    dataResponse = {
        "msg" : "List of All consultant",
        "consultant" : consultantRegisterSerializer(instance=consultant, many=True).data
    }

    return Response(dataResponse)

"""call all consultant for page'consultant"""

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