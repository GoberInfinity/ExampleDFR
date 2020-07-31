from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, FileUploadSerializer


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

    def create(self, request):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        return Response(status=status.HTTP_201_CREATED)
