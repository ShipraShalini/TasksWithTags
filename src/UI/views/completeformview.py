from django.shortcuts import render

from src.UI.forms.modifyform import ModifyForm
from src.UI.helpers.createurl import createurl
from src.common.constants.frontendconstants import *


import requests, json


def complete(request):
    if request.method == 'POST':
        form = ModifyForm(request.POST)
        if form.is_valid():
            url=createurl(MODIFYURL)
            params = dict((k, v) for k, v in form.cleaned_data.iteritems() if v)
            response = json.loads(requests.get(url=url, params=params)._content)

            #check if data is for one car or multiple
            if isinstance(response,list):
                context= dict(list=response)
            else:
                context= dict(data=response)
            return render(request, RESPONSEHTML, context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModifyForm()

    return render(request, FORMHTML, {'link': 'modify-form', 'form': form})