from uuid import uuid1
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, FileUploadSerializer
from boto3 import resource


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class FileUploadViewSet(viewsets.GenericViewSet):
    """
    Uploads a csv file
    """
    parser_class = FileUploadParser
    serializer_class = FileUploadSerializer
    permission_classes = (AllowAny,)
    file_field = 'file'

    def create(self, request):
        file_to_upload = request.data.get(self.file_field)
        if not file_to_upload or not str(file_to_upload).endswith('.csv'):
            raise ParseError("Error loading the content")

        # S3 crated here instead of a singleton, because we will need it once
        # Using uuid to create unique identifiers for the name inside the bucket
        # https://en.wikipedia.org/wiki/Universally_unique_identifier
        resource('s3').Object(settings.AWS_STORAGE_BUCKET_NAME,
                              f'{uuid1()}-{file_to_upload}').put(Body=file_to_upload)
        return Response(status=status.HTTP_201_CREATED)
