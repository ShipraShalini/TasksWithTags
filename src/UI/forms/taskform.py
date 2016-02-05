from django import forms

from src.common.constants.commonconstants import *


class TaskForm(forms.Form):
    task = forms.CharField(label='Task',max_length=MAX_TASK_LENGTH)
    tags = forms.CharField(label='tags',max_length=MAX_TAG_LENGTH)
