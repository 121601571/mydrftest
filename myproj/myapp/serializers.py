from rest_framework import serializers
from .models import Snippet, books
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'name', 'addr', 'status', )
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # addr = serializers.CharField()
    # status = serializers.IntegerField()

    # def create(self, validated_data):
    #     """
    #     根据提供的验证过的数据创建并返回一个新的`Snippet`实例。
    #     """
    #     return Snippet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.addr = validated_data.get('addr', instance.addr)

        # instance.save()
        # return instance


class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=False, read_only=True)


    class Meta:
        model = books
        fields = ('owner', 'name', 'descr', 'status')