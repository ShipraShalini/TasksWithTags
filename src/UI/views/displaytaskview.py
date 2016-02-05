import json
import requests
from django.http import HttpResponse

from django.views.generic import TemplateView

from src.UI.helpers.createurl import createurl
from src.common.constants.frontendconstants import *

class DisplayTaskView(TemplateView):
    template_name = RESPONSEHTML

    def get_context_data(self,**kwargs):
        url=createurl(DISPLAYTASK)
        response = json.loads(requests.get(url=url)._content)
        context = super(DisplayTaskView, self).get_context_data(**kwargs)

        if isinstance(response,list):
            context['list']= response
        else:
            context['message']=response

        context['title'] = ALLTASKTITLE
        return context