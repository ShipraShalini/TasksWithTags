from django.shortcuts import render

from src.UI.forms.modifyform import ModifyForm
from src.UI.helpers.createurl import createurl
from src.common.constants.frontendconstants import *


import requests, json


def delete(request):
    if request.method == 'POST':
        form = ModifyForm(request.POST)
        if form.is_valid():
            url=createurl(MODIFYURL)
            response = json.loads(requests.delete(url=url, data=(form.cleaned_data))._content)
            context= response
            return render(request, RESPONSEHTML, context)
    else:
        form = ModifyForm()

    return render(request, FORMHTML, {'link': 'modify-form', 'form': form})