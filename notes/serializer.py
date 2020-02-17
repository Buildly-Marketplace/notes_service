from rest_framework import serializers
from notes import models as notedata


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    user_uuid = serializers.UUIDField(read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = notedata.UserRegistration
        fields = '__all__'


class NoteProviderSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = notedata.NoteProvider
        fields = '__all__'


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = notedata.Note
        fields = '__all__'
