import json

from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from src.api.helpers import createmessagestring
from src.api.libraries.actionclasslib import actionclass
from src.common.constants.backendconstatants import *
from src.common.serialisers.serialiser import TaskSerializer


class TaskView(GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, )
    serializer_class = TaskSerializer

    def post(self,request):
        if request.method == 'POST':
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                task = actionclass.create(serializer.validated_data)
                return Response(task)
            else:
                return createmessagestring(SERIALISERNOTVALID)

