from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from . import models
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .filters import BlatFilter

# Create your views here.
class BlatListView(generic.ListView):
    model = models.Blat
    template_name = 'blat_list.html'

class BlatDetailView(generic.DetailView):
    model = models.Blat

@login_required
def add_comment_to_blat(request, pk):
    blat = get_object_or_404(models.Blat, pk=pk)
    author = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.blat = blat
            comment.author = author
            comment.save()
            return redirect('dialogue:blat_detail_url', pk=blat.pk)
    else:
        form = CommentForm()
    return render(request, 'dialogue/add_comment_to_blat.html', {'form': form})

@login_required
def dialogue_like(request, pk):
    blat = get_object_or_404(models.Blat, pk=pk)
    if request.method == 'GET':
        return render(request, 'dialogue/dialogue_likes.html', {'blat': blat})
    elif request.method == 'POST':
        user = request.user
        like, created = models.Like.objects.get_or_create(user=request.user, blat=blat)
        if not created:
            # the user already liked this picture before
            models.Like.objects.filter(pk=like.pk).delete()
        else:
            like.save()
        return redirect('dialogue:blat_detail_url', pk=blat.pk)

def search(request):
    charactor_list = models.Blat.objects.all()
    charactor_filter = BlatFilter(request.GET, queryset=charactor_list)
    return render(request, 'dialogue/search.html', {'filter':charactor_filter})
