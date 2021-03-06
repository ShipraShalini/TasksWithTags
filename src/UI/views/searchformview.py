from django.shortcuts import render

from src.UI.forms.searchform import SearchForm
from src.UI.helpers.createurl import createurl
from src.common.constants.frontendconstants import *

import requests, json


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            url=createurl(SEARCHURL)
            # response = (requests.post(url=url, data=(form.cleaned_data))._content)

            response =json.loads(requests.post(url=url, data=(form.cleaned_data))._content)
            print type(response), response
            # response = json.loads(response)
            # print type(response), response

            #check if data is for one car or multiple
            if isinstance(response,list):
                context= dict(list=response)
            else:
                context= dict(data=response)
            return render(request, RESPONSEHTML, context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, FORMHTML, {'link': 'search-form', 'form': form})