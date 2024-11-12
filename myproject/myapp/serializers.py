from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 20)
    password = serializers.CharField(max_length = 20)