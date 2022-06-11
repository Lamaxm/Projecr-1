from django.shortcuts import render, get_object_or_404
from rest_framework import status
from .models import comment, courses
from .serializers import commentSerializer, coursesSerializer
from user_app.models import User
from user_app.serializers import consultantRegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request


@api_view(['GET'])
def list_consultant(request : Request):
    consultant = User.objects.filter(as_consultant=True)

    dataResponse = {
        "msg" : "List of All consultant",
        "consultant" : consultantRegisterSerializer(instance=consultant, many=True).data
    }

    return Response(dataResponse)

"""call all consultant for page'consultant"""


@api_view(['GET'])
def comment_detile(request, pk):
    profile = get_object_or_404(User, pk=pk)
    comment = profile.comments.filter(active=True)
    dataResponse = {
        "msg": "List of All comment",
        "comment_list": commentSerializer(instance=comment, many=True).data
    }

    return Response(dataResponse)


@api_view(['DELETE'])
def delete_comment(request: Request, comment_id):
    comment_dalete = comment.objects.get(id=comment_id)
    comment_dalete.delete()
    return Response({"msg" : "Deleted Successfully"})

@api_view(['POST'])
def add_comment(request : Request):

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
def add_course(request : Request):

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
def delete_course(request: Request, course_id):
    course_dalete = courses.objects.get(id=course_id)
    course_dalete.delete()
    return Response({"msg" : "Deleted Successfully"})

@api_view(['PUT'])
def update_courses(request : Request, course_id):
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