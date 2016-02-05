import json

from django.http import HttpResponse

from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.libraries.searchclasslib import searchclass
from src.common.serialisers.serialiser import SearchSerializer


class ShowAllView(APIView):
    permission_classes = (permissions.AllowAny, )
    # renderer_classes = (JSONRenderer, )
    serializer_class = SearchSerializer

    def get(self, request):
        if self.request.method == 'GET':
            tasks = searchclass.findall()
            tasks = json.dumps(tasks)
            return HttpResponse(tasks, content_type="application/json")