from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        read_only_fields = ["id", "email"]
        fields = read_only_fields + ["username", "avatar"]
