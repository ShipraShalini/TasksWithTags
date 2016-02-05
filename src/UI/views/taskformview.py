from django.shortcuts import render
import requests, json

from src.UI.forms.taskform import TaskForm
from src.UI.helpers.createurl import createurl
from src.common.constants.frontendconstants import *


def task (request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            url=createurl(TASKURL)
            response = json.loads(requests.post(url=url, data=(form.cleaned_data))._content)
            context= dict(data=response, title=ADDTASKTITLE)
            return render(request, RESPONSEHTML, context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, FORMHTML, {'link': 'task-form', 'form': form})