import json

from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.generics import GenericAPIView

from src.api.libraries.searchclasslib import searchclass
from src.common.serialisers.serialiser import SearchSerializer


class SearchView(GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    # renderer_classes = (JSONRenderer, )
    serializer_class = SearchSerializer

    def post(self, request):
        if self.request.method == 'POST':
            tasks = searchclass.find(request.data['tags'])
            tasks = json.dumps(tasks)
            return HttpResponse(tasks, content_type="application/json")



