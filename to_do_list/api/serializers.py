from django.contrib.auth.models import User

from rest_framework import serializers

from tasks.models import ToDo


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )
        return user


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = [
            'id',
            'title',
            'description',
            'created_at',
            'completed',
            'user'
        ]
        read_only_fields = ['id', 'created_at', 'user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        created_at = instance.created_at
        representation['created_at'] = created_at.strftime(
            '%Y-%m-%d %H:%M:%S')

        return representation
