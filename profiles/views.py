from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from profiles.serializers import Userserializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RegisterViewSet(viewsets.GenericViewSet):
    serializer_class = Userserializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True}, status=status.HTTP_201_CREATED)
