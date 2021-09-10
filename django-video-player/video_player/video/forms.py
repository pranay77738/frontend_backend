from .models import History, Bookmark
from django.forms import ModelForm


class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ['history_url']


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = ['bookmark_url']
