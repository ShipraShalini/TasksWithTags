from django import forms

from src.common.constants.commonconstants import *


class ModifyForm(forms.Form):
    id = forms.CharField(label='id',max_length=MAX_TASK_LENGTH)
