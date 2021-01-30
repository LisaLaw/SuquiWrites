from django.shortcuts import render, get_object_or_404
from .models import Entry, Comment
from .forms import EntryForm, CommentForm
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import DetailView


def home(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "suquiwrites/home.html", {"entries": entries})


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    comments = entry.comments.all()
    new_comment = None
    if request.method == "Post":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.connected_entry = entry
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "suquiwrites/entry_detail.html",
        {
            "entry": entry,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


def entry_new(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.published_date = timezone.now()
            entry.save()
            return redirect("entry_detail", pk=entry.pk)
    else:
        form = EntryForm()
    return render(request, "suquiwrites/entry_edit.html", {"form": form})


def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.published_date = timezone.now()
            entry.save()
            return redirect("entry_detail", pk=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, "suquiwrites/entry_edit.html", {"form": form})
