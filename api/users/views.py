from io import StringIO
from uuid import uuid1
from django.conf import settings
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from .models import User, Data
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, FileUploadSerializer, DataSerializer
from boto3 import resource
import pandas as pd


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
    # It is possible to add more missing data to the csv files, those are merely some examples
    missing_values = ["n/a", "na", "--"]

    def create(self, request):
        file_to_upload = request.data.get(self.file_field)
        if not file_to_upload or not str(file_to_upload).endswith('.csv'):
            raise ParseError("Error loading the content")

        # S3 created here instead of a singleton, because we will need it once
        # Using uuid to create unique identifiers for the name inside the bucket
        # https://en.wikipedia.org/wiki/Universally_unique_identifier
        resource('s3').Object(settings.AWS_STORAGE_BUCKET_NAME,
                              f'{uuid1()}-{file_to_upload}').put(Body=file_to_upload)

        # I check for spurious data first if the data is bad we mark them as na_values
        # Most of the operations of pandas can be replaces by the built in csv module
        transactions = pd.read_csv(
            StringIO(file_to_upload.read().decode('utf-8')), na_values=self.missing_values)

        # It will be better to insert the bad data in other database instead of droppong
        transactions.dropna()

        # You can run a distributed queue speed up the process but I wanted to be
        # sure the atomicity of the database insertion, also the server will handle
        # all the request because of the configuration of gunicorn
        transaction_iter = transactions.iterrows()
        transaction_to_database = [
            Data(
                transaction_id=row['transaction_id'],
                transaction_date=row['transaction_date'],
                transaction_amount=row['transaction_amount'],
                client_id=row['client_id'],
                client_name=row['client_name'],
            )
            for index, row in transaction_iter
        ]
        Data.objects.bulk_create(transaction_to_database)

        return Response(status=status.HTTP_201_CREATED)

class DataViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Retrieves all the data uploaded by the csv file
    """
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['transaction_id', 'transaction_date', 'client_name']
    ordering_fields = '__all__'
