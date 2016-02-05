from django import forms

from src.common.constants.commonconstants import *


class SearchForm(forms.Form):
    tags = forms.CharField(label='tags',max_length=MAX_TAG_LENGTH)
