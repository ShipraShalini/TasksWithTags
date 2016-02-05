import json

from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from src.api.helpers.createmessagestring import createmessagestring
from src.api.libraries.actionclasslib import actionclass
from src.common.serialisers.serialiser import *
from src.common.constants.backendconstatants import *

class ModifyView(GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class =  ModifySerializer

    def get(self,request):
        if request.method == 'GET':
            id = request.GET.get('id', None)
            task = actionclass.toggle(id)._d_
            return Response(task)


    def delete(self, request):
        if request.method == 'DELETE':
            serializer = ModifySerializer(data=request.data)
            print request.data
            if serializer.is_valid():

                message = actionclass.delete(serializer.validated_data)
            else:
                message = createmessagestring(SERIALISERNOTVALID)

            print message, type (message)
            return Response(message)


