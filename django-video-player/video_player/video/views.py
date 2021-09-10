from django.shortcuts import render, redirect
from .models import History, Bookmark
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.serializers import serialize
from .forms import HistoryForm, BookmarkForm


@csrf_exempt
def history_addview(request):
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = HistoryForm()
    return render(request, 'video/history.html', {'form': form})


def history_list(request):
    obj = History.objects.all().order_by('-date_watched')
    data = serialize("json", obj, fields=('history_url'))
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def bookmark_addview(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = HistoryForm()
    return render(request, 'video/bookmark.html', {'form': form})


def bookmark_list(request):
    obj = Bookmark.objects.all().order_by('-date_added')
    data = serialize("json", obj, fields=('bookmark_url'))
    return HttpResponse(data, content_type="application/json")

# Class based Views

# @method_decorator(csrf_exempt, name='dispatch')
# class HistoryAddedView(CreateView):
#     model = History
#     success_url = '/'
#     fields = ['history_url']
#
#     def form_valid(self, form):
#         return super().form_valid(form)


# @method_decorator(csrf_exempt, name='dispatch')
# class HistoryListView(ListView):
#     model = History
#     template_name = 'video/history.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'objects'
#     ordering = ['-date_watched']


# @method_decorator(csrf_exempt, name='dispatch')
# class BookmarkAddedView(CreateView):
#     model = Bookmark
#     success_url = '/'
#     fields = ['bookmark_url']
#
#     def form_valid(self, form):
#         return super().form_valid(form)


# @method_decorator(csrf_exempt, name='dispatch')
# class BookmarkListView(ListView):
#     model = Bookmark
#     template_name = 'video/bookmarks.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_added']
