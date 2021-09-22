from rest_framework.viewsets import ModelViewSet

from api.users.models import Person
from api.users.serializers.person_serializer import PersonSerializer


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
