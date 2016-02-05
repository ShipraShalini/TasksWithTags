from rest_framework import serializers

from src.common.constants.commonconstants import *


class TaskSerializer(serializers.Serializer):
    task = serializers.CharField(max_length=MAX_TASK_LENGTH)
    tags = serializers.CharField(max_length=MAX_TAG_LENGTH)
    status = serializers.CharField(read_only=True,max_length=MAX_STATUS_LENGTH)
    date_created = serializers.IntegerField(read_only=True)


class SearchSerializer(serializers.Serializer):
    task = serializers.CharField(read_only=True,max_length=MAX_TASK_LENGTH)
    tags = serializers.CharField(max_length=MAX_TAG_LENGTH)
    date_created = serializers.IntegerField(read_only=True)
    status = serializers.CharField(read_only=True,max_length=MAX_STATUS_LENGTH)

class ModifySerializer(serializers.Serializer):
    id=serializers.CharField(max_length=MAX_TASK_LENGTH)
    # task = serializers.CharField(max_length=MAX_TASK_LENGTH)
    # tags = serializers.CharField(max_length=MAX_TAG_LENGTH)
    # taskno = serializers.IntegerField(read_only=True)
    # status = serializers.CharField(read_only=True,max_length=MAX_STATUS_LENGTH)