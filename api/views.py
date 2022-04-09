from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import *
from videos.models import Video, Category


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': 'api/videos'},
        {'GET': 'api/videos/id'},
        {'DELETE': 'api/videos/id'},
        {'POST': 'api/videos/add'},
        {'GET': 'api/categories'},
        {'DELETE': 'api/categories/id'},
    ]

    return Response(routes)


@api_view(['GET'])
def getVideos(request):
    videos = Video.objects.all()
    serializer = VideosSerializer(videos, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def getVideo(request, pk):
    video = Video.objects.get(id=pk)
    file = video.file
    thumbnail = video.thumbnail
    serializer = VideosSerializer(video, many=False)

    if request.method == "GET":
        return Response(serializer.data)

    elif request.method == "DELETE":
        file.delete()
        thumbnail.delete()
        video.delete()
        return Response(serializer.data)


@api_view(['POST', 'PUT'])
#@parser_classes([FormParser, MultiPartParser])
def addVideo(request):

    try:
        category = Category.objects.get(name__iexact=request.data['category'])
    except:
        category = Category.objects.create(name=request.data['category'])

    #file = request.data['file']
    serializer = VideosSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(category=category)
    return Response(serializer.data)


@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategoriesSerializer(category, many=False)
    category.delete()
    return Response(serializer.data)


@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
def getProfile(request, pk):
    profile = Profile.objects.get(username=pk)
    serializer = ProfileSerializer(profile, many=False)

    if request.method == "GET":
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
