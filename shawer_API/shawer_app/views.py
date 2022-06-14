from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import comment, courses
from .permissions import IsOwn
from .serializers import commentSerializer, coursesSerializer, timesSerializer
from user_app.models import User
from user_app.serializers import CustomRegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view , authentication_classes, permission_classes
from rest_framework.request import Request


@api_view(['GET'])
def list_consultant(request : Request):
    """call all consultant in page'consultant"""
    consultant = User.objects.filter(as_consultant=True)

    dataResponse = {
        "msg" : "List of All consultant",
        "consultant" : CustomRegisterSerializer(instance=consultant, many=True).data
    }

    return Response(dataResponse)

@api_view(['GET'])
def comment_list(request, pk):
    """ the view to display comments """
    profile = get_object_or_404(User, pk=pk)
    comment = profile.comments.filter(active=True)
    dataResponse = {
        "msg": "List of All comment",
        "comment_list": commentSerializer(instance=comment, many=True).data
    }

    return Response(dataResponse)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated , IsOwn])
def delete_comment(request: Request, comment_id):
    """ the view for delete comment"""
    comment_dalete = comment.objects.get(id=comment_id)
    comment_dalete.delete()
    return Response({"msg" : "Deleted Successfully"})

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_comment(request : Request):
    """ the view for add new comment"""
    new_comment = commentSerializer(data=request.data)
    if new_comment.is_valid():
        new_comment.save()
        dataResponse = {
            "msg" : "add Successfully",
            "comment" : new_comment.data
        }
        return Response(dataResponse)
    else:
        print(new_comment.errors)
        dataResponse = {"msg" : "couldn't create a comment"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_course(request : Request):
    """ the view for add new course"""
    new_course = coursesSerializer(data=request.data)
    if new_course.is_valid():
        new_course.save()
        dataResponse = {
            "msg" : "create Successfully",
            "course" : new_course.data
        }
        return Response(dataResponse)
    else:
        print(new_course.errors)
        dataResponse = {"msg" : "couldn't create a course"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated , IsOwn])
def delete_course(request: Request, course_id):
    """ the view for delete course"""
    course_dalete = courses.objects.get(id=course_id)
    course_dalete.delete()
    return Response({"msg" : "Deleted Successfully"})

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated , IsOwn])
def update_courses(request : Request, course_id):
    """ the view for update course"""
    course_update = courses.objects.get(id=course_id)

    updated_course = coursesSerializer(instance=course_update, data=request.data)
    if updated_course.is_valid():
        updated_course.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_course.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_time(request : Request):
    """ the view for add new time"""
    new_time = timesSerializer(data=request.data)
    if new_time.is_valid():
        new_time.save()
        dataResponse = {
            "msg" : "create Successfully",
            "time" : new_time.data
        }
        return Response(dataResponse)
    else:
        print(new_time.errors)
        dataResponse = {"msg" : "couldn't create a this time"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)
